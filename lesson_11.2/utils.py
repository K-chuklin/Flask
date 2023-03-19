import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding="utf-8") as file:
        data = json.loads(file.read())
        return data


def get_candidate(candidate_id):
    data = load_candidates_from_json()
    for candidate in data:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    data = load_candidates_from_json()
    info = []
    for candidate in data:
        if candidate_name.lower() in candidate['name'].lower():
            info.append(candidate)
    return info


def get_candidates_by_skill(skill_name):
    data = load_candidates_from_json()
    info = []
    for candidate in data:
        if skill_name.lower() in candidate['skills'].lower():
            info.append(candidate)
    return info

