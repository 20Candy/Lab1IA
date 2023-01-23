from PIL import Image, ImageDraw

def toPixelArt(image):

    im = Image.open(image)
    im = im.resize((100, 100))

    pixelated = Image.new('RGB', im.size, (255, 255, 255))
    pixels = im.load()

    for x in range(0, im.size[0], 5):
        for y in range(0, im.size[1], 5):
            pixel_color = pixels[x, y]

            ImageDraw.Draw(pixelated).rectangle([(x, y), (x + 5, y + 5)], fill=pixel_color)

    pixelated.save('pixelart.bmp')
