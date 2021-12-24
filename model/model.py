import sys
import csv
import pandas as pd
import numpy as np
import math
import json


def decomposeInput(input):

    dst = input["destination"]
    lst_dst = list(dst.values())
    lst_mvp = input["mvp"]
    userScore = input["scores"]
    lst_userScore = list(userScore.values())
    lst_userScore = [i / 10 for i in lst_userScore]
    src = input["starting"]
    lst_src = list(src.values())

    iC = [lst_dst, lst_src, lst_mvp, lst_userScore]
    iR = [lst_dst, lst_src, lst_userScore]
    iB = [lst_dst, lst_userScore]

    return (iC, iR, iB)


def getL2Distance(coor1, coor2):

    return math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)


def getLineInfo(coor1, coor2):
    a = (coor1[1] - coor2[1]) / (coor1[0] - coor2[0])
    b = coor1[1] - a * coor1[0]

    return a, b


def getLineDistance(x, y, a, b):

    return abs(a * x - y + b) / (a ** 2 + b ** 2) ** 0.5


class Recommend:
    def __init__(self, path):
        try:
            self.dfScore = pd.read_csv(path, encoding="cp949")
        except:
            self.dfScore = pd.read_csv(path, encoding="utf-8")

        # self.dfScore = self.dfScore.dropna(axis=0)
        # PoI = [1,2,5,7]
        # self.dfScore[1] = 1의점수
        # self.dfScore[5] = 5의점수

        # all scores are save
        # categorize: food, bar, (cafe, tourism)

    def recommend(self, poi, userScore):
        # list, numpy, series 2개의 vector가 주어지면 요거기반으로 cosim을 구하는 function

        # category = ['액티비티', '식당', '카페', '술집', '자연', '전시', '감성']

        # fitness_dict에 PoI과 다른 PoI 간의 유사도를 평가한 결과를 담게 됩니다.
        poiScore = self.dfScore.iloc[poi, 1:]

        result = []
        for poidx in poi:
            poiScore = self.dfScore.iloc[poidx, 1:]
            main_n = np.linalg.norm(userScore)
            user_n = np.linalg.norm(poiScore)
            prod = np.dot(userScore, poiScore)
            result.append(prod / (main_n * user_n))

        # user와 PoI 둘 다 평점을 매긴 카테고리에 대한 벡터로 코사인 유사도를 구한다.

        return result


class DB:
    def __init__(self, coorPath, scorePath, xl=0.2, yl=0.1):

        self.dfCoor = pd.read_csv(coorPath)
        self.rS = Recommend(scorePath)
        self.xlimit = xl
        self.ylimit = yl

    def getCoor(self, key):

        return float(self.dfCoor.iloc[key, 2]), float(self.dfCoor.iloc[key, 3])

    def squareVisitAlg(
        self,
        src,
        dst,
        userScore,
        mvp=False,
    ):

        results = []
        a, b = getLineInfo(src, dst)
        listOfPoI = self.getSquarebyTwo(src, dst)
        scorewithoutP = self.rS.recommend(listOfPoI, userScore)

        penalties = self.getPenaltywithLine(listOfPoI, a, b)

        scorewithoutP = np.array(scorewithoutP)
        penalties = np.array(penalties)
        penalties = penalties * penalties

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

        return self.getResult(results, src, dst)

    def expandedSquareVisitAlg(self, src, mvp, userScore):

        results = []
        mvpCoor = self.getCoor(mvp)

        listOfPoI = self.getSquarebyTwo(src, mvpCoor)
        scores = self.rS.recommend(listOfPoI, userScore)
        penalties = self.getPenaltywithDot(listOfPoI, src)

        scores = np.array(scores)
        penalties = np.array(penalties)

        scores = scores / (1 + np.exp(-1 * penalties))

        for _ in range(2):
            spot = np.argmax(scores)
            results.append(listOfPoI[spot])
            scores[spot] = -1

        results.append(mvp)

        return self.getResult(results, src, src)

    def greedyVisitAlg(self, src, userScore):
        results = []
        temp_src = src
        temp = -1
        for _ in range(3):
            xl = self.xlimit
            yl = self.ylimit
            listOfPoI = []

            while len(listOfPoI) == 0:
                listOfPoI = self.getSquarebyOne(temp_src, xl, yl)
                xl += 0.1
                yl += 0.1
            scores = self.rS.recommend(listOfPoI, userScore)
            spot = np.argmax(scores)
            if listOfPoI[spot] == temp:
                scores[spot] = -1
                spot = np.argmax(scores)
            temp = listOfPoI[spot]
            temp_src = self.getCoor(spot)
            results.append(listOfPoI[spot])

        return self.getResult(results, src, src)

    def getSquarebyOne(self, place, xl, yl):

        result_lst = []
        while len(result_lst) <= 3:
            x = place[0]
            y = place[1]

            xmin = x - xl
            xmax = x + xl
            ymin = y - yl
            ymax = y + yl

            condition = "(x > @xmin) and (x < @xmax) and (y > @ymin) and (y < @ymax)"

            result = self.dfCoor.query(condition)

            result_lst = result.index.tolist()

            xl += 0.05
            yl += 0.1
        print(result.index.tolist())
        return result.index.to_numpy()

    def getSquarebyTwo(self, src, dst):

        result_lst = []

        xl = 0
        yl = 0
        while len(result_lst) <= 3:
            x1 = src[0]
            y1 = src[1]
            x2 = dst[0]
            y2 = dst[1]

            xmin = min(x1, x2) - xl
            xmax = max(x1, x2) + xl
            ymin = min(y1, y2) - yl
            ymax = max(y1, y2) + yl

            condition = "(x > @xmin) and (x < @xmax) and (y > @ymin) and (y < @ymax)"

            result = self.dfCoor.query(condition)

            result_lst = result.index.tolist()

            xl += 0.05
            yl += 0.1

        return result.index.to_numpy()

    def getPenaltywithDot(self, poIs, target):

        penalties = []
        for poI in poIs:
            coor = self.getCoor(poI)
            penalties.append(getL2Distance(coor, target))

        return penalties

    def getPenaltywithLine(self, listofPoI, a, b):

        penalties = []
        for poI in listofPoI:
            x, y = self.getCoor(poI)
            penalties.append(getLineDistance(x, y, a, b))

        return penalties

    def getResult(self, lst, src, dst):

        results = []

        coors = [self.getCoor(i) for i in lst]
        names = [self.dfCoor.iloc[i, 1] for i in lst]
        adds = [list(self.dfCoor.iloc[i]) for i in lst]
        distfromSrc = np.array([getL2Distance(i, src) for i in coors])
        results.append(names[np.argmin(distfromSrc)])

        del coors[np.argmin(distfromSrc)]
        del names[np.argmin(distfromSrc)]

        distfromDst = np.array([getL2Distance(i, dst) for i in coors])
        results.append(names[np.argmax(distfromDst)])
        results.append(names[np.argmin(distfromDst)])

        return results


def getCourse(input, db):

    dst, src, mvp, userScore = input
    print(getL2Distance(src, dst))
    if getL2Distance(src, dst) <= 0.01:
        if mvp == 380:
            result = db.greedyVisitAlg(src, userScore)
        else:
            result = db.expandedSquareVisitAlg(src, mvp, userScore)
    else:
        if mvp == 380:
            result = db.squareVisitAlg(src, dst, userScore)
        else:
            result = db.squareVisitAlg(src, dst, userScore, mvp)

    return result


def getRestaruant(input, db):

    dst, src, userScore = input

    userScore = userScore[:-1]
    if getL2Distance(src, dst) <= 0.01:
        result = db.greedyVisitAlg(src, userScore)
    else:
        result = db.squareVisitAlg(src, dst, userScore)

    return result


def getBar(input, db):

    dst, userScore = input

    userScore = userScore[:-1]

    result = db.greedyVisitAlg(dst, userScore)

    return result


def main(inputs, dbs):

    iC, iR, iB = decomposeInput(inputs)
    courses = getCourse(iC, dbs[0])
    restaurants = getRestaruant(iR, dbs[1])
    bars = getBar(iB, dbs[2])

    return courses, restaurants, bars
