import cypher
import tkinter as tk
import string


def encryptcompat():
    global eTextGlobal
    eTextGlobal = ""
    str1 = cypher.encrypt(textEntry.get(), rotEntry.get())
    n = 95
    chunks = [str1[i:i + n] for i in range(0, len(str1), n)]
    encryptedText.set('\n'.join(chunks))
    eTextGlobal = '\n'.join(chunks)
    print("\n" + eTextGlobal)


def decrypt():
    global dTextGlobal
    global dcheck
    global symbols
    dcheck = ""
    dTextGlobal = ""
    if decryptInput.get() != "" and len(decryptInput.get()) <= 92:
        text = []
        for i in range(1, 27):
            text.append(str(i) + " = " + cypher.encrypt(decryptInput.get(), i))
            dcheck = dcheck + cypher.encrypt(decryptInput.get(), i) + " "
        decryptedText.set('\n'.join(text))
        for char in symbols:
            dcheck = dcheck.replace(char, "")
        dTextGlobal = '\n'.join(text)
        print("\n" + dTextGlobal)

    elif len(decryptInput.get()) > 92:
        decryptedText.set("Too many characters... :(")
        dTextGlobal = "Too many characters... :("
        print("\n" + dTextGlobal)

    else:
        decryptedText.set("Invalid Input... :(")
        dTextGlobal = "Invalid Input... :("
        print("\n" + dTextGlobal)


def dTextWrite():
    global dTextGlobal
    dText = open("Decrypted.txt", "a")
    dText.write("\n" + dTextGlobal + "\n")
    dText.close()


def eTextWrite():
    global eTextGlobal
    eText = open("Encrypted.txt", "a")
    eText.write(eTextGlobal + "\n")
    eText.close()


def dTextWrite2():
    global dTextGlobal
    dText = open("Decrypted.txt", "w")
    dText.write(dTextGlobal)
    dText.close()


def eTextWrite2():
    global eTextGlobal
    eText = open("Encrypted.txt", "w")
    eText.write(eTextGlobal + "\n")
    eText.close()


def close():
    global master
    global Dict
    Dict.close()
    master.destroy()


def DictionnaryFunc():
    global Dict2
    global dcheck
    global dictText
    print(dcheck.split())
    text = ""
    for i in dcheck.split():
        if i in Dict2:
            text = text + i + ", "
    dictText.set(text)
    print(text)


dcheck = ""
dTextGlobal = ""
eTextGlobal = ""
symbols = [char for char in string.punctuation]
master = tk.Tk()
encryptedText = tk.StringVar()
decryptedText = tk.StringVar()
dictText = tk.StringVar()
master.title("Cipher")
master.configure(bg="#00bae9")
master.geometry("1355x650")
Dict = open("Dictionnary.txt", "r")
Dict2 = Dict.read()
Dict2 = Dict2.splitlines()
# Widgets
Title = tk.Label(master, text="This is the caesar cipher encryptor:\n", bg="#00bae9", font=("Courier", 10))
cryptText = tk.Label(master, text="Input text to encrypt here:", bg="#00bae9")
textEntry = tk.Entry(master, width=100)
cryptNum = tk.Label(master, text="Input rotation number here:", bg="#00bae9")
rotEntry = tk.Entry(master, width=100)
menubuttone = tk.Menubutton(master, text="Save text to file", width=35)
menubuttond = tk.Menubutton(master, text="Save text to file", width=35)
runButton = tk.Button(master, text="Run Encryptor", command=encryptcompat)
encryptOutput = tk.Label(master, textvariable=encryptedText, bg="#f5f2d0", width=96, height=26, font=("Courier", 9))
Title2 = tk.Label(master, text="This is the caesar cipher decryptor:\n", bg="#00bae9", font=("Courier", 10))
decryptText = tk.Label(master, text="Input text to decrypt here: (92 characters maximum)", bg="#00bae9")
drunButton = tk.Button(master, text="Run Decryptor", command=decrypt)
decryptInput = tk.Entry(master, width=100)
decryptOutput = tk.Label(master, textvariable=decryptedText, bg="#f5f2d0", width=96, height=26, font=("Courier", 9))
closeButton = tk.Button(master, text="Close program", command=close)
dictButton = tk.Button(master, text="Compare to dictionnay", command=DictionnaryFunc)
DictText = tk.Label(master, textvariable=dictText, bg="#f5f2d0", width=96, font=("Courier", 9))

# Grid
Title.grid(row=1, column=0, sticky="W")
cryptText.grid(row=2, column=0, sticky="W")
textEntry.grid(row=3, column=0, sticky="W")
cryptNum.grid(row=4, column=0, sticky="W")
rotEntry.grid(row=5, column=0, sticky="W")
runButton.grid(row=6, column=0, sticky="W")
encryptOutput.grid(row=7, column=0, sticky="W")
Title2.grid(row=1, column=3, sticky="W")
decryptText.grid(row=2, column=3, sticky="W")
decryptInput.grid(row=4, column=3, sticky="W")
drunButton.grid(row=6, column=3, sticky="W")
decryptOutput.grid(row=7, column=3, sticky="W")
menubuttone.grid(row=8, sticky="")
menubuttond.grid(row=8, column=3, sticky="")
closeButton.grid(row=9, sticky="W")
dictButton.grid(row=9, column=3, sticky="E")
DictText.grid(row=10, column=3, columnspan=3)

menubuttone.menu = tk.Menu(menubuttone)
menubuttone["menu"] = menubuttone.menu
menubuttone.menu.add_cascade(label="Write to text file", command=eTextWrite)
menubuttone.menu.add_cascade(label="Write to text file (override previous)", command=eTextWrite2)
menubuttond.menu = tk.Menu(menubuttond)
menubuttond["menu"] = menubuttond.menu
menubuttond.menu.add_cascade(label="Write to text file", command=dTextWrite)
menubuttond.menu.add_cascade(label="Write to text file (override previous)", command=dTextWrite2)

master.mainloop()
