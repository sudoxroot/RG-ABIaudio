from tkinter import *
from tkinter.ttk import *
from sympy import re
import vlc
import os
import time
from os import walk

master = Tk()
master.geometry("800x600")
master.title("RG-ABI audio Playback")
master.iconbitmap("./scripts/mainIcon.ico")

selectedFile = ""
loadedFile = ""
loadedTime = ""
playingFile = ""
media_player = []

def playSound():
    global loadedFile, loadedTime, playingFile, media_player
    if(playingFile):
        playbtn.config(text = "Processing")
        lbll2tl.config(text = "Stopping: ")
        time.sleep(0.03)
        for i in range(0, 100):
            media_player.audio_set_volume(100-i)
            # fade out 3s
            time.sleep(0.03)
        playbtn.config(text = "Play")
        lbll2tl.config(text = "Loaded: ")
        media_player.stop()
        playingFile = ""

    elif(loadedFile):
        path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        media_player = vlc.MediaPlayer()
        media = vlc.Media(path + "/audio/" + loadedFile)
        media.add_option('start-time=' + loadedTime + '.0')
        media_player.set_media(media)
        media_player.audio_set_volume(0)
        time.sleep(0.01)
        media_player.play()
        for i in range(0, 100):
            media_player.audio_set_volume(i)
            # fade in 1s
            time.sleep(0.01)
            if(str(media_player.get_state()) == "State.Playing"):
                playbtn.config(text = "Pause")
                lbll2tl.config(text = "Playing: ")
                playingFile = loadedFile
            else:
                playingFile = ""

def loadSound():
    global selectedFile, loadedFile, loadedTime
    loadedFile = selectedFile
    loadedTime = selectedFile.split("-")[1]
    print(loadedTime)
    lbll.config(text = "Loaded: " + loadedFile)
    lbll2.config(text = loadedFile)
    time.sleep(0.01)
    lbll2t.delete(0, END)
    time.sleep(0.01)
    lbll2t.insert(0,loadedTime)
        
def timeUpdate(*args):
    global loadedTime
    item = var_lbll2t.get()
    print(item)
    if not item:
        item = loadedTime
    try:
        item_type = type(int(item))
        if item_type == type(int(1)):
            loadedTime = item
    except:
        lbll2t.delete(0, END)
        lbll2t.insert(0,loadedTime)
        
def textUpdate(*args):
    global selectedFile
    item = var_inputtxt.get()
    try:
        item_type = type(int(item))
        if item_type == type(int(1)):
            path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
            filenames = next(walk(path + "/audio/"), (None, None, []))[2]  # [] if no file
            try:
                file = [i for i in filenames if i.startswith(item)][0]
                lbls.config(text = file)
                selectedFile = file
            except:
                inputtxt.delete(0, END)
                try:
                    file = [i for i in filenames if i.startswith(item[-1])][0]
                    lbls.config(text = file)
                    inputtxt.insert(0,item[-1])
                    selectedFile = file
                except:
                    inputtxt.delete(0, END)
    except:
        inputtxt.delete(0, END)

    
            
var_inputtxt = StringVar()
var_lbll2t = StringVar()
L1 = Label(master, text="Selection")
L1.config(font=("Courier", 21))
L1.grid(column=0, row=0, sticky=NW, padx=5, pady=5)
label = Label(master, text ="Song Number:")
label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
inputtxt = Entry(master, width=20,  textvariable=var_inputtxt)
inputtxt.grid(column=1, row=1, sticky=W, padx=5, pady=5)
playbtn = Button(master, text ="Load", command = loadSound)
playbtn.grid(column=2, row=1, sticky=W, padx=5, pady=5)
lbls = Label(master, text = "")
lbls.grid(column=1, row=2, sticky=W)
lbll = Label(master, text = "")
lbll.grid(column=3, row=1, sticky=W, padx=5, pady=5)
L1 = Label(master, text="Play")
L1.config(font=("Courier", 21))
L1.grid(column=0, row=3, sticky=NW, padx=5, pady=5)
lbll2 = Label(master, text = "")
lbll2.grid(column=1, row=4, sticky=W, padx=5, pady=5)
lbll2tt = Label(master, text = "StartTime: ")
lbll2tt.grid(column=0, row=5, sticky=E, padx=5, pady=5)
lbll2tl = Label(master, text = "Loaded: ")
lbll2tl.grid(column=0, row=4, sticky=E, padx=5, pady=5)
lbll2t = Entry(master, width=20,  textvariable=var_lbll2t)
lbll2t.grid(column=1, row=5, sticky=W, padx=5, pady=5)
playbtn = Button(master, text ="Play", width=20, command = playSound)
playbtn.grid(column=1, row=6, sticky=W, padx=5, pady=5)


var_inputtxt.trace("w", textUpdate)
var_lbll2t.trace("w", timeUpdate)
# mainloop, runs infinitely
mainloop()
