import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob


def load_dataset(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    return df


def display_column_name(df: pd.DataFrame) -> None:
    for i, col in enumerate(df.columns):
        print(f"Column {i+1}: {col}")

    print(f"The number of rows: {df.shape[0]}")
    print(f"The number of columns: {len(df.columns)}")
    print("The first line of the dataframe: ")
    display(df.iloc[0])

    print("Set index: ")
    df1 = df.set_index("Age")
    display(df1.head())


def display_men_and_women(df: pd.DataFrame, df1: pd.DataFrame) -> None:
    labels_2019 = df["Age"].values
    men_2019 = df["M"].values / 1e6
    women_2019 = df["F"].values / 1e6

    labels_2020 = df1["Age"].values
    men_2020 = df1["M"].values / 1e6

    women_2020 = df1["F"].values / 1e6
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    X_axis = np.arange(len(labels_2019))
    ax1.bar(X_axis, men_2019, width=0.2)
    ax1.bar(X_axis + 0.2, women_2019, width=0.2)
    ax1.set_title("Population of Vietnam in 2019", fontsize=8)
    ax1.set_xlabel("Age")
    ax1.set_ylabel("Number of people (in million)")
    ax1.set_xticks(X_axis, labels_2019, fontsize=8)
    ax1.legend(labels=["M", "F"])
    ax1.grid()
    ax1.ticklabel_format()

    ax2.bar(X_axis, men_2020, width=0.2)
    ax2.bar(X_axis + 0.2, women_2020, width=0.2)
    ax2.set_title("Population of Vietnam in 2020", fontsize=8)
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Number of people (in million)")
    ax2.set_xticks(X_axis, labels_2020, fontsize=8)
    ax2.legend(labels=["M", "F"])
    ax2.grid()
    fig.tight_layout()
    plt.show()


def display_variation(df: pd.DataFrame, df1: pd.DataFrame) -> None:
    labels_2019 = df["Age"].values
    men_2019 = df["M"].values
    women_2019 = df["F"].values

    men_2020 = df1["M"].values

    women_2020 = df1["F"].values
    men_difference = men_2020 - men_2019
    women_difference = women_2020 - women_2019
    fig, ax = plt.subplots(figsize=(10, 6))
    X_axis = np.arange(len(labels_2019))
    ax.bar(X_axis, men_difference, width=0.2)
    ax.bar(X_axis + 0.2, women_difference, width=0.2)
    ax.set_title("Population variation between 2019 and 2020", fontsize=8)
    ax.set_xlabel("Age")
    ax.set_ylabel("Number of people")
    ax.set_xticks(X_axis, labels_2019, fontsize=8)
    ax.legend(labels=["M", "F"])
    ax.grid()
    ax.ticklabel_format()

    plt.show()


def display_population_variation() -> None:
    csv_files = sorted(glob.glob("datas/*.csv"), key=lambda x: x.split("-")[1][:4])
    populations_all = []
    populations_men = []
    populations_women = []
    populations_all_variation = []
    populations_men_variation = []
    populations_women_variation = []
    for file_name in csv_files:
        df = pd.read_csv(file_name)
        populations_men.append(np.sum(df["M"].values))
        populations_women.append(np.sum(df["F"].values))
        populations_all.append(np.sum(df["M"].values) + np.sum(df["F"].values))
    for i in range(1, len(populations_men)):
        populations_men_variation.append(populations_men[i] - populations_men[i - 1])
        populations_women_variation.append(
            populations_women[i] - populations_women[i - 1]
        )
        populations_all_variation.append(populations_all[i] - populations_all[i - 1])

    fig, ax = plt.subplots(figsize=(10, 6))
    X_axis = np.arange(1991, 2023)
    ax.plot(X_axis, populations_women_variation)
    ax.plot(X_axis, populations_men_variation)
    ax.plot(X_axis, populations_all_variation)
    ax.set_title("Variation of Vietnam population", fontsize=8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of people")
    ax.legend(labels=["Women", "Men", "Total"])
    ax.grid()
    ax.set_xticks(np.arange(min(X_axis) - 1, max(X_axis) + 1, 2))
    plt.show()


def display_age_variation() -> None:
    csv_files = sorted(glob.glob("datas/*.csv"), key=lambda x: x.split("-")[1][:4])
    populations_all = []
    populations_all_variations = []
    labels = pd.read_csv(csv_files[0])["Age"].values.tolist()
    for i in range(21):
        for file_name in csv_files:
            df = pd.read_csv(file_name)
            populations_all.append(df.iloc[i]["M"] + df.iloc[i]["F"])
    for i in range(21):
        population_index = []
        for j in range(1, 33):
            population_index.append(
                populations_all[i * 33 + j] - populations_all[i * 33 + j - 1]
            )
        populations_all_variations.append(population_index)
    fig, ax = plt.subplots(figsize=(10, 6))
    X_axis = np.arange(1991, 2023)
    for i in range(len(populations_all_variations)):
        ax.plot(X_axis, populations_all_variations[i])
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of people")
    ax.set_title("Variation of Vietnam population by age", fontsize=8)
    ax.ticklabel_format(useOffset=False)
    ax.set_xticks(np.arange(min(X_axis) - 1, max(X_axis) + 1, 2))
    ax.legend(labels=labels, loc="lower left", prop={"size": 8.3})
    ax.set_ylim = (-500000, 300000)
    ax.grid()
    plt.show()


def display_age_group() -> None:
    csv_files = sorted(glob.glob("datas/*.csv"), key=lambda x: x.split("-")[1][:4])
    X_axis = np.arange(1991, 2023)
    populations_group = []
    populations_group_variations = []
    labels = ["0-19", "20-39", "40-59", "60-79", "80-99", "100+"]
    fig, ax = plt.subplots(figsize=(10, 6))
    X_axis = np.arange(1991, 2023)
    for i in range(0, 21, 4):
        for file_name in csv_files:
            df = pd.read_csv(file_name)
            if i < 20:
                populations_group.append(
                    np.sum(df.iloc[i : i + 4]["M"]) + np.sum(df.iloc[i : i + 4]["F"])
                )
            else:
                populations_group.append(
                    np.sum(df.iloc[i]["M"]) + np.sum(df.iloc[i]["F"])
                )
        # break
    for i in range(6):
        population_index = []
        for j in range(1, 33):
            population_index.append(
                populations_group[i * 33 + j] - populations_group[i * 33 + j - 1]
            )
        populations_group_variations.append(population_index)
    for i in range(len(populations_group_variations)):
        ax.plot(X_axis, populations_group_variations[i])
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of people")
    ax.set_title("Variation of Vietnam population by age group", fontsize=8)
    ax.ticklabel_format(useOffset=False)
    ax.set_xticks(np.arange(min(X_axis) - 1, max(X_axis) + 1, 2))
    ax.legend(labels=labels, loc="lower left", prop={"size": 8})
    ax.grid()
    plt.show()


if __name__ == "__main__":
    df = load_dataset("datas/Viet Nam-2019.csv")
    df1 = load_dataset("datas/Viet Nam-2020.csv")
    # display(df.head())
    # display_column_name(df)
    # display_men_and_women(df, df1)
    # display_variation(df, df1)
    # display_population_variation()
    # display_age_variation()
    display_age_group()
