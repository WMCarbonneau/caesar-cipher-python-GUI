import cypher


def hi():
    print("HEllo")


def decrypt():
    Word = input("Word:")
    for i in range(1, 27):
        print(str(i) + " = " + cypher.encrypt(Word,i))


from tkinter import *
root = Tk()
root.geometry("300x350")
root.configure(bg="#00bae9")
menubutton = Menubutton(root, text = "File", width = 35)
menubutton.grid()
menubutton.menu = Menu(menubutton)
menubutton["menu"]=menubutton.menu
menubutton.menu.add_cascade(label = "New file", command = hi)
menubutton.pack()
root.mainloop()
