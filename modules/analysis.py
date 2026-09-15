from sklearn.cluster import KMeans

from modules.segmentation import prepare_pixels


def calculate_inertia(image, k):

    pixels = prepare_pixels(image)

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(pixels)

    return model.inertia_


def elbow_analysis(image, k_values):

    inertias = []

    for k in k_values:

        print(
            "Testing K = {}".format(k)
        )

        inertia = calculate_inertia(
            image,
            k
        )

        inertias.append(inertia)

    return inertias


def compare_k_values(image, k_values):

    results = {}

    for k in k_values:

        inertia = calculate_inertia(
            image,
            k
        )

        results[k] = inertia

    return results
