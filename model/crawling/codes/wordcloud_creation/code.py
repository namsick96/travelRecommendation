# 각 리뷰들을 바탕으로 wordcloud 파일들 생성하는 code.
# 파일경로는 다음과 같음
""" 
ㄴreview
  ㄴ cafe.csv
  ㄴ tourism.csv
  ㄴ …
ㄴcount
  ㄴ cafe.csv
  ㄴ tourism.csv
  ㄴ …
ㄴresult
code.py 
"""

import numpy as np
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import pandas as pd
import sys
import os
from tqdm import tqdm


def main(common_limit):

    review_path = "review"
    count_path = "count"
    result_path = "result"

    fl_list = os.listdir(review_path)
    print(common_limit)
    kom = Okt()
    
    print(fl_list)
    for fl in fl_list:

        num = 0

        reviews = pd.read_csv(os.path.join(review_path, fl),'|')
        counts = pd.read_csv(os.path.join(count_path, fl))['0'].to_list()

        counts = [int(i.split(' ')[-1]) for i in counts]
        for count in tqdm(counts):

            if count < 10:
                continue
            review = reviews.iloc[num : num + count, 3].dropna()
            category = reviews.iloc[num, 0]
            name = reviews.iloc[num, 1]

            num += count

            sentences_tag = []

            for sentence in review:
                morph = kom.pos(sentence)
                sentences_tag.append(morph)

            noun_list = []
            for sentence in sentences_tag:
                for word, tag in sentence:
                    if tag in ["Noun"]:
                        noun_list.append(word)
            noun_list = [n for n in noun_list if len(n) > 1]

            counts = Counter(noun_list)
            tags = counts.most_common(common_limit)

            wordcloud = WordCloud(
                font_path="/dwyu/Library/Fonts/NanumGothic.ttf", # 자신의 font 경로
                background_color="white",
                width=800,
                height=600,
            )
            try:
                cloud = wordcloud.generate_from_frequencies(dict(tags))
                cloud.to_file(os.path.join(result_path,name+"|"+category+".png")) 
            except:
                print("no")


if __name__ == "__main__":
    main(int(sys.argv[1]))