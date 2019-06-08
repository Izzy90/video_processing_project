import cv2
import numpy as np



def trimap(video_input):

    #background = cv2.imread(background)
    cap = cv2.VideoCapture(video_input)


    while cap.isOpened(): # play the video by reading frame by frame
        ret, frame = cap.read()

        if (ret == True):
            frame1=frame
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(image, 145, 255, cv2.THRESH_BINARY_INV)
            kernel1 = np.ones((2, 2), np.uint8)
            erosion = cv2.erode(thresh, kernel1, iterations=1)
            #cv2.imshow("AfterErosion", erosion)

            kernel2 = np.ones((1, 1), np.uint8)
            dilation = cv2.dilate(erosion, kernel2, iterations=2)
            #cv2.imshow("AfterDilation", dilation)

            contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            #sort contours
            sorted_ctrs = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

            mask = np.zeros_like(frame1)  # Create mask where white is what we want, black otherwise
            cv2.drawContours(mask, sorted_ctrs, 0, (255, 255, 255), -1)  # Draw filled contour in mask
            out = np.zeros_like(frame1)  # Extract out the object and place into output image
            out[mask == 255] = [255]

            #Show the output image
            #cv2.imshow('Output', out)

            image1 = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

            # noise removal
            kernel = np.ones((5, 5), np.uint8)
            opening = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel, iterations=1)

            # sure background area
            sure_bg = cv2.dilate(opening, kernel, iterations=1)

            # Finding sure foreground area
            sure_fg = cv2.erode(opening, kernel, iterations=1)
            cv2.imshow("foreground", sure_fg)

            # Finding unknown region
            sure_fg = np.uint8(sure_fg)
            unknown = cv2.subtract(sure_bg, sure_fg)
            ret, thresh = cv2.threshold(unknown, 240, 255, cv2.THRESH_BINARY)

            unknown[thresh == 255] = 127

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

            #cv2.imshow("unknown", unknown)

            final_mask = sure_fg + unknown
            cv2.imshow("final_mask", final_mask)




            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
                break
        else:
            break
            if cv2.waitKey(1) == ord('q'): break

    cap.release()
    cv2.destroyAllWindows






#test
trimap('walking.avi')
