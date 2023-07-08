from tkinter import Tk, Button, Entry, Label
from tkinter.messagebox import showinfo

def compute():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            showinfo("Error", "Height and weight must be positive")
        else:
            bmi = (weight * 703) / (height ** 2)
            showinfo("BMI", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        showinfo("Error", "Height and weight must be numbers")

root = Tk()
##I created a function where I get the values for the weight and height and also used exception handlers so that users make sure they enter values for their weight and height thats a nonnegative number and a number bigger than 0.
name_label = Label(root, text='Enter name:')
name_label.grid(row=0, column=0)

weight_label = Label(root, text='Enter height (inches):')
weight_label.grid(row=1, column=0)

height_label = Label(root, text='Enter weight (lbs):')
height_label.grid(row=2, column=0)
##I created labels for each aspect that will be asked for;the name, the weight, and height of the user.
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

weight_entry = Entry(root)
weight_entry.grid(row=1, column=1)

height_entry = Entry(root)
height_entry.grid(row=2, column=1)
##I created entry fields for the name,weight, and height. This is the little box that users will actually insert the information into.
button = Button(root, text='Compute BMI', command=compute)
button.grid(row=3, column=0, columnspan=2)
##Created the 'Compute BMI' button, after pressing this your bmi should be calulcated or an error may pop up to explain why your bmi couldn't be calculated.
root.mainloop()
