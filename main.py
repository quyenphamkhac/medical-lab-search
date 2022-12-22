from typing import Sequence
from google.cloud import documentai
import json


def process_document_ocr_sample() -> None:
    f = open('response.json')
    data = json.loads(f. read())
    document = data['document']
    text = document['text']
    # print(f"Full document text: {text}\n")
    # print(f"There are {len(document['pages'])} page(s) in this document.\n")

    for page in document['pages']:
        # print(page['detectedLanguages'])
        # print_page_dimensions(page['dimension'])
        # print_detected_langauges(page['detectedLanguages'])
        # print_paragraphs(page['paragraphs'], text)
        # print_blocks(page['blocks'], text)
        print_lines(page['lines'], text)
        # print_tokens(page['tokens'], text)


def print_page_dimensions(dimension) -> None:
    print(f"    Width: {str(dimension['width'])}")
    print(f"    Height: {str(dimension['height'])}")


def print_detected_langauges(
    detected_languages,
) -> None:
    print("    Detected languages:")
    for lang in detected_languages:
        code = lang['languageCode']
        print(f"        {code} ({lang['confidence']:.1%} confidence)")


def print_paragraphs(
    paragraphs, text: str
) -> None:
    print(f"    {len(paragraphs)} paragraphs detected:")
    first_paragraph_text = layout_to_text(paragraphs[0]['layout'], text)
    print(f"        First paragraph text: {repr(first_paragraph_text)}")
    last_paragraph_text = layout_to_text(paragraphs[-1]['layout'], text)
    print(f"        Last paragraph text: {repr(last_paragraph_text)}")


def print_blocks(blocks, text: str) -> None:
    print(f"    {len(blocks)} blocks detected:")
    first_block_text = layout_to_text(blocks[0]['layout'], text)
    print(f"        First text block: {repr(first_block_text)}")
    last_block_text = layout_to_text(blocks[-1]['layout'], text)
    print(f"        Last text block: {repr(last_block_text)}")


def print_lines(lines, text: str) -> None:
    print(f"    {len(lines)} lines detected:")
    for line in lines:
        line_text = layout_to_text(line['layout'], text)
        print(f"        Line text: {repr(line_text)}")
    # first_line_text = layout_to_text(lines[0]['layout'], text)
    # print(f"        First line text: {repr(first_line_text)}")
    # last_line_text = layout_to_text(lines[-1]['layout'], text)
    # print(f"        Last line text: {repr(last_line_text)}")


def print_tokens(tokens, text: str) -> None:
    print(f"    {len(tokens)} tokens detected:")
    for token in tokens:
        token_text = layout_to_text(token['layout'], text)
        # token_text_break_type = ''
        # try:
        #     token_text_break_type = token['detectedBreak']['type']
        # except:
        #     print(token)
        print(f"        First token text: {repr(token_text)}")
        # print(f"        First token break type: {repr(token_text_break_type)}")
    # first_token_text = layout_to_text(tokens[0]['layout'], text)
    # first_token_break_type = tokens[0]['detected_break']['type_']['name']
    # print(f"        First token text: {repr(first_token_text)}")
    # print(f"        First token break type: {repr(first_token_break_type)}")
    # last_token_text = layout_to_text(tokens[-1]['layout'], text)
    # last_token_break_type = tokens[-1]['detected_break']['type_']['name']
    # print(f"        Last token text: {repr(last_token_text)}")
    # print(f"        Last token break type: {repr(last_token_break_type)}")


# def print_image_quality_scores(
#     image_quality_scores,
# ) -> None:
#     print(f"    Quality score: {image_quality_scores['quality_score']:.1%}")
#     print("    Detected defects:")

#     for detected_defect in image_quality_scores.detected_defects:
#         print(
#             f"        {detected_defect['type_']}: {detected_defect['confidence']:.1%}")


def layout_to_text(layout, text: str) -> str:
    """
    Document AI identifies text in different parts of the document by their
    offsets in the entirety of the document's text. This function converts
    offsets to a string.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in layout['textAnchor']['textSegments']:
        start_index = 0
        try:
            start_index = int(segment['startIndex'])
        except:
            print(segment)
        end_index = int(segment['endIndex'])
        response += text[start_index:end_index]
    return response


process_document_ocr_sample()
