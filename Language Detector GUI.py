import pycld2 as cld2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def DL():
    text_content = text_entry_box.get()
    detected_language = cld2.detect(text_content)
    first = detected_language[2]
    second = first[0]
    output.config(text=second[0])

root = Tk()
root.title('Language Detector by Tahir Habib')
root.geometry("420x400")
root['bg'] = "black"
root.columnconfigure(0, weight=1)


blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 10))
blank_line.grid()


label_heading = Label(root, text="Enter Text Here!", font=("Helvetica", 25), fg="white",
                           bg="black")
label_heading.grid()

blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 5))
blank_line.grid()

text_entry_box_var = StringVar()
text_entry_box = Entry(root, width=20,font=("Helvetica", 20), textvariable=text_entry_box_var)
text_entry_box.grid()

blank_line = Label(root, text="\n", fg="red", bg="black", font=("Helvetica", 30))
blank_line.grid()

Detect_button = Button(root, text="Detect",width=10,font=("Helvetica",13), bg="blue4", fg="white", command=DL)
Detect_button.grid()

output = Label(root, text=" ", fg="green", font=("Helvetica", 20), bg="black")
output.grid()


root.mainloop()


