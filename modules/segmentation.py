import cv2
import numpy as np
from sklearn.cluster import KMeans


def prepare_pixels(image):

    height, width, channels = image.shape

    pixels = image.reshape(
        (-1, channels)
    )

    return pixels


def apply_kmeans(image, k):

    pixels = prepare_pixels(image)

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(pixels)

    centers = model.cluster_centers_

    return labels, centers


def reconstruct_image(labels, centers, image_shape):

    segmented_pixels = centers[
        labels
    ]

    segmented_image = segmented_pixels.reshape(
        image_shape
    )

    segmented_image = np.clip(
        segmented_image,
        0,
        255
    ).astype(np.uint8)

    return segmented_image
