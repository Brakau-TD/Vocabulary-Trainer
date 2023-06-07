from helpers import (
    set_app_mode_to,
    get_app_mode,
    set_line_index_to,
    get_line_index,
)
from dictionary_logic import (
    get_list_of_items,
    add_word_to_vocab_dict,
    delete_vocab_dict_entry,
    update_vocab_dict,
    propagate_items,
    get_filename,
)


def prepare_edit_mode(gui, key):
    """
    set up app for edit mode
    change textbox to listbox
    change frame 3 for buttons and two entry fields
    get list for listbox
    """
    listbox_frame, quiz_field, edit_field, divider = get_gui_variables(gui)
    id = [quiz_field, edit_field]
    gui.switch_to_edit_view(divider, id, setting=True)
    set_app_mode_to("edit")
    gui.print_s(f"File: {get_filename()[0:-4]}", type=False, field=["label", 0])
    update_edit_listbox(gui, listbox_frame, key)


def prepare_entries_for_edit(gui, line_no, key=""):
    line_no -= 2
    list_of_elements = get_list_of_items()
    de_key = list_of_elements[line_no][0]
    val = list_of_elements[line_no][1::]
    gui.print_s(de_key, field=["entry", 0])
    gui.print_s(",".join(val), field=["entry", 1])
    set_line_index_to(line_no)


def update_edit_listbox(gui, listbox_frame, key):
    list_of_items = create_entry_lines([])
    display_list_of_items_in_listbox(gui, listbox_frame, list_of_items, key)


def get_gui_variables(gui):
    """get gui variables"""
    funcs = gui.get_funcs()
    gui_dict = gui.get_gui_dict()
    listbox_frame = funcs["edit dictionary"][2]
    quiz_field = gui_dict["entry_fields"][0]["quiz"]
    edit_field = gui_dict["entry_fields"][1]["edit"]
    divider = funcs["dividers"][-1]

    return listbox_frame, quiz_field, edit_field, divider


def display_list_of_items_in_listbox(gui, listbox_frame, listbox_lines, key):
    """display list of items in listbox"""
    first = "Choose entry for editing or deletion"
    second = "or add new entry"
    # TODO: listbox_frame and listbox_index are confusing
    # listbox_index should be a variable
    listbox_index = 1
    gui.populate_listbox(
        listbox_lines, key, listbox_index, first_line=first, second_line=second
    )


def create_entry_lines(list_of_items):
    for i, elements in enumerate(get_list_of_items()):
        entry_line = [f"[{i:>3}] {elements[0]}: " + ", ".join(elements[1::])]
        list_of_items.append(entry_line[0])
    return list_of_items


def refresh_listbox(gui, index=1):
    """deletes content of listbox
    Args:
        gui (gui-instance)
        index (int): index of listbox
    """
    gui.clear_listbox(index)


def refresh_edit_gui(gui, text: str) -> None:
    refresh_listbox(gui)
    listbox_frame = gui.get_funcs()["edit dictionary"][2]
    update_edit_listbox(gui, listbox_frame, text)
    gui.clear_entry_field(0)
    gui.clear_entry_field(1)


def update_dict(gui):
    entries = gui.get_entry()
    index = get_line_index()
    if index is False:
        print("Did you want to add a new entry?")
        return
    update_vocab_dict(entries, index)
    end_single_edit_cycle(gui, lines=entries)
    set_line_index_to(False)


def prep_add_word(gui, entry):
    """add entry in edit mode"""
    if get_app_mode() == "edit":
        entry = gui.get_entry()
    add_word_to_vocab_dict(entry[0], entry[1]) if entry else None
    if get_app_mode()=="edit":
        end_single_edit_cycle(gui, lines="Edit dictionary")
    elif get_app_mode()=="add_mode":
        return


def delete_entry(gui, key=None):
    if not get_line_index():
        return
    delete_vocab_dict_entry(gui.get_entry(), get_line_index())
    end_single_edit_cycle(gui)


def end_single_edit_cycle(gui, lines=""):
    propagate_items()
    refresh_edit_gui(gui, lines)
