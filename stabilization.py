import cv2
from stabilization_functions import *


def stabilize(input_vid):

    # ########################################### PART 2: Video Stabilization ##############################################

    # Choose parameters
    WindowSize = 30  # Add your value here!
    MaxIter = 2  # Add your value here!
    NumLevels = 4  # Add your value here!
    NumOfFrames = 80

    # Stabilize video
    StabilizedVid = lucas_kanade_video_stabilization(input_vid, WindowSize, MaxIter, NumLevels, NumOfFrames)

    # Save stabilized video
    # TODO

    return StabilizedVid
