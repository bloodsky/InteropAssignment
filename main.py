from assignments import functions_menu
from row_parser import CsvList
from utils.utils_functions import display_func_menu, get_user_input, invalid_user_input, is_csv_loaded

if __name__ == "__main__":
    csv_struct = CsvList()
    while True:
        display_func_menu(functions_menu)
        try:
            selection = get_user_input(csv_struct)
            if is_csv_loaded(selection, csv_struct.get_csv_status()):
                selected_value = functions_menu[selection]  # Gets the function name
                selected_value(csv_struct)  # add parentheses to call the function
        except ValueError:
            invalid_user_input()

