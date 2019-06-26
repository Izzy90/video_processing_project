import stabilization as st
import matting as mt
import tracking as tr
import utilities as ut
import trimap as tri
import winsound


def main(input_vid_path, background_image_path):

    # Each of the functions should:
    # 1. Perform the necessary actions
    # 2. Save the new output video
    # 3. return a path to it

    # 1 - stabilize the input vid
    # stabilized_vid = st.stabilize(input_vid_path)
    stabilized_vid = input_vid_path
    # exit(0)

    # 2 - subtract background from stabilized video
    print("Starting trimap")
    trimap_folder = tri.trimap(stabilized_vid)
    # trimap_folder = "trimap_frames"
    print("Done with trimap")

    # 3 - apply matting
    print("Starting matting")
    output_matted_vid = "matted_output_vid_4.avi"
    matted_vid = mt.add_background_image(trimap_folder, input_vid_path,
                                         output_matted_vid, background_image_path)
    print("Done with matting")

    # generate frames folder
    ut.save_video_frames(matted_vid, folder_name="matted_vid_4_frames")
    # exit(0)

    # 4 - apply tracking
    print("Starting tracking")
    output_vid = tr.track("matted_vid_4_frames")

    # 5 - generate the output video from the tracked frames
    ut.create_video_from_image_folder("tracked_images", "tracked_4.avi", shape=(555,416))
    print("Done tracking")

    return output_vid


if __name__ == "__main__":

    # print("starting")
    input_vid_path = "walking_input.avi"
    background_image_path = "background4.jpg"

    main(input_vid_path, background_image_path)

    winsound.Beep(1760, 1000)
