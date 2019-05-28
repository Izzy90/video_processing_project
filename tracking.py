import cv2
from tracking_functions import *


def track(input_vid):

    return


ID1 = "123456789"
ID2 = "987654321"

ID = "HW3_{0}_{1}".format(ID1, ID2)
IMAGE_DIR_PATH = "./Images"

# SET NUMBER OF PARTICLES
N = 100

# Initial Settings
s_initial = [297,  # x center
             139,  # y center
             16,  # half width
             43,  # half height
             0,  # velocity x
             0]  # velocity y

# CREATE INITIAL PARTICLE MATRIX 'S' (SIZE 6xN)
S_temp = (s_initial) * np.ones((N, 1))
S = predict_particles(np.transpose(S_temp))

# LOAD FIRST IMAGE
# TODO: change this to read frames from video and not images
I = cv2.imread(IMAGE_DIR_PATH + os.sep + "001.png")

# COMPUTE NORMALIZED HISTOGRAM
q = comp_norm_hist(I, s_initial)

# COMPUTE NORMALIZED WEIGHTS (W) AND PREDICTOR CDFS (C)
W = np.zeros(shape=(N, 1))
C = np.zeros(shape=(N, 1))

for i in range(N):
    W[i] = comp_bat_dist(comp_norm_hist(I, S[:, i]), q)

W = W / np.sum(W)
C[0] = W[0]
for i in range(1, N):
    C[i] = C[i - 1] + W[i]

images_processed = 1

# MAIN TRACKING LOOP
image_name_list = os.listdir(IMAGE_DIR_PATH)
for image_name in image_name_list[1:]:

    S_prev = S

    # LOAD NEW IMAGE FRAME
    image_path = IMAGE_DIR_PATH + os.sep + image_name
    I = cv2.imread(image_path)

    # SAMPLE THE CURRENT PARTICLE FILTERS
    S_next_tag = sample_particles(S_prev, C)

    # PREDICT THE NEXT PARTICLE FILTERS (YOU MAY ADD NOISE
    S = predict_particles(S_next_tag)

    # COMPUTE NORMALIZED WEIGHTS (W) AND PREDICTOR CDFS (C)

    W = np.zeros(shape=(N, 1))
    C = np.zeros(shape=(N, 1))

    for k in range(N):
        W[k] = comp_bat_dist(comp_norm_hist(I, S[:, k]), q)

    W = W / np.sum(W)
    C[0] = W[0]
    for k in range(1, N):
        C[k] = C[k - 1] + W[k]

    # CREATE DETECTOR PLOTS
    images_processed += 1
    if 0 == images_processed % 10:
        show_particles(I, S, W, images_processed, ID)

comp_norm_hist(I, s_initial)
