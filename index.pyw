import os
import tkinter as tk
# master.title("RG-ABI audio")
# master.iconbitmap("mainIcon.ico")

# def openPlayback():
#     exec(open('playback.py').read())
#     master.destroy()

# def openSetup():
#     exec(open('setup.py').read())
#     master.destroy()


# label.pack(pady = 10)

# # a button widget which will open a
# # new window on button click
# btn = Button(master, text ="Launch Playback", command = openPlayback)
# btn.pack(pady = 10)
# btn = Button(master, text ="Open Setup", command = openSetup)
# btn.pack(pady = 10)

# # mainloop, runs infinitely
# mainloop()


class MainPage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RG-ABI audio")
        self.root.iconbitmap("./scripts/mainIcon.ico")
        self.root.geometry("300x200")
        label = tk.Label(self.root, text="RückertGymnasium ABI Audio", fg="blue")
        label.pack(pady=10)

        btn = tk.Button(self.root, text="Open Playback", command=self.openPlayback)
        btn.pack(pady=10)
        btn = tk.Button(self.root, text="Open Setup", command=self.openSetup)
        btn.pack(pady=10)
        btn = tk.Button(self.root, text="Close App", command=self.root.destroy)
        btn.pack(pady=10)

        self.root.mainloop()

    def openPlayback(self):
        self.root.destroy()
        os.system("python3 .\scripts\playback.pyw")

    def openSetup(self):
        self.root.destroy()
        os.system("python3 .\scripts\setup.pyw")

MP=MainPage()