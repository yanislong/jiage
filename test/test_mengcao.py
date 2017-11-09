# -*- coding=utf-8 -*-
#通过给定的经纬度，获取该地区的实时气温，湿度，天气情况, 首先访问高德地图天气接口，访问失败再从本地查询。无数据的项置为null

import requests
import json

import numpy as np
import urllib

'''url = "https://api.gagogroup.cn/api/v3/weather/realtime"
param = {"lat":0, "lon":-90}
header = {"token":"f4eb4a8119a563339678bf7f6f6de0b9804682ddbb3443f6b0959ba42139906e20febf772efd33cebbee7f04439792bb"}
r = requests.get(url, params=param, headers=header)
print r.content

url = "http://demo.gagogroup.cn/mengcao-img/#/Coverage"
url1 = "http://demo.gagogroup.cn/mengcao-img/#/Degeneration"
header = {"token":"fa619e77287c49370eb0048eb304b910f4659f9f436eefa5e2cac73590b5e7a72c93fc324ac7de050644890248e79fe8"}
r = requests.get(url1, headers=header)
print r.content
'''
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = urllib.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]

from sklearn import preprocessing
# normalize the data attributes
normalized_X = preprocessing.normalize(X)
# standardize the data attributes
standardized_X = preprocessing.scale(X)

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X, y)
# display the relative importance of each attribute
print(model.feature_importances_)

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
# create the RFE model and select 3 attributes
rfe = RFE(model, 3)
rfe = rfe.fit(X, y)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)

'''
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X, y)
# display the relative importance of each attribute
print(model.feature_importances_)
'''
