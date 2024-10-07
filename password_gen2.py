from tkinter import *
from random import choice

num = "1234567890"
alphanum = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

def create_pass():
    the_choice = Tchoice.get()
    if not the_choice:
        result_box.delete(1.0, END)
        result_box.insert(END, "Select the type of password you'd like")
        return

    try:
        length = int(pass_length.get())
    except ValueError:
        result_box.delete(1.0, END)
        result_box.insert(END, "Enter a valid password length")
        return

    rand_pass = [choice(the_choice) for _ in range(length)]
    result = "".join(rand_pass)

    result_text = result
    result_box.delete(1.0, END)
    result_box.insert(END, result_text)

    global generated_password
    generated_password = result

def copy_and_close():
    if generated_password:
        window.clipboard_clear()
        window.clipboard_append(generated_password)
        window.after(200, window.destroy)  

window = Tk()
window.geometry("650x450")
window.title("Enhanced Password Generator")

main_frame = Frame(window, bg="#fffce0", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

prog_name = Label(main_frame, font=('Helvetica', 18, 'bold'), text="Random Password Generator", fg="darkblue",
                  bg="#fffce0")
prog_name.pack(pady=10)

length_frame = Frame(main_frame, bg="#fffce0")
length_frame.pack(pady=10)

size_label = Label(length_frame, text='Length:', font=('Arial', 12), bg="#fffce0")
size_label.pack(side=LEFT, padx=10)

pass_length = Spinbox(length_frame, from_=8, to=100, width=5)
pass_length.pack(side=LEFT)

choose_type_frame = Frame(main_frame, bg="#fffce0")
choose_type_frame.pack(pady=10)

choose_type = Label(choose_type_frame, font=('Arial', 14), text='Choose a type:', bg="#fffce0")
choose_type.pack()

Tchoice = StringVar()
Tchoice.set("") 

num_choice = Radiobutton(choose_type_frame, font=('Arial', 12), text="Numeric", variable=Tchoice, value=num, bg="#fffce0")
num_choice.pack(side=LEFT, padx=10)
alpha_num_choice = Radiobutton(choose_type_frame, font=('Arial', 12), text="AlphaNumeric", variable=Tchoice, value=alphanum, bg="#fffce0")
alpha_num_choice.pack(side=LEFT, padx=10)
special_choice = Radiobutton(choose_type_frame, font=('Arial', 12), text="Special", variable=Tchoice, value=spalphanum, bg="#fffce0")
special_choice.pack(side=LEFT, padx=10)

buttons_frame = Frame(main_frame, bg="#fffce0")
buttons_frame.pack(pady=20)

gen_button = Button(buttons_frame, text='Generate Password', command=create_pass, font=('Arial', 12), bg="lightblue")
gen_button.pack()

result_frame = Frame(main_frame, bg="#fffce0")
result_frame.pack(pady=10)

result_title = Label(result_frame, text="Generated Password:", font=('Arial', 14, 'bold'), bg="#fffce0")
result_title.pack()

result_box = Text(result_frame, height=2, width=30, font=('Arial', 12))
result_box.pack(pady=10)

copy_button = Button(result_frame, text='Copy Password', command=copy_and_close, font=('Arial', 12), bg="lightgreen", height=3, width=15)
copy_button.pack(pady=10)

generated_password = ""

window.mainloop()


