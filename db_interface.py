from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


conn = sqlite3.connect('vehicle.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `vehicle` (car_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, make TEXT, model TEXT, style TEXT, mpg INTEGER, color TEXT)") 


def Create():
    if  MAKE.get() == "" or MODEL.get() == "" or STYLE.get() == "" or MPG.get() == "" or COLOR.get() == "" : #or PASSWORD.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        # Database()
        cursor.execute("INSERT INTO `vehicle` (make, model, style, mpg, color) VALUES(?, ?, ?, ?, ?)", (str(MAKE.get()), str(MODEL.get()), str(STYLE.get()), str(MPG.get()), str(COLOR.get())))
        conn.commit()
        MAKE.set("")
        MODEL.set("")
        STYLE.set("")
        MPG.set("")
        COLOR.set("")
        # cursor.close()
        # conn.close()
        txt_result.config(text="Created data!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `vehicle` ORDER BY `make` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5]))
    # cursor.close()
    # conn.close()
    txt_result.config(text="Successfully read the data from database", fg="black")


def Update():
    Read()


def Delete():
    cursor.execute('''DELETE FROM 'vehicle' WHERE make = ?''',(str(MAKE),))
    conn.commit()    


def Exit():
    result = tkMessageBox.askquestion('Simple Car Database', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        cursor.close()
        conn.close()
        exit()


root = Tk()
root.title("Simple Car Database")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)



#==================================VARIABLES==========================================
# FIRSTNAME = StringVar()
COLOR = StringVar()
MAKE = StringVar()
MODEL = StringVar()
STYLE = StringVar()
MPG = StringVar()


#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
# Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('arial', 16)).pack(side=LEFT)
# Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female", font=('arial', 16)).pack(side=LEFT)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Simple Car Database")
txt_title.pack()
txt_make = Label(Forms, text="Make:", font=('arial', 16), bd=15)
txt_make.grid(row=0, stick="e")
txt_model = Label(Forms, text="Model:", font=('arial', 16), bd=15)
txt_model.grid(row=1, stick="e")
txt_style = Label(Forms, text="Style:", font=('arial', 16), bd=15)
txt_style.grid(row=2, stick="e")
txt_mpg = Label(Forms, text="MPG:", font=('arial', 16), bd=15)
txt_mpg.grid(row=3, stick="e")
txt_color = Label(Forms, text="Color:", font=('arial', 16), bd=15)
txt_color.grid(row=4, stick="e")
# txt_password = Label(Forms, text="Password:", font=('arial', 16), bd=15)
# txt_password.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
make = Entry(Forms, textvariable=MAKE, width=30)
make.grid(row=0, column=1)
model = Entry(Forms, textvariable=MODEL, width=30)
model.grid(row=1, column=1)
# RadioGroup.grid(row=2, column=1)
style = Entry(Forms, textvariable=STYLE, width=30)
style.grid(row=2, column=1)
mpg = Entry(Forms, textvariable=MPG, width=30)
mpg.grid(row=3, column=1)
color = Entry(Forms, textvariable=COLOR, width=30)
color.grid(row=4, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", command=Update)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLE) #command=Delete
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("Make", "Model", "Style", "MPG", "Color"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Make', text="Make", anchor=W)
tree.heading('Model', text="Model", anchor=W)
tree.heading('Style', text="Style", anchor=W)
tree.heading('MPG', text="MPG", anchor=W)
tree.heading('Color', text="Color", anchor=W)
# tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
# tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.pack()


#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
