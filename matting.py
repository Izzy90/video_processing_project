import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_background_image(input_vid_path, background_image_path):
    im_shape = (720, 1280, 3)
    output_path = "matted_output_vid.avi"
    cap = cv2.VideoCapture(input_vid_path)
    bg_image = cv2.imread(background_image_path)
    bg_image = cv2.resize(bg_image, dsize=(1280, 720), interpolation=cv2.INTER_CUBIC)

    # plt.imshow(bg_image)
    # plt.show()

    fouorcc = cv2.VideoWriter_fourcc(*"MJPG")

    ret, frame = cap.read()
    vid_writer = cv2.VideoWriter(output_path, fouorcc, 30, (frame.shape[1], frame.shape[0]))

    while cap.isOpened():  # play the video by reading frame by frame
        ret, frame = cap.read()
        if (ret == True):

            # initialize new image to be written
            out_frame = np.zeros(im_shape, dtype=np.uint8)

            # iterate over all pixels
            for row in range(out_frame.shape[0]):
                for col in range(out_frame.shape[1]):
                    if frame[row,col].max() < 5:
                        out_frame[row,col] = bg_image[row,col]
                    else:
                        out_frame[row,col] = frame[row,col]
                    # print("d")
            #     check if binary mask value is 0, if it is take the value from the background image,
            #     otherwise from the frame

            # cv2.imshow('BGSUB', out_frame)
            # plt.imshow(out_frame)
            # plt.show()
            vid_writer.write(out_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
                break
        else:
            break

    vid_writer.release()
    cap.release()
    cv2.destroyAllWindows()

    return output_path

def cmb(fg,bg,a):
    return fg * a + bg * (1-a)

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

if __name__ == '__main__':
    main()