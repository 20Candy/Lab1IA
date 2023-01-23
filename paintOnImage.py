from PIL import Image

def paintOnImage(file, shortest_path):


    image = Image.open(file)
    path_image = image.copy()
    pixels = path_image.load()

    path_color = (0,0,255)  # red

    for i, j in shortest_path:

        pixels[i, j] = path_color

    path_image.save("result.jpg")

