import cv2
import numpy as np

def main():
    foreground = cv2.VideoCapture('output.avi')
    background = cv2.imread('background2.jpg')
    alpha = cv2.VideoCapture('circle_alpha.mp4')

    while foreground.isOpened():
        fr_foreground = foreground.read()[1]/255
        fr_background = background/255
        fr_alpha = 0.75


        cv2.imshow('My Image',cmb(fr_foreground,fr_background,fr_alpha))

        if cv2.waitKey(1) == ord('q'): break

    cv2.destroyAllWindows

def cmb(fg,bg,a):
    return fg * a + bg * (1-a)

if __name__ == '__main__':
    main()