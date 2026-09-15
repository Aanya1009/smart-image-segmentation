import numpy as np

from modules.segmentation import (
    prepare_pixels,
    apply_kmeans,
    reconstruct_image
)


def test_prepare_pixels():

    image = np.zeros(
        (10, 10, 3),
        dtype=np.float32
    )

    pixels = prepare_pixels(image)

    assert pixels.shape == (
        100,
        3
    )


def test_kmeans():

    image = np.random.randint(
        0,
        255,
        (20, 20, 3)
    ).astype(np.float32)

    labels, centers = apply_kmeans(
        image,
        3
    )

    assert len(labels) == 400
    assert centers.shape == (
        3,
        3
    )


def test_reconstruct_image():

    image = np.zeros(
        (10, 10, 3),
        dtype=np.float32
    )

    labels, centers = apply_kmeans(
        image,
        2
    )

    result = reconstruct_image(
        labels,
        centers,
        image.shape
    )

    assert result.shape == (
        10,
        10,
        3
    )
