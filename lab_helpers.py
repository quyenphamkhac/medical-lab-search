from difflib import get_close_matches

LABS = ['WCB', 'BẠCH CẦU', '%NEU', 'NEUT%', '%LYM', 'LYMPH%',
        '%MONO', 'MONO%', '%EOS', 'EO%', '%BASO', 'BASO%', 'NEU',
        'NEUT#', 'LYM', 'LYMPH#', 'MONO', 'MONO#', 'EOS', 'EO#', 'BASO',
        'BASO#', 'RBC', 'HỒNG CẦU', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC',
        'RDW', 'PLT', 'MPV', 'PDW', 'PCT']

LAB_NAMES = {
    'WCB': 'WCB',
    'BẠCH CẦU': 'Bạch cầu',
    '%NEU': '%NEU',
    'NEUT%': 'NEUT%',
    '%LYM': '%LYM',
    'LYMPH%': 'LYMPH%',
    '%MONO': '%MONO',
    'MONO%': 'MONO%',
    '%EOS': '%EOS',
    'EO%': 'EO%',
    '%BASO': '%BASO',
    'BASO%': 'BASO%',
    'NEU': 'NEU',
    'NEUT#': 'NEUT#',
    'LYM': 'LYM',
    'LYMPH#': 'LYMPH#',
    'MONO': 'MONO',
    'MONO#': 'MONO#',
    'EOS': 'EOS',
    'EO#': 'EO#',
    'BASO': 'BASO',
    'BASO#': 'BASO#',
    'RBC': 'RBC',
    'HỒNG CẦU': 'Hồng cầu',
    'HGB': 'HGB',
    'HCT': 'HCT',
    'MCV': 'MCV',
    'MCH': 'MCH',
    'MCHC': 'MCHC',
    'RDW': 'RDW',
    'PLT': 'PLT',
    'MPV': 'MPV',
    'PDW': 'PDW',
    'PCT': 'PCT'
}


def find_best_match_lab(text: str) -> str:
    best_match_lab_name = ''
    matches = get_close_matches(text.upper(), LABS, n=1, cutoff=0.6)
    if len(matches) > 0:
        best_match_lab = matches.pop()
        best_match_lab_name = LAB_NAMES[best_match_lab]
    return best_match_lab_name


def correct_value(value: float, unit: str) -> float:
    return value
