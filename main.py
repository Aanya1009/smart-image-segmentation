import argparse
import os
import time

from validation import validate_image, validate_k
from modules.preprocessing import load_image, resize_image, prepare_image
from modules.segmentation import apply_kmeans, reconstruct_image
from modules.analysis import elbow_analysis
from modules.extraction import extract_cluster
from modules.visualization import save_image, save_elbow_plot


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Smart Image Segmentation using K-Means Clustering"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input image"
    )

    parser.add_argument(
        "--k",
        type=int,
        default=3,
        help="Number of clusters"
    )

    parser.add_argument(
        "--elbow",
        action="store_true",
        help="Perform Elbow Method analysis"
    )

    return parser.parse_args()


def run_segmentation(image_path, k):

    validate_image(image_path)
    validate_k(k)

    print("\nLoading image...")
    image = load_image(image_path)

    print("Preprocessing image...")
    image = resize_image(image)
    image = prepare_image(image)

    print("Preparing pixels...")

    start_time = time.time()

    print("Running K-Means clustering...")
    labels, centers = apply_kmeans(image, k)

    segmented_image = reconstruct_image(
        labels,
        centers,
        image.shape
    )

    processing_time = time.time() - start_time

    output_directory = "results/segmented"

    os.makedirs(output_directory, exist_ok=True)

    output_path = os.path.join(
        output_directory,
        "segmented_image.jpg"
    )

    save_image(segmented_image, output_path)

    print("\nSegmentation completed successfully!")
    print("Clusters:", k)
    print("Processing Time: {:.2f} seconds".format(processing_time))
    print("Output:", output_path)

    return image, labels, centers


def main():

    args = parse_arguments()

    image, labels, centers = run_segmentation(
        args.input,
        args.k
    )

    if args.elbow:

        print("\nRunning Elbow Method...")

        k_values = range(2, 9)

        inertias = elbow_analysis(
            image,
            k_values
        )

        plot_path = "results/analysis/elbow_plot.png"

        os.makedirs("results/analysis", exist_ok=True)

        save_elbow_plot(
            k_values,
            inertias,
            plot_path
        )

        print("Elbow graph saved to:", plot_path)

    print("\nProject execution completed.")


if __name__ == "__main__":
    main()
