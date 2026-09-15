import numpy as np

from modules.preprocessing import (
    resize_image,
    prepare_image
)


def test_resize_small_image():

    image = np.zeros(
        (100, 100, 3),
        dtype=np.uint8
    )

    result = resize_image(image)

    assert result.shape == (
        100,
        100,
        3
    )


def test_prepare_image():

    image = np.zeros(
        (50, 50, 3),
        dtype=np.uint8
    )

    result = prepare_image(image)

    assert result.dtype == np.float32
