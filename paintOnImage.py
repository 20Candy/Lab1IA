import cv2

def paintOnImage(file, shortest_path):

    img = cv2.imread(file)

    height, width, _ = img.shape

    lila = (255, 0, 255)

    for x, y in shortest_path:
        # Paint each pixel of the path with the color lila
        img[y, x] = lila   

    cv2.imwrite("modified_image.bmp", img)
