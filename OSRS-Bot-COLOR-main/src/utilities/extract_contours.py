from typing import List
import cv2
import numpy as np
from utilities.geometry import Point, RuneLiteObject

def extract_contours(image: cv2.Mat) -> List[RuneLiteObject]:
    """
    This extracts the white in your image into a data structure.
    Args:
        image: The image to process.
    Returns:
        A list of RuneLiteObjects, or an empty list if no objects are found.
    """
    # Threshold the image to obtain a binary image
    thresholded_image = image
    # Find the contours
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    black_image = np.zeros(thresholded_image.shape, dtype="uint8")
    # Extract the objects from each contoured object
    objs: List[RuneLiteObject] = []
    for objects in range(len(contours)):
        if len(contours[objects]) > 0:
            # Fill in the outline with white pixels
            black_copy = black_image.copy()
            cv2.drawContours(black_copy, contours, objects, (255, 255, 255), -1)
            x, y, width, height = cv2.boundingRect(contours[objects])
            area = width * height
            if area <= 125*125:
                center = [int(x + (width / 2)), int(y + (height / 2))]
                axis = np.column_stack((y, x))
                objs.append(RuneLiteObject(x, x + width, y, y + height, width, height, center, axis))
            else:
                chunk_width = 50
                chunk_height = 50
                for i in range(0, height, chunk_height):
                    for j in range(0, width, chunk_width):
                        sub_image = thresholded_image[y + i:y + i + chunk_height, x + j:x + j + chunk_width]
                        if cv2.countNonZero(sub_image) > 0:
                            x_offset = x + j
                            y_offset = y + i
                            sub_width = min(chunk_width, width - j)
                            sub_height = min(chunk_height, height - i)
                            center = [int(x_offset + (sub_width / 2)), int(y_offset + (sub_height / 2))]
                            axis = np.column_stack((y_offset, x_offset))
                            objs.append(RuneLiteObject(x_offset, x_offset + sub_width, y_offset, y_offset + sub_height, sub_width, sub_height, center, axis))
    return objs or []
