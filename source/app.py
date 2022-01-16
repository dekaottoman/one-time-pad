import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random
import hashlib

root = tk.Tk()
root.minsize(300,600)
root.maxsize(300,600)
root.title('One-Time Encryption')
icon = tk.PhotoImage("icon.ico")
root.iconbitmap(icon)

def popUp(msg:str):
    win = tk.Toplevel()
    win.wm_title("For you!")
    win.maxsize(300,150)
    win.minsize(300,150)

    l = tk.Label(win, text=msg)
    l.place(relwidth=1, relheight=0.2, rely=0.25, relx=0)

    b = ttk.Button(win, text="OK", command=win.destroy)
    b.place(relwidth=0.5, relheight=0.2, rely=0.5, relx=0.25)

def genKey():
    try:
        fPath = filedialog.askopenfilename(initialdir="/", title="Select a File to Generate a Key for")
        f = open(fPath, 'rb')
        file = f.read()
        f.close()
        key = random.randbytes(len(file))
        print(key)
        print(len(file))
        print(len(key))
        f = open(fPath + '.key', 'wb')
        f.write(key)
        f.close()
        popUp("Key Created Succesfully!")
    except:
        popUp("Something went wrong...")

def enc():
    try:
        fPath = filedialog.askopenfilename(initialdir="/", title="Select a File to Encrypt")
        kPath = filedialog.askopenfilename(initialdir="/", title="Select a Key to Use")
        f = open(fPath, 'rb')
        file = f.read()
        f.close()

        k = open(kPath, 'rb')
        key = k.read()
        k.close

        flen = len(file)

        if len(file) == len(key):
            file = bytearray(file)
            key = bytearray(key)
            for i, f in enumerate(file):
                file[i] = f^key[i]

            fenc = open(fPath + ".enc", 'wb')
            fenc.write(file)
            fenc.close()
            popUp("Encryption Done!")
        else:
            popUp("Key not compatible.")
        
    except:
        popUp("Something went wrong...")

def dec():
    try:
        fPath = filedialog.askopenfilename(initialdir="/", title="Select a File to Decrypt")
        kPath = filedialog.askopenfilename(initialdir="/", title="Select a Key to Use")
        f = open(fPath, 'rb')
        file = f.read()
        f.close()

        k = open(kPath, 'rb')
        key = k.read()
        k.close

        if len(file) == len(key):
            file = bytearray(file)
            key = bytearray(key)
            for i, f in enumerate(file):
                file[i] = f^key[i]

            fenc = open(fPath.replace(".enc", ""), 'wb')
            fenc.write(file)
            fenc.close()
            popUp("Decryption Done!")
        else:
            popUp("Key not compatible.")
        
    except:
        popUp("Something went wrong...")

def genChs():
    try:
        path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        f = open(path, 'rb')
        file = f.read()
        f.close()
        file = bytearray(file)
        checksum = hashlib.sha256(file)
        f = open(path + ".chs", 'wb')
        f.write(checksum.hexdigest().encode('ascii'))
        f.close()
        popUp("Checksum created.")
    except:
        popUp("Something went wrong...")

def valInt():
    try:
        filePath = filedialog.askopenfilename(initialdir="/", title="Select File to Check")
        chsPath = filedialog.askopenfilename(initialdir="/", title="Select a Checksum File")
        
        f = open(filePath, 'rb')
        file = f.read()
        file = bytearray(file)
        f.close()
        new_chs = hashlib.sha256(file)

        f = open(chsPath, 'rb')
        chs = f.readline()
        f.close()

        if chs.decode('ascii') == new_chs.hexdigest():
            popUp('Integrity check succesful.')
        else:
            popUp('Integrity check failed')
    except:
        popUp("Something went wrong...")

canvas = tk.Canvas(root, width=300, height=600, bg="#f0f0f0")
canvas.pack()

mainLabel = tk.Label(root, text="One-Time Encryption", bg="#252a35", fg="#f0f0f0")
mainLabel.place(relheight=0.075, relwidth=1, relx=0, rely=0)

img = tk.PhotoImage(file="icon.png")
qr = tk.Label(root, image=img)
qr.place(relwidth=0.9, relheight=0.45 , rely=0.075, relx=0.05)

genKeyBtn = ttk.Button(root, text="Generate New Key", command=genKey)
genKeyBtn.place(relwidth=0.8, relheight=0.075, rely=0.5, relx=0.1)

encBtn = ttk.Button(root, text="Encrypt a File", command=enc)
encBtn.place(relwidth=0.8, relheight=0.075, rely=0.6, relx=0.1)

decBtn = ttk.Button(root, text="Decrypt a File", command=dec)
decBtn.place(relwidth=0.8, relheight=0.075, rely=0.7, relx=0.1)

chsGenBtn = ttk.Button(root, text=" Generate\nChecksum", command=genChs)
chsGenBtn.place(relwidth=0.35, relheight=0.1, rely=0.8, relx=0.1)

intValBtn = ttk.Button(root, text="Validate\nIntegrity", command=valInt)
intValBtn.place(relwidth=0.35, relheight=0.1, rely=0.8, relx=0.55)

stdLabel = tk.Label(root, text="by dekaottoman", bg="#252a35", fg="#f0f0f0")
stdLabel.place(relheight=0.075, relwidth=1, relx=0, rely=0.925)

root.mainloop()