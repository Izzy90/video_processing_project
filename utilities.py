import cv2
import os


def take_video_frames(input_vid_path, folder_name="input_frames"):

    # create the images folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # start the video capture
    input_vid = cv2.VideoCapture(input_vid_path)
    frame_num = 1

    while input_vid.isOpened():
        ret, frame = input_vid.read()
        if ret:
            # save frame to frames folder
            cv2.imwrite(f"{folder_name}/frame_{frame_num}.jpg", frame)
            frame_num += 1
        else:
            break

    input_vid.release()
    cv2.destroyAllWindows()


def play_video(video_path):
    input_vid = cv2.VideoCapture(video_path)

    while input_vid.isOpened():
        ret, frame = input_vid.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    input_vid.release()
    cv2.destroyAllWindows()
