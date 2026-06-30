import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm



# The 'os' module will help to get the list of all header image files
folderPath = "Header_Images"
myList = os.listdir(folderPath)



overlayImageList = []



for imagePath in myList:

    image = cv2.imread(f'{folderPath}/{imagePath}')
    overlayImageList.append(image)


header = overlayImageList[0]


selected_color = (0, 255, 0)


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)


detector = htm.HandDetector(detectionCon=0.8)


brushThickness = 15


eraserThickness = 50


x_previous, y_previous = 0, 0


drawing_started = False


# Creating a canvas for drawing using numpy
drawing_canvas = np.zeros((720, 1280, 3), np.uint8)




while True:

    # Import the images
    success, img = cap.read()


    img = cv2.flip(img, 1)


    # Find the hand landmarks
    img = detector.findHands(img)

    lmList = detector.findPosition(img)


    if len(lmList) != 0:


        fingers = []

        # Finding the tip of index and middle finger
        x_index , y_index = lmList[8][1:]
        x_middle, y_middle = lmList[12][1:]


        # Checking which fingers are up
        fingers = detector.fingersUp()


        # Check if the fingers are in selection mode or drawing mode
        if fingers[1] and fingers[2]:


            x_previous, y_previous = 0, 0
            drawing_started = False


            if y_index < 125:
                if 250 < x_index < 450:
                    header = overlayImageList[0]
                    selected_color = (0, 255, 0)

                elif 550 < x_index < 750:
                    header = overlayImageList[1]
                    selected_color = (255, 0, 255)

                elif 800 < x_index < 950:
                    header = overlayImageList[2]
                    selected_color = (0, 255, 255)

                elif 1050 < x_index < 1200:
                    header = overlayImageList[3]
                    selected_color = (0, 0, 0)

            
            cv2.rectangle(
                img,
                (x_index, y_index-30),
                (x_middle, y_middle+30),
                selected_color,
                cv2.FILLED
            )


        if fingers[1] and not fingers[2]:


            cv2.circle(
                img,
                (x_index, y_index),
                15,
                selected_color,
                cv2.FILLED
            )


            # Start a new stroke when entering drawing mode
            if not drawing_started:

                x_previous, y_previous = x_index, y_index
                drawing_started = True

            else:

                if selected_color == (0, 0, 0):

                    cv2.line(
                    img,
                    (x_previous, y_previous),
                    (x_index, y_index),
                    selected_color,
                    eraserThickness
                )
                    
                    cv2.line(
                    drawing_canvas,
                    (x_previous, y_previous),
                    (x_index, y_index),
                    selected_color,
                    eraserThickness
                )
                    
                else:

                    cv2.line(
                    img,
                    (x_previous, y_previous),
                    (x_index, y_index),
                    selected_color,
                    brushThickness
                )

                cv2.line(
                    drawing_canvas,
                    (x_previous, y_previous),
                    (x_index, y_index),
                    selected_color,
                    brushThickness
                )

            x_previous, y_previous = x_index, y_index

    gray_image = cv2.cvtColor(drawing_canvas, cv2.COLOR_BGR2GRAY)



    # Creating into an binary image and inversing the image
    _, inverse_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV)



    inverse_image = cv2.cvtColor(inverse_image, cv2.COLOR_GRAY2BGR)



    img = cv2.bitwise_and(img, inverse_image)
    img = cv2.bitwise_or(img, drawing_canvas)



    # Overlaying the header image
    img[0:125, 0:1280] = header



    cv2.imshow("Virtual Painter", img)



    if cv2.waitKey(1) == ord('s'):
        break


cap.release()


cv2.destroyAllWindows()
