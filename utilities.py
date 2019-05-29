import cv2
import os

# this is a comment

def save_video_frames(input_vid_path, folder_name="input_frames"):

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


# takes in an input video and saves an output video after processing
def write_video(input_vid_path, output_vid_path, processing_function):
    # TODO - change imgSize as necessary
    imgSize = (640, 360)
    frame_per_second = 30.0
    writer = cv2.VideoWriter(output_vid_path, cv2.VideoWriter_fourcc(*"MJPG"), frame_per_second, imgSize)

    cap = cv2.VideoCapture(input_vid_path)  # load the video
    while cap.isOpened():  # play the video by reading frame by frame
        ret, frame = cap.read()
        if ret == True:
            # image processing here
            # Our operations on the frame come here
            out_frame = processing_function(frame)
            writer.write(out_frame)  # save the frame into video file

            cv2.imshow('out_frame', out_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
                break
        else:
            break
    cap.release()
    writer.release()
    cv2.destroyAllWindows()
