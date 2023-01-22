from PIL import Image, ImageDraw

def toPixelArt(image):
    # Load image
    im = Image.open(image)

    # Resize image
    im = im.resize((100, 100))

    # Create a new image with a white background
    pixelated = Image.new('RGB', im.size, (255, 255, 255))

    # Get the pixel data from the original image
    pixels = im.load()

    # Loop through the columns and rows of the image
    for x in range(0, im.size[0], 5):
        for y in range(0, im.size[1], 5):
            # Get the pixel color at the current position
            pixel_color = pixels[x, y]

            # Draw a rectangle with the pixel color at the current position
            ImageDraw.Draw(pixelated).rectangle([(x, y), (x + 5, y + 5)], fill=pixel_color)

    # Save the pixelated image
    pixelated.save('pixelart.bmp')
