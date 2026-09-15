import cv2


def load_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to load the image."
        )

    return image


def resize_image(image, max_width=800, max_height=800):

    height, width = image.shape[:2]

    if width <= max_width and height <= max_height:
        return image

    scale_width = max_width / width
    scale_height = max_height / height

    scale = min(
        scale_width,
        scale_height
    )

    new_width = int(width * scale)
    new_height = int(height * scale)

    resized = cv2.resize(
        image,
        (new_width, new_height)
    )

    return resized


def prepare_image(image):

    return image.astype("float32")
