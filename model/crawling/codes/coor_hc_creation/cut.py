# coordinate 결과 / scoring 위한 틀 생성하는 코드.

import pandas as pd
import os
import sys

def main(which):
    folder_path = 'result_full_' + which
    #folder_path = 'result_full_' + which # 전체 파일 용
    coor_path = os.path.join('coor',which+'_result.csv')

    fl_list = os.listdir(folder_path)

    coors = pd.read_csv(coor_path)

    result = pd.DataFrame(columns = ['name','x','y'])
    forHard = pd.DataFrame(columns = ['name','activity','inside','nature','photo','cafe'])
    print(len(fl_list))
    for fl in fl_list:
        #fName = fl[:-4].split("|")[0] # alcohol / food / cafe
        fName = fl[:-4].split('|')[0] # tourism
        
        try:
            x = float(coors.loc[coors['name'] == fName,'x'])
        except:
            print(coors.loc[coors['name'] == fName,'x'])
        try:
            y = float(coors.loc[coors['name'] == fName,'y'])
        except:
            print(coors.loc[coors['name'] == fName,'y'])
        
        result = result.append({'name':fName,'x':x,'y':y},ignore_index=True)
        forHard = forHard.append({'name':fName,'activity':0,'inside':0,'nature':0,'photo':0,'cafe':0},ignore_index=True)
    #forHard.to_csv(which+'_hc.csv', sep=',',  na_rep='NaN') #하드코딩 csv

    result = result.sort_values('name')
    result.to_csv(which+'_coor.csv', sep=',',  na_rep='NaN') #좌표 csv

    print(result)

if __name__ == "__main__":
    main(sys.argv[1])