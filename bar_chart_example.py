"""
Bar Chart Example

This script creates a simple bar chart showing sample values.
"""

import matplotlib.pyplot as plt
import numpy as np


def create_bar_chart():
    """
    Create a simple bar chart.

    Returns
    -------
    None
    """
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]

    plt.bar(categories, values)
    plt.title("Sample Bar Chart")
    plt.xlabel("Category")
    plt.ylabel("Value")

    plt.show()


if __name__ == "__main__":
    create_bar_chart()