import os
import requests
import io

from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from documentai_helpers import print_blocks, print_detected_langauges, print_page_dimensions, print_paragraphs, print_lines, print_tokens, print_image_quality_scores

project_id = 'conductive-bank-365208'
location = 'us'  # Format is 'us' or 'eu'
processor_id = '34e550bda24b8927'  # Create processor before running sample
file_path = './data/lab_result_1.png'
file_url = 'https://s3.ap-southeast-1.amazonaws.com/admin.marika.cafe/icons/lab_result_1.png'
# Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
mime_type = 'image/png'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './service_account/medical_lab_sa.json'


def quickstart(
    project_id: str, location: str, processor_id: str, file_path: str, mime_type: str
):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor, e.g.:
    # projects/project_id/locations/location/processor/processor_id
    name = client.processor_path(project_id, location, processor_id)

    image = requests.get(file_url)
    image_content = io.BytesIO(image.content).getvalue()

    # Read the file into memory
    # with open(file_path, "rb") as image:
    #     image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(
        content=image_content, mime_type=mime_type)

    # Configure the process request
    request = documentai.ProcessRequest(name=name, raw_document=raw_document)

    result = client.process_document(request=request)

    # For a full list of Document object attributes, please reference this page:
    # https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document
    document = result.document
    text = document.text
    # Read the text recognition output from the processor
    print("The document contains the following text:")
    print(text)
    for page in document.pages:
        print(f"Page {page.page_number}:")
        print_page_dimensions(page.dimension)
        print_detected_langauges(page.detected_languages)
        print_paragraphs(page.paragraphs, text)
        print_blocks(page.blocks, text)
        print_lines(page.lines, text)
        print_tokens(page.tokens, text)

        # Currently supported in version pretrained-ocr-v1.1-2022-09-12
        if page.image_quality_scores:
            print_image_quality_scores(page.image_quality_scores)


quickstart(project_id="conductive-bank-365208", location="us", processor_id="34e550bda24b8927",
           file_path="./data/lab_result_1.png", mime_type="image/png")
