import numpy as np
import pandas as pd
import seaborn as sns
import warnings

# Unable warnings.
warnings.filterwarnings('ignor')

train_df = pd.read_csv("train.csv")
train_df.head()
