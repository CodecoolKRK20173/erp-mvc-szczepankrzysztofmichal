# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common


def ask_untill_correct(list_of_games):
    is_correct = False
    FIRST_ELEMENT_IN_LIST = 0
    while is_correct is not True:
        id_of_record = terminal_view.get_inputs(["Line number: "], "Please enter value ")
        is_correct = common.check_is_number(id_of_record[FIRST_ELEMENT_IN_LIST], len(list_of_games))
    return id_of_record[FIRST_ELEMENT_IN_LIST]


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    list_of_games = hr.get_data_to_list()

    # your code
    options = ["Add new record",
               "Remove a record",
               "Update record",
               "Count games each manufacturer",
               "Average of games"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options, "Back to main menu")
        if choice == "1":
            new_record = terminal_view.get_inputs(["Name: ", "Birthyear: "], "Please enter value: ")
            new_record.insert(0, hr.get_random_id(list_of_games))
            list_of_games = hr.add(list_of_games, new_record)
        elif choice == "2":
            id_of_record_to_remove = ask_untill_correct(list_of_games)
            list_of_games = hr.remove(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_remove)))
        elif choice == "3":
            id_of_record_to_update = ask_untill_correct(list_of_games)
            updated_record = terminal_view.get_inputs(["Name: ", "Birthyear: "], "Please enter value: ")
            list_of_games = hr.update(list_of_games, common.check_id_by_number(list_of_games, int(id_of_record_to_update)), updated_record)
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "0":
            hr.export_list_to_file(list_of_games)
        else:
            terminal_view.print_error_message("There is no such choice.")
