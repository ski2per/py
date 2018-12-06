import matplotlib.pyplot as plt

import re
import os.path
import pandas as pd

#SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "sample")
SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "raw")


def get_sample_list():
    return os.listdir(SAMPLE_DIR)


def get_delay(sample):
    # mat = re.search("[0-9]+ms", sample)
    mat = re.search("[0-9]+", sample)
    if mat:
        delay = mat.group(0)
    else:
        delay = ""

    return delay


def plot_all_sample():
    all_sample = pd.DataFrame()
    samples = get_sample_list()

    for sample in samples:
        delay = get_delay(sample)
        if not delay:
            continue

        df = pd.read_json(os.path.join(SAMPLE_DIR, sample), lines=True)
        df["elapse"] = df["endTime"] - df["startTime"]
        # df.drop(["endTime", "startTime", "invokeStatus", "valueAfter", "valueBefore"],axis=1)
        all_sample = pd.concat([all_sample, df["elapse"]], axis=1)
        all_sample = all_sample.rename(columns={"elapse": delay})

    all_sample.plot()
    plt.show()


def plot_all_mean():
    sample_mean = {}

    samples = get_sample_list()

    for sample in samples:
        delay = get_delay(sample)
        if not delay:
            continue

        df = pd.read_json(os.path.join(SAMPLE_DIR, sample), lines=True)
        df["elapse"] = df["endTime"] - df["startTime"]
        # sample_mean[int(delay)] = df["elapse"].mean()
        sample_mean[delay] = df["elapse"].mean()

    s = pd.Series(sample_mean)

    # print(s.index)
    s.index = s.index.astype("int64")
    # s.sort_index().plot.bar()
    s.sort_index().plot()
    plt.show()



if __name__ == "__main__":
    # plot_all_sample()
    plot_all_mean()
