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
    filename = "output.json"
    if not os.path.exists(filename):
        # File does not exist → return empty list
        return checklist_data

    # File exists — check if it has content
    if os.path.getsize(filename) == 0:
        # File is empty → return empty list
        return checklist_data

    with open("output.json", "r") as outfile:
        return json.load(outfile)

def create_new_checklist():
    global main_list, checklist_contents, checklist, new_checklist, open_checklist, checklist_name

    open_checklist = True
    if checklist_contents:
        new_checklist = {"Name": checklist_name, "Checklist": checklist_contents.copy()}
        main_list.append(new_checklist)
        checklist_contents = []
    checklist_name = input("Please enter the name of the new checklist: ")

def add_new_entry():
    global checklist_contents
    to_do_input = input("What would you like to add?: ")
    checklist_contents.append(to_do_input)

def show_all_checklists():
    for checklists in main_list:
        print(f"{checklists["Name"]}:\n* {'\n* '.join(checklists['Checklist'])}\n")

def remove_checklist():
    global main_list, command
    index = command.split()[2:]
    index_together = ' '.join(index)
    for checklists in main_list:
        if checklists["Name"] == index_together:
            main_list.remove(checklists)

def save_changes():
    global main_list, new_checklist, checklist_contents
    if checklist_contents:
        new_checklist = ({"Name": checklist_name, "Checklist": checklist_contents.copy()})
        main_list.append(new_checklist)
    with open("output.json", "w") as outfile:
        json.dump(main_list, outfile, indent="")

def show_specific_checklist():
    global selected_checklist, checklist, found_checklist, main_list
    selected_checklist = ' '.join(command.split()[1:])
    for checklist in main_list:
        if selected_checklist in checklist["Name"]:
            found_checklist = True
            print(f"{checklist["Name"]}:\n* {'\n* '.join(checklist['Checklist'])}\n")
    if not found_checklist:
        print("No checklists found, please try again.")
    found_checklist = False

def edit_checklist():
    global selected_checklist, checklist, main_list, found_checklist
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
    found_checklist = False


main_list = load_tasks()
checklist_contents = []
open_checklist = False
found_checklist = False
while True:

    command = input("What would you like to do?(type help for commands): ")

    if command == "exit":
        save_changes()
        break

    elif command == "help":
        help_list()

    elif command == "new checklist":
        create_new_checklist()

    elif command == "add entry" and open_checklist:
        add_new_entry()

    elif "remove checklist" in command:
        remove_checklist()

    elif command == "show all":
        show_all_checklists()

    elif "show" in command and len(command.split()) >= 2:
        show_specific_checklist()

    elif "edit checklist" in command:
        edit_checklist()

    elif command == "save":
        save_changes()

    else:
        print("You probably made a mistake in your input! Please, try again.")







