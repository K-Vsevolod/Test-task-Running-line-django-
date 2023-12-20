from moviepy.editor import *
import math


def text_to_video(text, size):
    duration = 3

    bg_clip = ColorClip(size, color=(100, 100, 100)).set_duration(duration)
    text_clip = TextClip(text, size=(None, size[1]), color="white").set_duration(duration)

    video = CompositeVideoClip([
        bg_clip,
        text_clip.set_position(lambda t: (size[0] / 2 - (text_clip.size[0]) * (t / duration), "center"))
    ])

    fps = math.ceil(len(text) / 2) + 1

    video.write_videofile("result/result.mp4", fps=max(24, fps))
