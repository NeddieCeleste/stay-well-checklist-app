import json
import os

def help_list():
    print("""* These are the available commands:
        * new checklist -> adds a new checklist
        * add entry -> adds a new entry to current checklist
        * remove checklist [name] -> removes a checklist entry
        * edit checklist [name] -> edits an existing checklist entry
        * show [name] -> shows a checklist entry
        * show all -> prints out all available checklist entries
        * save -> saves changes made so far
        * exit -> exits the program""")

def load_tasks():
    checklist_data = []
    filename = "../data/output.json"
    if not os.path.exists(filename):
        # File does not exist → return empty list
        return checklist_data

    # File exists — check if it has content
    if os.path.getsize(filename) == 0:
        # File is empty → return empty list
        return checklist_data

    with open("../data/output.json", "r") as outfile:
        return json.load(outfile)

def create_new_checklist(main_list, checklist_contents, checklist_name):
    if checklist_contents:
        new_checklist = {"Name": checklist_name, "Checklist": checklist_contents.copy()}
        main_list.append(new_checklist)
        checklist_contents = []
    checklist_name = input("Please enter the name of the new checklist: ")
    return main_list, checklist_contents, checklist_name

def add_new_entry(checklist_contents):
    to_do_input = input("What would you like to add?: ")
    checklist_contents.append(to_do_input)
    return checklist_contents

def show_all_checklists(main_list):
    for checklists in main_list:
        print(f"{checklists["Name"]}:\n* {'\n* '.join(checklists['Checklist'])}\n")

def remove_checklist(main_list, command):
    index = command.split()[2:]
    index_together = ' '.join(index)
    for checklists in main_list:
        if checklists["Name"] == index_together:
            main_list.remove(checklists)
    return main_list

def save_changes(main_list, checklist_contents, checklist_name):
    if checklist_contents:
        new_checklist = ({"Name": checklist_name, "Checklist": checklist_contents.copy()})
        main_list.append(new_checklist)
    with open("../data/output.json", "w") as outfile:
        json.dump(main_list, outfile, indent="")
    return main_list

def show_specific_checklist(main_list, command):
    found_checklist = False
    selected_checklist = ' '.join(command.split()[1:])
    for checklist in main_list:
        if selected_checklist in checklist["Name"]:
            found_checklist = True
            print(f"{checklist["Name"]}:\n* {'\n* '.join(checklist['Checklist'])}\n")
    if not found_checklist:
        print("No checklists found, please try again.")

def edit_checklist(command, main_list):
    found_checklist = False
    selected_checklist = ' '.join(command.split()[2:])
    for checklist in main_list:
        if selected_checklist in checklist["Name"]:
            found_checklist = True
            editing_command = input("What would you like to edit?(name/contents): ")
            if editing_command == "name":
                new_name = input("Please enter the new name for the checklist: ")
                checklist["Name"] = new_name
            elif editing_command == "contents":
                new_content_command = input("Would you like to edit, add or delete entry?: ")
                if new_content_command == "edit":
                    entry_index = int(input("Which entry would you like to edit?: ")) - 1
                    if entry_index > len(checklist["Checklist"]):
                        print("Invalid entry. Please try again.")
                    else:
                        checklist["Checklist"].pop(entry_index)
                        new_entry = input("What entry would you like to add?: ")
                        checklist["Checklist"].insert(entry_index, new_entry)
                elif new_content_command == "delete":
                    entry_index = int(input("Which entry would you like to delete?: ")) - 1
                    if entry_index > len(checklist["Checklist"]):
                        print("Invalid entry. Please try again.")
                    else:
                        checklist["Checklist"].pop(entry_index)
                elif new_content_command == "add":
                    new_entry = input("What entry would you like to add?: ")
                    checklist["Checklist"].append(new_entry)
                else:
                    print("Invalid command.")
    if not found_checklist:
        print("No checklists found, please try again.")
    return main_list


main_list = load_tasks()
checklist_contents = []
open_checklist = False
checklist_name = ""
while True:

    command = input("What would you like to do?(type help for commands): ")

    if command == "exit":
        main_list = save_changes(main_list, checklist_contents, checklist_name)
        break

    elif command == "help":
        help_list()

    elif command == "new checklist":
        open_checklist = True
        main_list, checklist_contents, checklist_name = create_new_checklist(
            main_list,
            checklist_contents,
            checklist_name)

    elif command == "add entry" and open_checklist:
        checklist_contents = add_new_entry(checklist_contents)

    elif "remove checklist" in command:
        main_list = remove_checklist(main_list, command)

    elif command == "show all":
        show_all_checklists(main_list)

    elif "show" in command and len(command.split()) >= 2:
        show_specific_checklist(main_list, command)
        found_checklist = False

    elif "edit checklist" in command:
        main_list = edit_checklist(command, main_list)

    elif command == "save":
        main_list = save_changes(main_list, checklist_contents, checklist_name)

    else:
        print("You probably made a mistake in your input! Please, try again.")







