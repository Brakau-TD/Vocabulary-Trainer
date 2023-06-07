from dictionary_logic import (
    get_vocab_object,
    collect_data,
    refresh_stats,
    get_mistakes,
    save_mistakes_filehandler,
    get_success_stats,
)
from helpers import (
    get_app_mode,
    set_app_mode_to,
)
from gui_logic import (
    end_gui_mode,
    display_question,
)
from init_app import hold_mistakes_list, hold_success_stats

from PIL import ImageTk, Image
import random
import sys


def start_quizmode(gui):
    if get_vocab_object().get_dict_length()==0:
        return
    quiztype, difficulty = gui.get_quiztype()   
    gui.set_quizmode(action=True)
    start_training(gui, quiztype, get_vocab_object(), difficulty)


def start_training(gui, quiztype, vocab_dict, difficulty):
    """sets variables for learning to default values"""
    vocab_dict.initialize_session()
    loop_quiz(
        gui, initialize_loop_list(gui, quiztype, vocab_dict), vocab_dict, difficulty
    )


def initialize_loop_list(gui, quiztype, vocab_dict):
    """creates list for loop and loops through items"""
    r_list = [x for x in range(0, vocab_dict.get_dict_length())]
    random.shuffle(r_list) if quiztype == "z" else None
    gui.print_s(
        f"You're in Quizmode. \nThere are {len(r_list)} items",
        True,
        field=["label", 2],
    )
    return r_list


def check_answer(gui, index, answer, vocab_dict, difficulty):
    if vocab_dict.is_correct(index, answer, difficulty):
        gui.print_s(string=f"'{answer}' is correct! ", type=True, field=["textbox", 0])
    else:
        gui.print_s(
            string=f"'{answer}' was wrong :(.",
            type=True,
            field=["textbox", 0],
        )
    gui.print_s(
        string=f"{vocab_dict.return_score_values()} correct out of {vocab_dict.get_dict_length()}.\nThis is item #{index + 2}.",
        type=True,
        field=["label", 2],
    )


def loop_quiz(gui, r_list, vocab_dict, difficulty):
    """
    loops through items of r_list
    params: r_list (list): random or in order, list of integers
    """
    for index in r_list:
        answer = ""
        display_question(gui, index, vocab_dict)
        while not answer:
            answer = gui.wait_for_answer()
            exit_injection()        
        gui.clear_entry_field(0)
        check_answer(gui, index, answer, vocab_dict, difficulty)
        gui.set_focus_to_entry(index=0)
    after_quiz(gui, vocab_dict)


def exit_injection():
    if get_app_mode() == "exit":
        collect_data(), sys.exit()
    return


def after_quiz(gui, vocab_dict):
    hold_success_stats, hold_mistakes_list = manage_mistakes()
    filename, img = create_badge(gui, vocab_dict)
    end_gui_mode(
        gui,
        get_app_mode,
        set_app_mode_to,
        hold_mistakes_list,
        hold_success_stats,
        filename,
        img,
        stats = True
    )
    refresh_stats()
    set_app_mode_to("start")


def manage_mistakes():
    answerstring, m_dict, wrong_items = get_mistakes()
    if answerstring:
        hold_mistakes_list.set_state([answerstring, wrong_items])
        save_mistakes_filehandler(m_dict)
    else:
        hold_mistakes_list.set_state(["Perfect!", "No mistakes!"])
    hold_success_stats.set_state(get_success_stats())
    return hold_success_stats, hold_mistakes_list


def create_badge(gui, vocab_dict=False):
    if vocab_dict:
        percent = vocab_dict.get_percents(string=False)
        filename = f"images/{grading_dict(percent)}"
    else:
        filename = gui.get_gui_dict()["images"]["add_mode"]
    # get the image "firstplace.png" from the folder "/images"
    img = Image.open(filename)
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return filename, img


def grading_dict(percent):
    grading_dict = {
        90: "firstplace.gif",
        80: "secondplace.gif",
        65: "thirdplace.gif",
        50: "fourthplace.gif",
        0: "noplace.gif",
    }
    grades = list(grading_dict.keys())
    for i in grades:
        if percent >= i:
            return grading_dict[i]
