import json
import os


def load_tasks():
    checklist_data = []
    filename = "../dist/data/output.json"
    if not os.path.exists(filename):

        return checklist_data


    if os.path.getsize(filename) == 0:

        return checklist_data

    with open("../dist/data/output.json", "r") as outfile:
        return json.load(outfile)


def create_new_checklist(main_list, checklist_contents, checklist_name):

    if checklist_contents:
        new_checklist = {"Name": checklist_name, "Checklist": checklist_contents.copy()}
        main_list.append(new_checklist)
        checklist_contents = {}

    return main_list, checklist_contents


def add_new_entry(checklist_contents, task_name):

    checklist_contents[task_name] = False
    return checklist_contents


def show_all_checklists(main_list):
    for checklist in main_list:
        print(f"{checklist['Name']}:")

        for task, is_completed in checklist['Checklist'].items():
            status_mark = "[x]" if is_completed else "[ ]"
            print(f"* {status_mark} {task}")
        print("\n")


def remove_checklist(main_list, checklist):
    if checklist in main_list:
            main_list.remove(checklist)
    return main_list


def save_changes(main_list):
    with open("../dist/data/output.json", "w") as outfile:
        json.dump(main_list, outfile, indent=4)
    return main_list


def show_specific_checklist(main_list, command):
    found_checklist = False
    target_name = ' '.join(command.split()[1:])

    for checklist in main_list:
        if target_name in checklist["Name"]:
            found_checklist = True
            print(f"{checklist['Name']}:")
            for task, is_completed in checklist['Checklist'].items():
                status_mark = "[x]" if is_completed else "[ ]"
                print(f"* {status_mark} {task}")
            print("\n")

    if not found_checklist:
        print("No checklists found, please try again.")



