import os

dir = "C:/Users/Biel/Downloads/"
mp4 = dir + "Lunatic.mp4"
mp3 = dir + "LUNATIC.mp3"
cmd = f"ffmpeg -i {mp4} -vn {mp3}"
cmd_youtube = "youtube-dl --extract-audio --audio-quality 0 --audio-format mp3 https://www.youtube.com/watch?v=yH01xqrynOE"
os.system(cmd_youtube)
#os.system(f"afplay {mp3}")
