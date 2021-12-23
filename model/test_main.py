import rsgaram
import numpy as np

path = 'example_score.npy'
rs = rsgaram.Recommend(path)

print(rs.recommend([1,1,1],[1,2,3]))
print(rs.recommend([1,0,1],[1,2,3]))
print(rs.recommend([0,0,1],[1,2,3]))

# example_score = [[[1,1,1],[1,0,1],[0,0,1]]]