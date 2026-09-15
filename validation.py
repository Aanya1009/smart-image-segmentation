import os


def validate_image(image_path):

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            "Image file does not exist: " + image_path
        )

    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png"
    ]

    extension = os.path.splitext(image_path)[1].lower()

    if extension not in allowed_extensions:
        raise ValueError(
            "Unsupported image format. "
            "Use JPG, JPEG, or PNG."
        )

    return True


def validate_k(k):

    if k < 2:
        raise ValueError(
            "K must be at least 2."
        )

    if k > 20:
        raise ValueError(
            "K should not be greater than 20."
        )

    return True


def validate_path(path):

    if not os.path.exists(path):
        raise FileNotFoundError(
            "Path does not exist: " + path
        )

    return True
