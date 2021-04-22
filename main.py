import tkinter as tk

from pytube import YouTube


root = tk.Tk()
root.title("YouTube Video Downloader")


def getTextInput():
    result = textExample.get(1.0, tk.END + "-1c")

    yt = YouTube(result)
    my_video = yt.streams.get_highest_resolution()
    my_video.download()


textExample = tk.Text(root, height=1)
textExample.pack()
btnRead = tk.Button(root, height=1, width=15, text="Download Starten",
                    command=getTextInput)
btnRead.pack()
root.mainloop()
