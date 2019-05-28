import stabilization as st
import background_subtraction as bs
import matting as mt
import tracking as tr


def main(input_vid, background_image):
    # stabilize the input vid
    stabilized_vid = st.stabilize(input_vid)

    # subtract background from stabilized video
    binary_mask_vid = bs.subtract_background(stabilized_vid)

    # apply matting
    matted_vid = mt.matt(stabilized_vid, binary_mask_vid, background_image)

    # apply tracking
    output_vid = tr.track(matted_vid)

    return output_vid


if __name__ == "__main__":

    input_vid = "INPUT.avi"
    background_image = "background.jpg"

    main(input_vid, background_image)