"""
Main menu for the vocabulary trainer.
"""
from helpers import get_filelist, set_app_mode_to, get_app_mode
from file_handling import FileHandling

# import all functions from dictionary_logic.py that are used in vocab_main.py
from dictionary_logic import (
    collect_data,
    handle_loading_dict,
    is_vocab_dict,
    set_outside_dictionary_to_file_instance,
    save_file_object_instance,
    delete_instances,
    refresh_stats,
)
from edit_mode import (
    prepare_entries_for_edit,
    prepare_edit_mode,
    update_dict,
    prep_add_word,
    delete_entry,
)
from quiz_mode import start_quizmode
from add_dict import add_dict
from gui_logic import end_gui_mode
from init_app import *
import sys


def main_menu(gui, keyword, funcs):
    """
    calls the function that is associated with the button that was pressed
    Args:
        gui (obj): gui object
        keyword (str): name of the button"""
    funcs[keyword][0](gui, keyword)


def present_choice(gui, key, *args, **kwargs):
    """implements the load function for the main menu
    Args:
        gui (obj): gui object
        key (event): tkinter event
    """
    if get_app_mode() != "start":
        return
    first_l = kwargs["first_line"] if "first_line" in kwargs else "Choose a dictionary"
    second_l = kwargs["second_line"] if "second_line" in kwargs else "-" * 25
    l_i = kwargs["listbox_index"] if "listbox_index" in kwargs else 0
    gui.populate_listbox(get_filelist(), key, l_i, first_l, second_l)
    set_app_mode_to("start")


def get_line(gui, line_index: int, listbox_index: int, line_content: str) -> None:
    print(f"line_index: {line_index}, listbox_index: {listbox_index}")

    if get_app_mode() == "start" and line_index >= 2:
        handle_loading_dict(line_content)
        gui.clear_listbox(listbox_index, text=f"File '{line_content}' loaded.")

    elif get_app_mode() == "edit" and line_index > 1:
        prepare_entries_for_edit(gui, line_no=line_index)


def quiz(gui, keyword, *args, **kwargs):
    if get_app_mode() != "loaded" or not is_vocab_dict():
        return
    set_app_mode_to("quiz")
    gui.clear_label(0)
    start_quizmode(gui)
    set_app_mode_to("start")
    restore_app_mode(gui)  # TODO: check if this works
    gui.show_quote()


def create(gui, keyword, *args, **kwargs):
    """function is called from the button "create
    Args:
        gui (gui-instance)
        keyword (str): function call of the button ("create")"""
    if get_app_mode() != ("start" or "loaded"):
        return

    gui.clear_label(0)
    gui.clear_listbox(0, text="Add a dictionary")
    add_dict(gui, keyword)
    # exit_mode(gui,key)


def edit(gui, keyword, *args, **kwargs):
    if get_app_mode() != "loaded":
        return

    gui.clear_label(0)
    prepare_edit_mode(gui, keyword)


def send(gui, keyword, *args, **kwargs):
    """function is called from the button "send"
    Args:
        gui (gui-instance)
        keyword (str): name of the button ("send")
    """
    if get_app_mode() == "edit":
        update_dict(gui)
    elif get_app_mode() == "add_dict":
        gui.decision.set(keyword)
    elif get_app_mode() == "quiz":
        gui.decision.set(keyword)
    elif get_app_mode() == "add_mode":
        gui.decision.set(keyword)


def add_item(gui, keyword, *args, **kwargs):
    if get_app_mode() != "edit":
        return
    prep_add_word(gui, entry=[])


def delete(gui, keyword, *args, **kwargs):
    if get_app_mode() != "edit":
        return
    delete_entry(gui)


def add_word(gui, keyword, *args, **kwargs):
    pass


def add_mode(gui, keyword, *args, **kwargs):
    pass


def prepare_file_loading(filename):
    """
    gets the content of a line in the listbox and passes it to the loading function
    """
    handle_loading_dict(filename)


def exit_mode(gui, keyword, *args, **kwargs):
    if get_app_mode() == "edit":
        gui.switch_to_edit_view(setting=False, id=[0, 1], divider=False)
    elif get_app_mode() == "quiz":
        refresh_stats()
    elif get_app_mode() == "add_dict" or get_app_mode() == "add_mode":
        gui.set_quizmode(action=False)
    end_gui_mode(
        gui, get_app_mode, set_app_mode_to, hold_mistakes_list=[], hold_success_stats=[]
    )
    gui.show_quote()


def exit_app(gui):
    set_app_mode_to("exit")
    gui.decision.set("exit")
    collect_data()
    sys.exit()


def restore_app_mode(gui):
    set_outside_dictionary_to_file_instance(dict_obj.get_state().get_dict())
    save_file_object_instance()
    delete_instances()
    gui.revert_to_start()
    gui.show_quote()
