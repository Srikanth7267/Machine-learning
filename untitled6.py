# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KPGtt_s9ZbpDPGepvUlaZQMXLNd90RWm
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
np.random.seed(42)
def createdata():
  data = {
      'Age': np.random.randint(18, 70, size=20),
      'Salary': np.random.randint(30000, 120000, size=20),
      'Purchased': np.random.choice([0, 1], size=20),
      'Gender': np.random.choice(['Male', 'Female'], size=20),
      'City': np.random.choice(['New York', 'London', 'Sydney'], size=20),
  }
  df = pd.DataFrame(data)
  return df
df = createdata()
df.head(10)

df.shape

df.loc[5, 'Age'] = np.nan
df.loc[9, 'Salary'] = np.nan
df.head(10)

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df.head(10)

df_dropped = df.dropna()
df_dropped.head(10)

