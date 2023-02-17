import numpy as np
import cv2


def detect_color(image, color):
   
    # Convert the image from BGR to HSV color space
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_ranges = {
        "orange": (np.array([0, 147, 136]), np.array([36, 209, 255])), #door orange
        "red": (np.array([180, 100, 78]), np.array([10, 255, 255])), #path red
        "cyan": (np.array([77, 236, 136]), np.array([104, 255, 255])),#default marker cyan
        "green": (np.array([35, 50, 50]), np.array([70, 255, 255])),
        "red1": (np.array([180, 255, 255]),np.array([159, 50, 70])),
        "red2": (np.array([9, 255, 255]), np.array([0, 50, 70])),
        "green": (np.array([89, 255, 255]), np.array([36, 50, 70])),
        "blue": (np.array([128, 255, 255]), np.array([90, 50, 70])),
        "yellow": (np.array([35, 255, 255]), np.array([25, 50, 70])),
        "purple": (np.array([158, 255, 255]), np.array([129, 50, 70])),
        "orange2": (np.array([24, 255, 255]), np.array([10, 50, 70])),
        "gray": (np.array([180, 18, 230]), np.array([0, 0, 40]))
        # Add more color ranges here as needed
    }

    # Get the color range to use based on the input argument
    lower, upper = color_ranges.get(color, (None, None))

    # If the specified color is not found in the color_ranges dictionary, return an error message
    if lower is None or upper is None:
        return "Error: Invalid color specified"

    # Create a mask that only includes pixels within the specified color range
    mask = cv2.inRange(image, lower, upper)

    # Apply the mask to the original image, keeping only the specified color pixels and setting the rest to black
    result = cv2.bitwise_and(image, image, mask=mask)

    # Convert result to grayscale
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Threshold the result to black and white
    _, result = cv2.threshold(result, 50, 255, cv2.THRESH_BINARY)

    # Find the contours
    contours, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a black image
    black_image = np.zeros(result.shape, dtype="uint8")

    # Fill the contours with white pixels
    for c in contours:
        if cv2.contourArea(c) < 25:
            cv2.drawContours(black_image, [c], 0, (0, 0, 0), -1)
        else:
            cv2.drawContours(black_image, [c], 0, (255, 255, 255), -1)


    _, black_image = cv2.threshold(black_image, 0, 255, cv2.THRESH_BINARY)
    #use this for trouble shooting
    #cv2.imwrite("orange better detection.png",black_image)
     
    return black_image
