import time
import numpy as np
import matplotlib.pyplot as plt

from torch import Tensor


def comparison_plot(prediction: Tensor, ground_truth: Tensor, params: dict = {}):
    prediction = np.reshape(
        prediction, (params["data"]["grid"], params["data"]["grid"])
    )
    ground_truth = np.reshape(
        ground_truth, (params["data"]["grid"], params["data"]["grid"])
    )

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 3))
    axes[0].imshow(
        ground_truth,
        cmap="jet",
        aspect="auto",
        extent=params["data"]["extent"],
        origin="lower",
    )
    axes[0].set_title(params["title"]["ground_truth"])
    axes[1].imshow(
        prediction,
        cmap="jet",
        aspect="auto",
        extent=params["data"]["extent"],
        origin="lower",
    )
    axes[1].set_title(params["title"]["prediction"])

    fig.tight_layout()
    if "savefig_path" in params:
        plt.savefig(params["savefig_path"])

    return fig, axes


if __name__ == "__main__":
    output_random = np.random.rand((2500))
    comparison_plot(
        prediction=output_random,
        ground_truth=output_random,
        params={
            "title": {
                "ground_truth": "Analytical PDE Solution",
                "prediction": "Neural Network PDE Solution",
            },
            "data": {
                "grid": 50,
                "extent": [0, 1, 0, 2 * np.pi],
            },
            "savefig_path": f"./results_{time.time()}.png",
        },
    )
