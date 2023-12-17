from moviepy.editor import *


def text_to_video(text, size):
    bg_clip = ColorClip(size, color=(100, 100, 100)).set_duration(3)
    text_clip = TextClip(text, size=(None, size[1]), color="white").set_duration(3)
    video = CompositeVideoClip([
        bg_clip,
        text_clip.set_position(lambda t: (size[0] / 2 - (text_clip.size[0]) * (t / 3), "center"))
    ])
    video.write_videofile("static/video/result.mp4", fps=24)