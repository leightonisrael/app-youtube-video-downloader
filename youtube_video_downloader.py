import tkinter
import customtkinter
from pytube import YouTube
from tkinter.font import Font

def downloadVideo():
    url = customtkinter.CTkEntry.get(videoURL)
    exit_dir = customtkinter.CTkEntry.get(exitPath)
    video = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path = exit_dir)


app = tkinter.Tk()
app.title("Youtube Video Downloader")
app.geometry("690x190")
app.resizable(width = False ,height = False)
app.configure(bg='#101010')



title = customtkinter.CTkLabel(
    master=app,
    text="Youtube Video Download",
    text_color="white",
    width= 650,
    font=("Helvetica", 45),
)

videoURL = customtkinter.CTkEntry(
    master=app,
    placeholder_text='Coloque a URL do vídeo aqui',
    width= 600,
    height=35,
)
exitPath = customtkinter.CTkEntry(
    master=app,
    placeholder_text='Local destino do arquivo',
    width= 345,
    height=35,
)

downloadButton = customtkinter.CTkButton(
    master=app,
    command=downloadVideo,
    text="Download",
    text_color="white",
    hover= True,
    hover_color= "black",
    height=35,
    width= 240,
    border_width=2,
    corner_radius=4,
    border_color= "#5d6266", 
    bg_color="#353535",
    fg_color= "#353535",
    font=("Roboto", 20)
)



title.place(x= 22, y= 15)
videoURL.place(x= 43, y= 80)
exitPath.place(x= 43, y= 125)
downloadButton.place(x= 405, y= 125)



app.mainloop()