import matplotlib.pyplot as plt

import re
import os.path
import pandas as pd

sample_dir = os.path.join(os.path.dirname(__file__), "sample")

samples = os.listdir(sample_dir)

total = pd.DataFrame()

for sample in samples:
    delay = ""
    mat = re.search("[0-9]+ms", sample)
    if mat:
        delay = mat.group(0)
        
    df = pd.read_json(os.path.join(sample_dir,sample), lines=True)
    df["elapse"] = df["endTime"] - df["startTime"]
    #df.drop(["endTime", "startTime", "invokeStatus", "valueAfter", "valueBefore"],axis=1)
    total = pd.concat([total, df["elapse"]], axis=1)
    total = total.rename(columns={"elapse", delay})

print(total)





#df.plot()
#plt.show()