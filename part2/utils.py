import json
from typing import List, Dict

PATH = "candidates.json"


def load_candidates_from_json(path: str) -> List[dict]:
    """
    Return list of all candidates from json file
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> Dict:
    for candidate in load_candidates_from_json(PATH):
        if candidate["id"] == candidate_id:
            return candidate
    return "Нет такого кандидата"


def get_candidates_by_name(candidate_name: str) -> Dict:
    for candidate in load_candidates_from_json(PATH):
        if candidate["name"] == candidate_name:
            return candidate
    return "Нет такого кандидата"



def get_candidate_by_skill(skill: str) -> List:
    candidate_by_skill_list = []
    for candidate in load_candidates_from_json(PATH):
        if skill in candidate["skills"].lower().split(", "):
            candidate_by_skill_list.append(candidate)
    return candidate_by_skill_list

