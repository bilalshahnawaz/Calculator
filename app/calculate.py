# @author: Bilal Shahnawaz
# @github: github.com/bilalshahnawaz

from tkinter import END

def calculate(btn_text, entry_box):
    """
    Evaluates the the text in the entry box and outputs the answer.
    :param btn_text: String containing the text of the button which executed
    this function.
    :param entry_box: The entry field object created with tkinter.Entry.
    """
    # List of operations which are not supposed to be evaluated.
    operations = ["=", "C", "CE"]
    # List containing the arithmetics in the calculator.
    arithmetics = ["+", "-", "*", "/"]
    if btn_text not in operations:
        entry_box.insert(END, btn_text)
    elif btn_text == "=":
        entry_text = entry_box.get()
        # Check if the entry box is not empty or does not consist of
        # just whitespaces and if the text contains an arithmetic.
        if len(entry_text) > 0 and not entry_text.isspace() and \
                any(arithmetic in entry_text for arithmetic in arithmetics):
            # Clear the entry box.
            entry_box.delete(0, END)
            # Attempt to evaluate the text in entry box and insert it.
            try:
                result = eval(entry_text)
            except Exception as error:
                print(error)
            else:
                entry_box.insert(END, result)
    # Clear the entry box if "C" or "CE" was pressed.
    else:
        entry_box.delete(0, END)