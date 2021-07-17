# @author: Bilal Shahnawaz
# @github: github.com/bilalshahnawaz

import tkinter
from functools import partial
from .calculate import calculate

# Buttons layout, as they would appear in the application.
button_layout = [
    ["C", "CE"],
    [7, 8, 9, "+"],
    [4, 5, 6, "-"],
    [1, 2, 3, "*"],
    [0, ".", "=", "/"]
]

width, height = 320, 350


def create_window():
    main_window = tkinter.Tk()
    main_window.title("Calculator by Bilal")
    main_window.geometry(f"{width}x{height}")

    output = tkinter.Entry(main_window, font="Helvetica 20")
    output.grid(column=0, row=0, padx=8, pady=10)

    frame = tkinter.Frame(main_window)
    frame.grid(column=0, row=1, pady=5)

    for row_position, button_row in enumerate(button_layout):
        for column_position, button_text in enumerate(button_row):
            button = tkinter.Button(
                frame, text=button_text,
                font="Helvetica 20",
                width=3,
                command=partial(calculate, button_text, output)
            )
            button.grid(column=column_position, row=row_position, padx=2)

    main_window.mainloop()
