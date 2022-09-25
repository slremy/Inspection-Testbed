import cv2
from PIL import ImageGrab
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox

while True:
    image_pil = ImageGrab.grab(bbox= (800, 0, 3360, 1100)).convert('RGB').resize((400,400))
    image = np.array(np.flip(image_pil, axis=2), dtype = 'uint8').reshape((image_pil.size[1], image_pil.size[0], 3))
    box, label, count = cv.detect_common_objects(image)
    output = draw_bbox(image, box, label, count)
    print(label)
    print("Number of clocks in this image are " +str(label.count('clock')))
    cv2.imshow('output',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break