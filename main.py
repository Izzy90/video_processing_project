import stabilization as st
import background_subtraction as bs
import matting as mt
import tracking as tr
import utilities as ut


def main(input_vid_path, background_image_path):

    # 1 - stabilize the input vid
    # stabilized_vid = st.stabilize(input_vid_path)
    stabilized_vid = input_vid_path

    # 2 - subtract background from stabilized video
    binary_mask_vid = bs.subtract_background(stabilized_vid)

    # 3 - apply matting
    matted_vid = mt.add_background_image(binary_mask_vid, background_image_path)

    # generate frames folder
    ut.save_video_frames(matted_vid, folder_name="matted_vid_frames")

    # 4 - apply tracking
    output_vid = tr.track("matted_vid_frames")

    # 5 - generate the output video from the tracked frames

    return output_vid


if __name__ == "__main__":

    print("starting")
    input_vid_path = "walking_input.avi"
    background_image_path = "background2.jpg"

    main(input_vid_path, background_image_path)
