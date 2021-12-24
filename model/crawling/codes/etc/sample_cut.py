# 전체 sample data 목록에서 이미 수집한 data 를 제외한 data 들을 추려내기 위한 코드.

import pandas as pd
import os
import sys

from pandas.core.tools.timedeltas import to_timedelta
def main(which):

    sample_path = 'sampled_'+which+'.csv'

    sample = pd.read_csv(sample_path,sep='|')
    toDel = pd.read_csv(os.path.join('data',which+'_review_num.csv'))

    toDel = toDel['0'].tolist()
    toDel_list = [i.split(' ')[:-1] for i in toDel]
    toDel = [" ".join(i) for i in toDel_list]

    for tod in toDel:
        sample = sample[sample.이름 != tod]

    print(sample)

    sample.to_csv('re'+sample_path,sep="|",index=False)

if __name__ == "__main__":
    main(sys.argv[1])