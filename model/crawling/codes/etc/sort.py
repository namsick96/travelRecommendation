# 각 파일들에 대해 오름차순으로 정렬하기 위한 코드.

import pandas as pd

data = pd.read_csv('파일경로/alcohol_result.csv')

df = pd.DataFrame(data)
df = df.drop(df.columns[0], axis=1)
df = df.sort_values('name')

df.to_csv('파일경로/alcohol_result_new.csv', mode='w', index=False)