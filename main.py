import stabilization as st
import background_subtraction as bs
import matting as mt
import tracking as tr
import utilities as ut


def main(input_vid_path, background_image_path):

    # 1 - stabilize the input vid
    stabilized_vid = st.stabilize(input_vid_path)

    # 2 - subtract background from stabilized video
    binary_mask_vid = bs.subtract_background(stabilized_vid)

    # 3 - apply matting
    matted_vid = mt.matt(stabilized_vid, binary_mask_vid, background_image_path)

    # 4 - apply tracking
    output_vid = tr.track(matted_vid)

    return output_vid


if __name__ == "__main__":

    input_vid_path = "INPUT.avi"
    background_image_path = "background.jpg"

    main(input_vid_path, background_image_path)
