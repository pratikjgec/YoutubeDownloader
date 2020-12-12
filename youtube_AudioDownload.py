from pytube import *
from tkinter.filedialog import *
from PIL import Image

url = "https://www.youtube.com/watch?v=-V_M0gqTD7A"
path_save = askdirectory()


try:
    ob = YouTube(url)
    strem = ob.streams.first()
    #  strem = ob.streams.filter(only_audio=True).all
    file_size = strem.filesize
    res = strem.download(output_path=path_save)
    showinfo('Massage', 'Video Downlaoded Successsful.')
except Exception as e:
    print(e)

