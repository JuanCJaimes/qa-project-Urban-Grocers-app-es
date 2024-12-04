from copy import deepcopy

BASE_KIT_BODY = {"name": ""}

def get_kit_body(name):
    kit_body = deepcopy(BASE_KIT_BODY)
    kit_body["name"] = name
    return kit_body

