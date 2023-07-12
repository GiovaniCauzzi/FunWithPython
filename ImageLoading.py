from PIL import Image


# Open the image file
image = Image.open('image.jpg')

# Get the pixel values
pixels = image.load()

# Get the size of the image
width, height = image.size

# Iterate over each pixel
for y in range(height):
    for x in range(width):
        # Get the RGB values of the pixel
        r, g, b = pixels[x, y]

        # Do something with the pixel values
        print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")

def freezeExecution():
    printPressEnter2Continue()
    return input()

def OpenImage(filePath):
    try:
        localimage = Image.open(filePath)
    except:
        print("Image loading error")
        freezeExecution()

    else:
        return localimage


    
