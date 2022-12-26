import json


def add_new_user(user_id: int, user_list:list):
    user_dikt = {"user_id": user_id, "notification": True}
    user_list.append(user_dikt)
    with open("list_of_alerts.json", "w") as file:
        json.dump(user_list, file, indent=4)

def write_json(user_list: list):
    with open("list_of_alerts.json", "w") as file:
        json.dump(user_list, file, indent=4)

def on_of_alert(user_id: int):
    with open("list_of_alerts.json", "r") as file:
        user_list = json.load(file)
    # print(user_list)
    add_new_us = True
    result = True
    for item in user_list:
        if user_id == item["user_id"]:
            if item["notification"]:
                item["notification"] = False
                result = False
            else:
                item["notification"] = True
            # item["notification"] = False if item["notification"] else True
            add_new_us = False
    if add_new_us: add_new_user(user_id, user_list)
    else:  write_json(user_list)

    return result

def take_user_id():
    result_list = []
    with open("list_of_alerts.json", "r") as file:
        user_list = json.load(file)
    for item in user_list:
        if item["notification"]:
            result_list.append(item["user_id"])
    return result_list
