import sys
import csv
import pandas as pd
import numpy as np
import math
import json
import operator
from sklearn.feature_extraction.text import CountVectorizer
def getL2Distance(coor1, coor2):
    return math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)
def getLineInfo(coor1, coor2):
    a = (coor1[1] - coor2[1]) / (coor1[0] - coor2[0])
    b = coor1[1] - a * coor1[0]
    return a, b


api_key = "76129b4755674eabb8122486664765ab"


class Recommend:
    def __init__(self, path):
        self.dfScore = path
        #PoI = [1,2,5,7]
        #self.dfScore[1] = 1의점수
        #self.dfScore[5] = 5의점수
        
        # all scores are save
        # categorize: food, bar, (cafe, tourism)

    def recommend(self, userScore, PoI):

        #가장 유사도가 높은 3개의 PoI를 딕셔너리로 출력
        sorted(a.items() ,key=operator.itemgetter(1), reverse=True)[:3]

        # cosim을 기반으로 userScore PoI들 쭈루룩 비교해서 dictionary 만드는 기능
        pass
        # to-do 1
        # 기본 로직 1. 현재 위치가 들어오면 그 위치를 기준으로 거리제한 = PoI
        # 2. scroe 기반으로 정렬
        # 3. return 하
        # [액티비티,식당,...]
        # score = [0,1,,...]
        # PoI = [3,11,28,35,...](거리 기준으로 추려낸 장소들의 key값이 쭈루룩)
        # dfScore[3] = [0,1,1,...]

        # return {3:0.24,11:0.56,...} or [0.24,0.56]

    def cosim(self,userScore, dfscore):
        # list, numpy, series 2개의 vector가 주어지면 요거기반으로 cosim을 구하는 function
        # category = ['액티비티', '식당', '카페', '술집', '자연', '전시', '감성']
        # user_name 에는 사용자 이름만 담는다


        dfscore = pd.concat([userScore, dfscore])

        # category 안에는 PoI가 평가된 카테고리 이름만 담는다.
        category = []
        for i in userScore.iloc[user_name,:].index:
            if math.isnan(userScore.iloc[user_name,i]) == False:
                category.append(i)
    
        # U_df는 user_name가 평가된 것만 추출한다.
        U_df = self.dfScore[0]
    
        # other_df는 PoI를 제외한 데이터프레임이다.
        other_df=dfscore.iloc[:,category].drop(user_name, axis=0)
    
        # U_list는 PoI 가 평가된 카테고리를 리스트에 담는다.
        U_list = list(U_df.index)
    
        #sum_dict에 PoI과 다른 PoI 간의 유사도를 평가한 결과를 담게 됩니다.
        sim_dict={}
    
        # user와 PoI 둘 다 평점을 매긴 카테고리에 대한 벡터로 코사인 유사도를 구한다.
        for user in U_df.index:
            sm= [m for m in U_df.columns if math.isnan(other_df.iloc[user,m])==False]
        
            main_n = np.linalg.norm(U_df.iloc[user_name,sm])
            user_n = np.linalg.norm(other_df.iloc[user,sm])
            prod = np.dot(U_df.iloc[user_name,sm], other_df.iloc[user,sm])
            sim_dict[user]=prod/(main_n*user_n)

        #사용자
        a=cosim(user_name, dfscore)

        return a

        # to-do 2

        # src - 1,2,3 - dst(src == dst?)
        # 1,2,3 - tourism
        # how to recommend - think!
        # if code implementation is hard, trust me.

class DB:
    def __init__(self, coorPath, scorePath, xl=4, yl=2):
        self.dfCoor = pd.read_csv(coorPath)
        self.rS = Recommend(scorePath)
        self.xlimit = xl
        self.ylimit = yl
    def get(self, key, obj):
        return self.pd[key][obj]

    def getCoor(self, key):
        return self.dfCoor[key]["x"], self.dfCoor[key]["y"]

        if type(key) == int:

            return self.dfCoor[key]["x"], self.dfCoor[key]["y"]
        else:
            return key

    def squareVisitAlg(self, src, dst, mvp=False):

        results = []
        a, b = getLineInfo(src, dst)
        listOfPoI = self.getSquarebyTwo(src, dst)
        scorewithoutP = self.rS.recommend(listOfPoI)
        penalties = self.getPenalty(listOfPoI, a, b)
        scores = scorewithoutP / penalties
        for _ in range(2):
            spot = np.argmax(scores)
            results.append(spot)
            scores[spot] = -1
        if not mvp:
            spot = np.argmax(scores)
            results.append(spot)
        else:
            results.append(mvp)
        return self.idxToNum(results)
    def expandedSquareVisitAlg(self, src, mvp):

        results = []
        mvpCoor = self.getCoor(mvp)
        mvpCoor = self.getCoorByName(mvp)

        listOfPoI = self.getSquarebyTwo(src, mvpCoor)
        scores = self.rS.recommend(listOfPoI)
        for _ in range(2):
            spot = np.argmax(scores)
            results.append(spot)
            scores[spot] = -1
        results.append(mvp)
        return self.idxToNum(results)
    def greedyVisitAlg(self, src):
        results = []
        temp_src = src
        for _ in range(3):
            listOfPoI = self.getSquarebyOne(temp_src)
            scores = self.rS.recommend(listOfPoI)
            spot = np.argmax(scores)
            temp_src = spot
            results.append(spot)
        return self.idxToNum(results)

    def getSquarebyOne(self, place):
        x, y = self.getCoor(place)
        x = place[0]
        y = place[1]

        xmin = x - self.xlimit
        xmax = x + self.xlimit
        ymin = y - self.ylimit
        ymax = y + self.ylimit
        condition = "(x > @xmin) and (x < @xmax) and (y > @ymin) and (y < @ymax)"
        result = self.df.query(condition)
        return result["id"].to_numpy()

    def getSquarebyTwo(self, src, dst):
        x1, y1 = self.getCoor(src)
        if type(dst) == int:
            x2, y2 = self.getCoor(dst)
        else:
            x2 = dst[0]
            y2 = dst[1]
        x1 = src[0]
        y1 = src[1]
        x2 = dst[0]
        y2 = dst[1]

        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        condition = "(x > @xmin) and (x < @xmax) and (y > @ymin) and (y < @ymax)"
        result = self.df.query(condition)
        return result["id"].to_numpy()
    def getScore(self, userScore, listofPoI):
        return self.rS.recommend(userScore, listofPoI)
    def getPenalty(self, listofPoI, a, b):
        penalties = {}
        for poI in listofPoI:
            targetCoor = self.getCoor(poI)
            penalties[poI] = getLineInfo(targetCoor, a, b)
        return penalties
    def getResult(self, lst, src, dst):
        results = []
        results.append(src)
        coors = [self.getCoor(i) for i in lst]
        srcCoor = self.getCoor(src)
        dstCoor = self.getCoor(dst)
        distfromSrc = np.array([getL2Distance(i, srcCoor) for i in coors])
        results.append(coors[np.argmin(distfromSrc)])
        del coors[np.argmin(distfromSrc)]
        distfromDst = np.array([getL2Distance(i, dstCoor) for i in coors])
        results.append(coors[np.argmax(distfromDst)])
        results.append(coors[np.argmin(distfromDst)])
        results.append(dst)
        return results
def getCourse(input):
    db = DB("data.csv")
    dst, src, mvp = 1, 2, 3
    if dst == src:
        if len(mvp) == 0:
            result = db.greedyVisitAlg(src)
        else:
            result = db.expandedSquareVisitAlg(src, mvp)
    else:
        if len(mvp) == 0:
            result = db.squareVisitAlg(src, dst)
        else:
            result = db.squareVisitAlg(src, dst, mvp)
    return result
