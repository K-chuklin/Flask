import json


def load_candidates():
    with open('candidates.json', 'r', encoding="utf-8") as file:
        data = json.loads(file.read())
        return data


def get_all():
    data = load_candidates()
    candidates_names = []
    for item in data:
        candidates_names.append(item)
    return candidates_names


def get_by_pk(pk):
    data = load_candidates()
    for candidate in data:
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(skill):
    data = load_candidates()
    cand_info = []
    for candidate in data:
        if skill.lower() in candidate['skills'].lower():
            cand_info.append(candidate)
    return cand_info

