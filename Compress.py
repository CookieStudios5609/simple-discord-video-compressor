import subprocess




def ffmpeg_check():
    try:
        subprocess.Popen(["ffmpeg"])
    except FileNotFoundError:
        print("Looks like you don't have ffmpeg! Make sure its installed and in your PATH.")



ffmpeg_check()


