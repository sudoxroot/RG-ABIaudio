from __future__ import unicode_literals
import youtube_dl
import sys
from os.path import exists
from tkinter import *
from tkinter.ttk import *
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'/audio/{sys.argv[1]}.wav',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'prefer_ffmpeg': True,
    'keepvideo': True
}
if exists('./audio/' + sys.argv[1] + '.wav'):
    pop = Tk()
    pop.wm_title("ERROR")
    pop.iconbitmap("./scripts/error.ico")
    pop.attributes("-topmost", True)
    labelBonus = Label(pop, text="   Song allready exist:   ")
    labelBonus.pack(pady=10)
    labelBonus = Label(pop, text=f'   /audio/{sys.argv[1]}.wav   ')
    labelBonus.pack(pady=10)
    B1 = Button(pop, text="Okay", command=pop.destroy)
    B1.pack(pady=10)
else:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([sys.argv[2]])
    except:
        pop = Tk()
        pop.wm_title("ERROR")
        pop.iconbitmap("./scripts/error.ico")
        pop.attributes("-topmost", True)
        labelBonus = Label(pop, text="   There was an error downloading:   ")
        labelBonus.pack(pady=10)
        labelBonus = Label(pop, text=[sys.argv[2]])
        labelBonus.pack(pady=10)
        labelBonus = Label(pop, text="from")
        labelBonus.pack(pady=10)
        labelBonus = Label(pop, text=[sys.argv[1]])
        labelBonus.pack(pady=10)
        B1 = Button(pop, text="Okay", command=pop.destroy)
        B1.pack(pady=10)

mainloop()
