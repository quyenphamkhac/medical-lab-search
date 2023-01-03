from thefuzz import process
from typing import List, Union

samples = [
    "Yêu cầu xét nghiệm",
    "Kết quả",
    "Tổng phân tích tế bào máu ngoại vi (bằng máy đếm laser)",
    "RBC (Số lượng hồng cầu)",
    "HGB (Hemoglobin)",
    "HCT (Hematocrit)",
    "MCV (Thể tích trung bình HC)",
    "MCH (Lượng HGB trung bình HC)",
    "MCHC (Nồng độ HGB trung bình HC)",
    "RDW-CV (Phân bố kích thước HC)",
    "NRBC# (Số lượng HC có nhân)",
    "NRBC% (Tỷ lệ % HC có nhân)",
    "PLT (Số lượng tiểu cầu)",
    "MPV (Thể tích trung bình TC)",
    "WBC (Số lượng bạch cầu)",
    "NEUT% (Tỷ lệ % BC trung tính)",
    "EO% (Tỷ lệ % BC ưa axít)",
    "BASO% (Tỷ lệ % BC ưa bazơ)",
    "MONO% (Tỷ lệ % BC mono)",
    "LYM% (Tỷ lệ % BC lympho)",
    "NEUT# (Số lượng BC trung tỉnh)",
    "EO# (Số lượng BC va axit)",
    "BASO# (Số lượng BC ưa bazơ)",
    "MONO# (Số lượng BC mono)",
    "LYM# (Số lượng BC lympho)",
    "LUC# (Số lượng BC lớn không bắt mẫu)",
    "LUC% (Tỷ lệ % BC lớn không bắt màu)",
    "Tế bào bắt thường",
    "Tế bào kích thích",
    "0.443",
    "0",
    "0",
    "280",
    "5.7",
    "5.32",
    "51.8",
    "2.4",
    "6.2",
    "36.0",
    "2.75",
    "0.13",
    "0.07",
    "0.33",
    "1.91",
    "0.13",
    "2.4",
    "6.54",
    "129",
    "67.8",
    "19.8",
    "292",
    "15.4",
    "1.2",
    "BS chỉ định: Vũ Công Thắng",
    "Trị số bình thường",
    "Đơn vị",
    "4.5-5.9",
    "135-175",
    "0.41 -0.53",
    "80 - 100",
    "26-34",
    "315-363",
    "10-15",
    "150-400",
    "5-20",
    "4.0 - 10.0",
    "45-75",
    "0-8",
    "0-1",
    "0-8",
    "25-45",
    "1.8-7.5",
    "0-0.8",
    "0-0.1",
    "0-0.8",
    "1.0 - 4.5",
    "0-4",
    "T/L",
    "g/L",
    "L/L",
    "IL",
    "Pg",
    "g/L",
    "%",
    "G/L",
    "%",
    "G/L",
    "fL",
    "G/L",
    "%",
    "%",
    "%",
    "%",
    "%",
    "G/L",
    "G/L",
    "G/L",
    "G/L",
    "G/L",
    "#",
    "%",
    "%",
    "%",
    "Máy XN",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7",
    "7"
]

master_data = {
    "RBC": {
        "name": "RBC",
        "other_names": ["RBC", "Số lượng hồng cầu", "red blood cell"]
    }
}


def find_best_match(keyword: str, choices: List[str]):
    other_names = master_data[keyword].get('other_names')
    matches = []
    for name in other_names or []:
        print('key: ', name)
        match = process.extractOne(name, choices=choices)
        print('match: ', match)
        matches.append(match)
    matches.sort(key=lambda a: a[1])
    best_match = matches.pop()
    return best_match


def find_best_match_by_user_input(keyword: str, choices: List[str]):
    lab_name = find_best_match_lab(keyword=keyword)
    if lab_name is None:
        return None
    return find_best_match(lab_name, choices=choices)


def find_lab_by_name(lab_other_name: str) -> Union[str, None]:
    for key in master_data:
        other_names = master_data[key].get('other_names') or []
        if lab_other_name in other_names:
            return key

    return None


def find_best_match_lab(keyword: str) -> Union[str, None]:
    choices = []
    for key in master_data:
        other_names = master_data[key].get('other_names') or []
        choices = choices + other_names
    best_match = process.extractOne(keyword, choices=choices)
    if best_match is not None:
        lab_name = best_match[0]
        return find_lab_by_name(lab_name)
    else:
        return None


print(find_best_match_by_user_input('rrrbc nè', samples))
