import sys
import csv
import pandas as pd
import numpy as np
import math
import json


def getL2Distance(coor1, coor2):

    return math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)


def getLineInfo(coor1, coor2):
    a = (coor1[1] - coor2[1]) / (coor1[0] - coor2[0])
    b = coor1[1] - a * coor1[0]

    return a, b


class Recommend:
    def __init__(self, path):
        self.dfScore = np.load(path)

    def recommend(self, userScore, listofPoI):

        cos_sim = np.dot(listofPoI, userScore) / (
            np.linalg.norm(listofPoI, axis=1) * np.linalg.norm(userScore)
        )
        return cos_sim


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

    #db = DB("data.csv") 안지훈이 테스트 하려고 일단 주석처리함. 대규 나중에 풀어줘.
    print(input)
    dst, src, mvp = 1, 2, 3

    # if dst == src:
    #     if len(mvp) == 0:
    #         result = db.greedyVisitAlg(src)
    #     else:
    #         result = db.expandedSquareVisitAlg(src, mvp)
    # else:
    #     if len(mvp) == 0:
    #         result = db.squareVisitAlg(src, dst)
    #     else:
    #         result = db.squareVisitAlg(src, dst, mvp)

    result = {"courses": [(1, 1), (0, 2), (3, 4),(5, 6), (3, 1)]}

    return result
