from helpers import get_app_mode, set_app_mode_to, check_filename, get_filelist
from dictionary_logic import create_new_dict, propagate_items
from edit_mode import prep_add_word
from quiz_mode import exit_injection


def add_dict(gui, key):
    set_app_mode_to("add_dict")
    create_add_dict_gui(gui, key)
    get_new_filename(gui, key)


def create_add_dict_gui(gui, key):
    gui.set_quizmode(action=True)
    gui.print_s("Add a new dictionary", type=False, field=["label", 3])
    gui.print_s(
        "Enter a name \nfor the dictionary\n[name.csv]:", type=False, field=["label", 1]
    )
    gui.clear_entry_field(0)
    gui.print_s("name.csv", type=False, field=["entry", 0])


def get_new_filename(gui, key):
    filename = gui.wait_for_answer()
    checked_name = check_filename(filename, ".csv")
    if not checked_name or checked_name in get_filelist():
        gui.print_s("Invalid filename", type=False, field=["textbox", 0])
        gui.clear_entry_field(0)
        add_dict(gui, key)
    create_new_dict(checked_name, {})
    prepare_add_mode(gui, key)


def prepare_add_mode(gui, key):
    gui.clean_up_add_dict_gui()
    gui.clear_entry_and_focus(list_of_indices=[0, 1])
    set_app_mode_to("add_mode")
    gui.add_mode_gui()
    gui.print_s("Add new words to the dictionary", type=True, field=["label", 0])
    add_loop(gui, key)


def add_loop(gui, key):
    gui.print_s("Add new words to the dictionary", type=True, field=["textbox", 0])
    while get_app_mode() == "add_mode":
        entry = gui.wait_for_answer()
        prep_add_word(gui, entry) if entry else None
        gui.print_s(
            f"{entry[0]}: " + " ".join(entry[1]), True, field=["textbox", 0]
        ) if entry else None
        gui.clear_entry_and_focus(list_of_indices=[0, 1])
        propagate_items()
        exit_injection()
