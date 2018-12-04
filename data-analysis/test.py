#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

df = pd.read_json("sample\\simulation-0ms.log", lines=True)

df.plot()