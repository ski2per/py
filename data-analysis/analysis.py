import matplotlib.pyplot as plt

import re
import os.path
import pandas as pd

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "sample")

def get_sample_list():
    return os.listdir(SAMPLE_DIR)


def plot_all_sample():
    all = pd.DataFrame()
    samples = get_sample_list()
    
    for sample in samples:
        delay = ""
        #mat = re.search("[0-9]+ms", sample)
        mat = re.search("[0-9]+", sample)
        if mat:
            delay = mat.group(0)

        df = pd.read_json(os.path.join(SAMPLE_DIR,sample), lines=True)
        df["elapse"] = df["endTime"] - df["startTime"]
        #df.drop(["endTime", "startTime", "invokeStatus", "valueAfter", "valueBefore"],axis=1)
        all = pd.concat([all, df["elapse"]], axis=1)
        all = all.rename(columns={"elapse": delay})

    all.plot()
    plt.show()

def plot_all_mean():
    pass

if __name__ == "__main__":
    plot_all_sample()