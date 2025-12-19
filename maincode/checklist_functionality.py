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
    # If there is content in the buffer, save it as a new checklist
    if checklist_contents:
        new_checklist = {"Name": checklist_name, "Checklist": checklist_contents.copy()}
        main_list.append(new_checklist)
        checklist_contents = {}  # Reset for the next one

    return main_list, checklist_contents


def add_new_entry(checklist_contents, task_name):
    # Direct assignment: Set the task name as Key and False (not done) as Value
    checklist_contents[task_name] = False
    return checklist_contents


def show_all_checklists(main_list):
    for checklist in main_list:
        print(f"{checklist['Name']}:")
        # Loop through Key (task) and Value (status)
        for task, is_completed in checklist['Checklist'].items():
            status_mark = "[x]" if is_completed else "[ ]"
            print(f"* {status_mark} {task}")
        print("\n")


def remove_checklist(main_list, command):
    # Extract the name from the command (e.g., "remove checklist My List")
    name_parts = command.split()[2:]
    target_name = ' '.join(name_parts)

    for checklist in main_list:
        if checklist["Name"] == target_name:
            main_list.remove(checklist)
            print(f"Removed checklist: {target_name}")
            break  # Stop after finding and removing it
    return main_list


def save_changes(main_list):
    with open("../data/output.json", "w") as outfile:
        json.dump(main_list, outfile, indent=4)  # indent=4 makes it readable
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


def edit_checklist(command, main_list):
    found_checklist = False
    target_name = ' '.join(command.split()[2:])

    for checklist in main_list:
        if target_name in checklist["Name"]:
            found_checklist = True
            editing_command = input("What would you like to edit? (name/contents): ")

            if editing_command == "name":
                new_name = input("Please enter the new name for the checklist: ")
                checklist["Name"] = new_name

            elif editing_command == "contents":
                action = input("Would you like to edit, add or delete an entry?: ")

                if action == "delete":
                    task_to_delete = input("Enter the name of the entry to delete: ")
                    # Use .pop() with the key name to remove from dictionary
                    if task_to_delete in checklist["Checklist"]:
                        checklist["Checklist"].pop(task_to_delete)
                    else:
                        print("Entry not found.")

                elif action == "add":
                    new_task = input("What entry would you like to add?: ")
                    checklist["Checklist"][new_task] = False

                elif action == "edit":
                    old_task = input("Enter the name of the entry you want to change: ")
                    if old_task in checklist["Checklist"]:
                        # Save the old status
                        old_status = checklist["Checklist"].pop(old_task)
                        # Ask for new name and restore status
                        new_task_name = input("Enter the new text for this entry: ")
                        checklist["Checklist"][new_task_name] = old_status
                    else:
                        print("Entry not found.")

                else:
                    print("Invalid command.")

    if not found_checklist:
        print("No checklists found, please try again.")
    return main_list


if __name__ == "__main__":
    main_list = load_tasks()
    checklist_contents = {}
    checklist_name = ""
    open_checklist = False  # Flag to track if we are currently building a list

    while True:
        command = input("What would you like to do? (type help for commands): ")

        if command == "exit":
            main_list = save_changes(main_list, checklist_contents, checklist_name)
            break

        elif command == "help":
            help_list()

        elif command == "new checklist":
            checklist_name = input("Please enter the name of the new checklist: ")

            main_list, checklist_contents = create_new_checklist(
                main_list,
                checklist_contents,
                checklist_name
            )
            open_checklist = True

        elif command == "add entry":
            if open_checklist:
                task_input = input("What would you like to add?: ")


                checklist_contents = add_new_entry(checklist_contents, task_input)
            else:
                print("Please create a 'new checklist' first.")

        elif "remove checklist" in command:
            main_list = remove_checklist(main_list, command)

        elif command == "show all":
            show_all_checklists(main_list)

        elif "show" in command and len(command.split()) >= 2:
            show_specific_checklist(main_list, command)

        elif "edit checklist" in command:
            main_list = edit_checklist(command, main_list)

        elif command == "save":
            main_list = save_changes(main_list, checklist_contents, checklist_name)
            # After saving, we clear the current working buffer
            checklist_contents = {}
            open_checklist = False
            print("Progress saved!")

        else:
            print("You probably made a mistake in your input! Please, try again.")