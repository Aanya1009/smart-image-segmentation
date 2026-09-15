import numpy as np
import cv2


def create_mask(labels, cluster_number, image_shape):

    mask = (
        labels == cluster_number
    ).astype(np.uint8)

    mask = mask.reshape(
        image_shape[:2]
    )

    return mask


def extract_cluster(
    image,
    labels,
    cluster_number
):

    mask = create_mask(
        labels,
        cluster_number,
        image.shape
    )

    extracted = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    return extracted


def save_extracted_cluster(
    image,
    labels,
    cluster_number,
    output_path
):

    extracted = extract_cluster(
        image,
        labels,
        cluster_number
    )

    cv2.imwrite(
        output_path,
        extracted
    )

    return extracted
