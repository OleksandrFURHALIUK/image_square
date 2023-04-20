from PIL import Image, ImageOps


def calculate_bad_image(image: Image) -> list:
    width, height = image.size
    pixel_map = []
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            try:
                condition = (r / g) > 1 and (r / b) > 3 and (g / b) > 2  # R/G>1 and R/B>3 and G/B>2
            except ZeroDivisionError:
                condition = False

            if condition:
                pixel_map.append((i, j, True))
            else:
                pixel_map.append((i, j, False))

    return pixel_map


def get_pixel_count(pixel_map) -> int:
    return len(list(filter(lambda p: p[2], pixel_map)))


def calculate_good_image(image: Image) -> list:
    width, height = image.size
    pixel_map = []

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]

            try:
                condition_1 = (r / g) < 1 and (r / b) < 3.7 and (g / b) < 4
            except ZeroDivisionError:
                condition_1 = True
            try:
                condition_2 = (r / g) < 1.02 and (r / b) < 1.7 and (g / b) < 1.7
            except ZeroDivisionError:
                condition_2 = True
            try:
                condition_3 = (r / g) > 1 and (r / b) < 1.7 and (g / b) < 1.7
            except ZeroDivisionError:
                condition_3 = True

            if condition_1 or condition_2 and condition_3:
                pixel_map.append((i, j, True))
            else:
                pixel_map.append((i, j, False))
    return pixel_map


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
    image = input_image.convert('RGB')
    good_pixels = calculate_good_image(image)
    bad_pixels = calculate_bad_image(image)
    good_pixels_count = get_pixel_count(good_pixels)
    bad_pixels_count = get_pixel_count(bad_pixels)

    generate_image(good_pixels, image.width, image.height, 'good_image.bmp')
    generate_image(bad_pixels, image.width, image.height, 'bad_image.bmp')
    print('Кількість не вражених пікселів:', good_pixels_count)
    print('Кількість вражених пікселів:', bad_pixels_count)
    print(f'Уражена площа {(bad_pixels_count / good_pixels_count) * 100}')

    print()


if __name__ == "__main__":
    main()
