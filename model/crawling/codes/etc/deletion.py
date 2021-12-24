# 리뷰데이터에서 아래 문자열 제거하는 코드.

import pandas as pd

data = pd.read_csv('파일경로/alcohol_reviews.csv', sep='|')

df = pd.DataFrame(data)
df = df.replace("(Google 번역 제공)", '', regex=True)
df = df.replace("(원문)", '', regex=True)

df.to_csv('파일경로/alcohol_reviews.csv', mode='w', sep='|', index=False)