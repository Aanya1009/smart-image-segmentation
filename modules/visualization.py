import cv2
import matplotlib.pyplot as plt


def save_image(image, output_path):

    success = cv2.imwrite(
        output_path,
        image
    )

    if not success:
        raise IOError(
            "Unable to save image: "
            + output_path
        )


def save_elbow_plot(
    k_values,
    inertias,
    output_path
):

    plt.figure(figsize=(8, 5))

    plt.plot(
        list(k_values),
        inertias,
        marker="o"
    )

    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for K-Means")

    plt.grid(True)

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
