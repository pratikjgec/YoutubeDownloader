from pytube import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

#oncomplete callback function

def completeDownload(stream=None,file_path=None):
    global file_loc
    print("Downlaod completed")
    file_loc='Video Downlaoded Successsful '+file_path;
    #print(file_path)
    showinfo('Massage', file_loc)
    dbutton['text']="Downlaod"
    dbutton['state']='active'
    urlField.delete(0, END);
    #file_loc= file_path
#onprogress callback function
def progressDownlaod(stream=None,chunk=None,bytes_remaining=None):
    percentage=((file_size-bytes_remaining)/file_size)*100
    dbutton['text']="{:00.0f} % downloaded".format(percentage)

#downlaod function
def download_video(url):
    global file_size

        #url = "https://www.youtube.com/watch?v=vzGxuaz7Iy8"
    path_save = askdirectory()
    if path_save is None:
        return

    try:
        ob = YouTube(url)
        strem = ob.streams.first()
        ob.register_on_complete_callback(completeDownload)
        ob.register_on_progress_callback(progressDownlaod)
          #  strem = ob.streams.filter(only_audio=True).all
        file_size=strem.filesize
        res = strem.download(output_path=path_save)

    except Exception as e:
        print(e)
        print("Somthing went wrong")
#button function
def btnclick():
    try:
        dbutton['text']="Please wait.."
        dbutton['state']='disabled'
        url=urlField.get()
        if url=='':
            return
        print(url)
        #download_video(url)
        thread=Thread(target=download_video,args=(url,))
        thread.start()
    except Exception as e:
        print(e)

def reset():
    dbutton['text'] = "Downlaod"
    dbutton['state'] = 'active'
    urlField.delete(0, END);


#UI coding
font="Helvetica"
main=Tk()
main.title("Youtube video Downlaoder")
main.iconbitmap('icon.ico')
main.geometry("360x350")
print('wondow came')
file=PhotoImage("icon.jpg")
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)
urlField=Entry(main,font=font,justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10,pady=10)
urlField.focus()
dbutton=Button(main,text="Downoad",font=font,relief='ridge',command=btnclick)
dbutton.pack(pady=10)
resetbutton=Button(main,text="Reset",font=font,relief='ridge',command=reset)
resetbutton.pack()

main.mainloop()



