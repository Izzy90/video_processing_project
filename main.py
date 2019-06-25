import stabilization as st
import background_subtraction as bs
import matting as mt
import tracking as tr
import utilities as ut


def main(input_vid_path, background_image_path):

    # Each of the functions should:
    # 1. Perform the necessary actions
    # 2. Save the new output video
    # 3. return a path to it

    # 1 - stabilize the input vid
    stabilized_vid = st.stabilize(input_vid_path)
    # stabilized_vid = input_vid_path
    # exit(0)

    # 2 - subtract background from stabilized video
    binary_mask_vid = bs.subtract_background(stabilized_vid)

    # 3 - apply matting
    matted_vid = mt.add_background_image(binary_mask_vid, background_image_path)
    matted_vid = "matted_output_vid_3.avi"

    # generate frames folder
    ut.save_video_frames(matted_vid, folder_name="matted_vid_3_frames")
    # exit(0)

    # 4 - apply tracking
    output_vid = tr.track("matted_vid_3_frames")

    # 5 - generate the output video from the tracked frames
    ut.create_video_from_image_folder("tracked_images", "tracked_3.avi")

    return output_vid


if __name__ == "__main__":

    print("starting")
    input_vid_path = "walking_input.avi"
    background_image_path = "background3.jpg"

    main(input_vid_path, background_image_path)
