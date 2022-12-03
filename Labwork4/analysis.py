from population import load_file_as_table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

# mean(x): returns the mean of the one-dimensional array x
def mean(x):
    return np.mean(x)


# variance(x): returns the variance of the one-dimensional array x
def variance(x):
    return np.var(x)


# covariance(x,y): returns the covariance of the one-dimensional array x and y
def covariance(x, y):
    return np.cov(x, y)


# median(x): returns the median of the one-dimensional array x
def median(x):
    return np.median(x)


def plot_question1(weight, height) -> None:
    plt.plot(weight, height, ".")
    plt.xlabel("Weight (kg)")
    plt.ylabel("Height (cm)")
    plt.title("Weight/Height population")
    plt.show()


def plot_question2(weight, height) -> None:
    a, b = np.polyfit(weight, height, 1)
    plt.plot(weight, height, ".")
    plt.plot(weight, a * np.array(weight) + b, color="red")
    plt.xlabel("Weight (kg)")
    plt.ylabel("Height (cm)")

    plt.title("Weight/Height population")
    plt.show()


def plot_question3(woman_weight, woman_height) -> None:
    a, b = np.polyfit(woman_weight, woman_height, 1)
    plt.plot(woman_weight, woman_height, ".")
    plt.plot(woman_weight, a * np.array(woman_weight) + b, color="red")
    plt.ylabel("Height (cm)")
    plt.xlabel("Weight (kg)")
    plt.title("Weight/Height Female")
    plt.show()


def plot_question4(man_weight, man_height, woman_weight, woman_height) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
    a, b = np.polyfit(woman_weight, woman_height, 1)
    ax1.plot(woman_weight, woman_height, ".")
    ax1.plot(woman_weight, a * np.array(woman_weight) + b, color="red")
    ax1.set_xlabel("Weight (kg)")
    ax1.set_ylabel("Height (cm)")
    ax1.set_title("Woman")

    a, b = np.polyfit(man_weight, man_height, 1)
    ax2.plot(man_weight, man_height, ".")
    ax2.plot(man_weight, a * np.array(man_weight) + b, color="red")
    ax2.set_xlabel("Weight (kg)")
    ax2.set_title("Man")

    plt.show()


def plot_question5(num_correct_bmi_man, num_correct_bmi_woman) -> None:
    fig, ax = plt.subplots(figsize=(12, 8))
    X = np.arange(1)
    ax.bar(X + 0.25, num_correct_bmi_man, width=0.25)
    ax.bar(X + 0.5, num_correct_bmi_woman, width=0.25)
    ax.set_title("BMI correct")
    ax.legend(labels=["Men", "Women"])
    ax.xaxis.set_visible(False)
    plt.show()


def plot_question6(
    num_underweight_man, num_underweight_woman, num_overweight_man, num_overweight_woman
) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
    X = np.arange(1)
    ax1.bar(X + 0.25, num_underweight_man, width=0.25)
    ax1.bar(X + 0.5, num_underweight_woman, width=0.25)
    ax1.set_title("Thin")
    ax1.legend(labels=["Men", "Women"])
    ax1.xaxis.set_visible(False)
    ax1.set_yticks(np.arange(0, 12, 2))

    ax2.bar(X + 0.25, num_overweight_man, width=0.25)
    ax2.bar(X + 0.5, num_overweight_woman, width=0.25)
    ax2.set_title("Obese")
    ax2.legend(labels=["Men", "Women"])
    ax2.xaxis.set_visible(False)
    ax2.set_yticks(np.arange(0, 12, 2))

    plt.show()


def plot_question7(weight, height):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(
        x=weight,
        y=height,
        ax=ax,
        n_levels=6,
        thresh=0,
        cbar=True,
        fill=True,
        cmap="nipy_spectral",
        common_norm=False,
        alpha=0.6,
    )
    plt.show()


def calculate_population(df: pd.DataFrame) -> None:
    print("Mean of population's weight: ", mean(df["weight"]))
    print("Mean of population's height: ", mean(df["height"]))
    print("Median of population's weight: ", median(df["weight"]))
    print("Median of population's height: ", median(df["height"]))
    print("Variance of population's weight: ", variance(df["weight"]))
    print("Variance of population's height: ", variance(df["height"]))


if __name__ == "__main__":
    df = load_file_as_table("population.csv")
    calculate_population(df)
    weight = df["weight"].values.tolist()
    height = df["height"].values.tolist()
    # plot_question1(weight, height)
    # plot_question2(weight, height)
    woman_weight = df[df["sex"] == "f"]["weight"]
    woman_height = df[df["sex"] == "f"]["height"]
    man_weight = df[df["sex"] == "h"]["weight"]
    man_height = df[df["sex"] == "h"]["height"]
    # plot_question3(woman_weight, woman_height)
    # plot_question4(man_weight, man_height, woman_weight, woman_height)
    df["bmi"] = df["weight"] / ((df["height"] / 100) * (df["height"] / 100))
    bmi_man = df[df["sex"] == "h"]["bmi"]
    bmi_woman = df[df["sex"] == "f"]["bmi"]
    num_correct_bmi_man = len([bmi for bmi in bmi_man if (bmi < 25 and bmi > 18.5)])
    num_correct_bmi_woman = len([bmi for bmi in bmi_woman if (bmi < 25 and bmi > 18.5)])
    # plot_question5(num_correct_bmi_man, num_correct_bmi_woman)

    num_underweight_man = len([bmi for bmi in bmi_man if (bmi < 18.5)])
    num_underweight_woman = len([bmi for bmi in bmi_woman if (bmi < 18.5)])
    num_overweight_man = len([bmi for bmi in bmi_man if (bmi > 25.5)])
    num_overweight_woman = len([bmi for bmi in bmi_woman if (bmi > 25.5)])

    # plot_question6(num_underweight_man, num_underweight_woman, num_overweight_man, num_overweight_woman)
    plot_question7(weight, height)
