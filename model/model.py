def getValue(key):
    # get value of key from DB
    pass


def squareVisitAlg(src, dst):
    pass


def squareVisitwithMVPAlg(src, dst, mvp):
    pass


def expanedSquareVisitAlg(src, mvp):
    pass


def greedyVisitAlg(src):
    pass


def main():

    dst = "a"
    src = "b"
    mvp = ["a", "b", "c"]

    if dst == src:
        if len(mvp) == 0:
            result = greedyVisitAlg(src)
        else:
            result = expanedSquareVisitAlg(src, mvp)
    else:
        if len(mvp) == 0:
            result = squareVisitAlg(src, mvp)
        else:
            result = squareVisitwithMVPAlg(src, dst, mvp)

    return result
