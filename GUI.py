from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess


def browse_input():
    browse_input.video_file = filedialog.askopenfilename(initialdir="/", title="Select a video file")
    input_label.configure(text="Input Video: "+browse_input.video_file)
    ffmpeg_check()


def save_as():
    save_as.save_location = filedialog.asksaveasfilename(initialdir="/", title="Where should this file be saved?")
    output_label.configure(text="Output Video: "+save_as.save_location)


def ffmpeg_check():
    try:
        subprocess.Popen(["ffmpeg"])
        ffmpeg_check_label.configure(text="FFMpeg found successfully.", fg='green', bg='#2c2f33')
    except FileNotFoundError:
        messagebox.showerror("FFMPEG check Failed!", "Looks like you don't have ffmpeg! Make sure its installed and in your PATH, then reopen this program.")
        ffmpeg_check_label.configure(text="FFMpeg not found.", fg='red', bg='#2c2f33')


def compress_start():
    confirm = messagebox.askyesno("FFMPEG found successfully.", "Note that compression speed is dependant on your specs and may take upwards of a minute for longer videos. This script does not notify you when compression is complete. Would you like to continue?")
    if confirm is True:
        compressor()
    else:
        Convert_Compress_Window.destroy()


def compressor():
    subprocess.Popen(["ffmpeg", "-i", f"{browse_input.video_file}", "-vcodec", "libx264", "-crf", f"{int(quality.get())}", f"{save_as.save_location}"])


# bg='#2c2f33', fg="#d3d3d3" for labels, bg='#696969', fg="#d3d3d3" for entries
Convert_Compress_Window = Tk()
Convert_Compress_Window.resizable(False, False)
Convert_Compress_Window.title("Simple Video Compressor")
Convert_Compress_Window.configure(bg='#2c2f33')

# title
title_frame = Frame(Convert_Compress_Window)
title_label = Label(title_frame, text="Compress videos for Discord embeds", anchor=CENTER, width=40, bg='#2c2f33', fg="#d3d3d3")


# input
input_frame = Frame(Convert_Compress_Window)
input_label = Label(input_frame, text="Input file:", justify=LEFT, bg='#2c2f33', fg="#d3d3d3")
# input_entry = Entry(width=30, bg='#696969', fg="#d3d3d3")
input_video_btn = Button(master=Convert_Compress_Window, text="Browse", bg='#99aab5', command=browse_input)

# output
output_frame = Frame(Convert_Compress_Window)
output_label = Label(output_frame, text="Output file:", justify=LEFT, bg='#2c2f33', fg="#d3d3d3")
output_video_btn = Button(master=Convert_Compress_Window, text="Browse", bg='#99aab5', command=save_as)
ffmpeg_check_label = Label(Convert_Compress_Window, bg='#2c2f33')

# convert
convert_btn = Button(master=Convert_Compress_Window, text='Convert', bg='#2c2f33', fg='#02AC1E', command=compress_start)

# options
quality = IntVar()
slider = Scale(master=Convert_Compress_Window, from_=1, to=50, bg='#2c2f33', fg="#d3d3d3", highlightcolor='#99aab5', troughcolor="black", variable=quality)
slider.configure(bg='#2c2f33')
quality_description = Label(master=Convert_Compress_Window, text='1 = lossless, 50 = lowest quality, 28 recommended', bg='#2c2f33', fg="#d3d3d3")

# grid nonsense
title_frame.grid(row=0, column=0)
title_label.grid(row=0, column=1)
input_frame.grid(row=1, column=0)
input_label.grid(row=1, column=0)
input_video_btn.grid(row=1, column=1, padx=1)
# input_entry.grid(row=1, column=1)
output_frame.grid(row=2, column=0)
output_label.grid(row=2, column=0)
output_video_btn.grid(row=2, column=1, padx=1)
ffmpeg_check_label.grid(row=3, column=0)
slider.grid(row=4, column=0, sticky="w")
convert_btn.grid(row=5, column=1)
quality_description.grid(row=5, column=0, sticky='w')


# goes at end because the docs said so
Convert_Compress_Window.mainloop()
