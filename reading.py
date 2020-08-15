from PIL import Image, ImageSequence
import numpy as np


def read_gif(filename):
    max_frames = 50
    im = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(im):
        #print(frame.size)
        resized_frame = np.array(frame.convert('RGB').resize((200,200)))
        frames.append(resized_frame)
    frames = frames*max_frames
    return np.asarray(frames[:max_frames])