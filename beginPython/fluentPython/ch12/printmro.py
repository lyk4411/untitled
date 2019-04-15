def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

import tkinter
print_mro(tkinter.Text)