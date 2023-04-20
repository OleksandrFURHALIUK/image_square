from PIL import Image, ImageOps

def get_pixel_count(pixel_map) -> int:
    return len(list(filter(lambda p: p[2], pixel_map)))


def generate_image(pixel_map: list, width, height, image_name):
    image = Image.new('RGB', (width, height), "white")
    for i in pixel_map:
        if i[2]:
            image.putpixel((i[0], i[1]), (0, 0, 0))
        else:
            image.putpixel((i[0], i[1]), (255, 255, 255))
    image.show()
    image.save(image_name, 'bmp')


def main():
    input_image = Image.open("image.jpg")
    # image = im.convert("RGB")
    input_image.save("result.bmp", 'bmp')

    image = Image.open('result.bmp')
    for pixel in image.getdata():
        print(pixel)
    print()


if __name__ == "__main__":
    main()


