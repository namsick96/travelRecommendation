import sys
import csv
import pandas as pd
import numpy as np
import math
import json


def decopmoseInput(input):
    pass


def getL2Distance(coor1, coor2):

    return math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)


def getLineInfo(coor1, coor2):
    a = (coor1[1] - coor2[1]) / (coor1[0] - coor2[0])
    b = coor1[1] - a * coor1[0]

    return a, b


api_key = "76129b4755674eabb8122486664765ab"


class Recommend:
    def __init__(self, path):
        self.dfScore = np.load(path)
        # all scores are save
        # categorize: food, bar, (cafe, tourism)

    def recommend(self, score, PoI):
        pass
        # to-do 1
        # [액티비티,식당,...]
        # score = [0,1,,...]
        # PoI = [3,11,28,35,...]
        # dfScore[3] = [0,1,1,...]
        # recommend function - study!

        # return {3:0.24,11:0.56,...} or [0.24,0.56]

        # to-do 2

        # src - 1,2,3 - dst(src == dst?)
        # 1,2,3 - tourism
        # how to recommend - think!
        # if code implementation is hard, trust me.
        #


class DB:
    def __init__(self, coorPath, scorePath, xl=4, yl=2):
        self.dfCoor = pd.read_csv(coorPath)
        self.rS = Recommend(scorePath)
        self.xlimit = xl
        self.ylimit = yl

    def get(self, key, obj):
        return self.pd[key][obj]

    def getCoor(self, key):

        if type(key) == int:
            return self.dfCoor[key]["x"], self.dfCoor[key]["y"]
        else:
            return key

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

    def expandedSquareVisitAlg(self, src, mvp, userScore):

        results = []
        mvpCoor = self.getCoorByName(mvp)

        listOfPoI = self.getSquarebyTwo(src, mvpCoor)
        scores = self.rS.recommend(listOfPoI, userScore)

        for _ in range(2):
            spot = np.argmax(scores)
            results.append(spot)
            scores[spot] = -1

        results.append(mvp)

        return self.idxToNum(results)

    def greedyVisitAlg(self, src, userScore):
        results = []
        temp_src = src

        for _ in range(3):
            listOfPoI = self.getSquarebyOne(temp_src)
            scores = self.rS.recommend(listOfPoI, userScore)
            spot = np.argmax(scores)
            temp_src = spot
            results.append(spot)

        return self.idxToNum(results)

    def getSquarebyOne(self, place):
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

    def getPenalty(self, listofPoI, a, b):

        penalties = {}

        for poI in listofPoI:
            targetCoor = self.getCoor(poI)
            penalties[poI] = getLineInfo(targetCoor, a, b)

        return penalties

    def getResult(self, lst, src, dst):

        results = []

        coors = [self.getCoor(i) for i in lst]

        distfromSrc = np.array([getL2Distance(i, src) for i in coors])
        results.append(coors[np.argmin(distfromSrc)])
        del coors[np.argmin(distfromSrc)]

        distfromDst = np.array([getL2Distance(i, dst) for i in coors])
        results.append(coors[np.argmax(distfromDst)])
        results.append(coors[np.argmin(distfromDst)])

        return results


def getCourse(input, db):

    dst, src, mvp, userScore = input

    if dst == src:
        if len(mvp) == 0:
            result = db.greedyVisitAlg(src, userScore)
        else:
            result = db.expandedSquareVisitAlg(src, mvp, userScore)
    else:
        if len(mvp) == 0:
            result = db.squareVisitAlg(src, dst, userScore)
        else:
            result = db.squareVisitAlg(src, dst, userScore, mvp)

    return result


def getRestaruant(input, db):

    dst, src, userScore = input

    if dst == src:
        result = db.greedyVisitAlg(src, userScore)
    else:
        result = db.squareVisitAlg(src, dst, userScore)

    return result


def getBar(input, db):

    dst, userScore = input

    result = db.greedyVisitAlg(dst, userScore)

    return result


def main(inputs, dbs):

    iC, iR, iB = decopmoseInput(inputs)
    courses = getCourse(iC, dbs[0])
    restaurants = getRestaruant(iR, dbs[1])
    bars = getBar(iB, dbs[2])
