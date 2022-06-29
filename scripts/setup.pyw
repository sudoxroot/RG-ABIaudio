import os
import webbrowser
import subprocess
from tkinter import *
from tkinter.ttk import *
from os.path import exists

from sympy import li
master = Tk()
master.geometry("300x200")
master.title("RG-ABI audio Setup")
master.iconbitmap("./scripts/mainIcon.ico")


def openEditor():
    if not exists("links.conf"):
        with open('links.conf', 'w') as f:
            f.write('Youtube Link\nTimestamp (Leave blank if specified in link)\nName\nhttps://youtu.be/dQw4w9WgXcQ\n0\nRick Astley\nhttps://www.youtube.com/watch?v=LDU_Txk06tM\n28s\nCrabby Crab\nhttps://www.youtube.com/watch?v=BMJjq3qG0vY\n1m58s\nLDT\nhttps://youtu.be/LACbVhgtx9I?t=44\n\nMuffin Lover')
        popupBonusWindow = Tk()
        popupBonusWindow.wm_title("Info")
        popupBonusWindow.iconbitmap("./scripts/mainIcon.ico")
        popupBonusWindow.attributes("-topmost", True)
        labelBonus = Label(popupBonusWindow, text="   An example config will be created automatically   ")
        labelBonus.pack(pady = 10)
        B1 = Button(popupBonusWindow, text="Okay", command=popupBonusWindow.destroy)
        B1.pack(pady = 10)
    webbrowser.open("links.conf")

def goBack():
    master.destroy()
    os.system("python3 .\index.pyw")


def downloadAudio():
    if not exists("links.conf"):
        popupBonusWindow = Tk()
        popupBonusWindow.wm_title("Info")
        popupBonusWindow.iconbitmap("./scripts/mainIcon.ico")
        popupBonusWindow.attributes("-topmost", True)
        labelBonus = Label(popupBonusWindow, text="   You have to create a config first   ")
        labelBonus.pack(pady = 10)
        labelBonus = Label(popupBonusWindow, text="   To do this, press \"Open Editor\"   ")
        labelBonus.pack(pady = 1)
        B1 = Button(popupBonusWindow, text="Okay", command=popupBonusWindow.destroy)
        B1.pack(pady = 10)
    else:
        with open('links.conf') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 3):
                if lines[i+1]:
                    temp = lines[i+1]
                    time = 0
                    if "h" in temp:
                        temp = temp.split("h")
                        time = time + int(temp[0])*3600
                        temp = temp[-1]
                    if "m" in temp:
                        temp = temp.split("m")
                        time = time + int(temp[0])*60
                        temp = temp[-1]
                    if "s" in temp:
                        temp = temp.split("s")
                        time = time + int(temp[0])*1
                        temp = temp[-1]
                else:
                    time = lines[i+1].split("?t=")[-1]
                # print("python3 .\scripts\download.pyw " + str(i/3).split(".")[0] + "-" + str(time) + "-" + lines[i+2].replace(" ", "_").rstrip() + " " + lines[i])
                subprocess.Popen("python3 .\scripts\download.pyw " + str(i/3).split(".")[0] + "-" + str(time) + "-" + lines[i+2].replace(" ", "_").rstrip() + " " + lines[i], shell=False, stdout=None)
                # os.system("python3 .\scripts\download.pyw " + str(i/3).split(".")[0] + "_"  + lines[i+2].replace(" ", "_").rstrip() + "_" + str(time) + " " + lines[i])
            popupBonusWindow = Tk()
            popupBonusWindow.wm_title("Info")
            popupBonusWindow.iconbitmap("./scripts/mainIcon.ico")
            popupBonusWindow.attributes("-topmost", True)
            labelBonus = Label(popupBonusWindow, text="   Audio files download in backgorund   ")
            labelBonus.pack(pady = 10)
            B1 = Button(popupBonusWindow, text="Okay", command=popupBonusWindow.destroy)
            B1.pack(pady = 10)

L1 = Label(master, text="Setup")
L1.pack(pady = 10)
btn = Button(master, text ="Open Editor", command = openEditor)
btn.pack(pady = 10)
btn = Button(master, text ="Create Audio Files", command = downloadAudio)
btn.pack(pady = 10)
btn = Button(master, text ="Back", command = goBack)
btn.pack(pady = 10)
master.mainloop()
