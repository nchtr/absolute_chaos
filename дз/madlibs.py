import tkinter as Tk
Screen = Tk()
Screen.title("PythonGeeks Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="pink")
Label(Screen, text='PythonGeeks Mad Libs Generator').place(x=100, y=20)
#creating buttons
Story1Button = Button(Screen, text='A memorable day', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Blue')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)
 
Screen.update()
Screen.mainloop()