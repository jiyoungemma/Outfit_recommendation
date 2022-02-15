# 평균 풍속 10 이상 -> 겉옷 필수, 일강수량 0 이상이면 우산 필수

# season : spring 1, summer 2, autumn 3, winter 4
# clothes : 
# ~4 : 패딩, 두꺼운 코드, 히트텍, 목도리, 장갑  -- so cold 1
# 5~8 : 코트, 가죽자켓, 니트, 플리스 -- cold 2
# 9~11 : 트렌치코트, 야상, 자켓  -- chilly 3
# 12~16 : 기모후드티, 가디건, 니트/맨투맨 -- little chilly 4
# 17~19 : 후드티, 바람막이, 슬랙스 --  little warm 5
# 20~22 : 셔츠, 7부바지, 면바지 --  warm 6
# 23~27 : 티셔츠, 반바지 -- hot 7
# 28~ : 민소매, 숏팬츠 -- so hot 8

# import pandas as pd
# import numpy as np
# import pickle

# df = pd.read_csv('weather.csv')

# target = 'outfit'
# features = ['평균기온(°C)']
# # '일강수량(mm)','평균풍속(m/s)','season'

# df.to_csv('weather.csv', encoding='utf-8-sig')

# df.isna().sum().sort_values()

# from sklearn.model_selection import train_test_split
# train, test = train_test_split(df, test_size=0.2, random_state=2)
# train.shape, test.shape

# train, val = train_test_split(train, test_size =0.2, random_state=2)
# train.shape, val.shape

# X_train = train[features]
# y_train = train[target]
# X_val = val[features]
# y_val = val[target]
# X_test = test[features]
# y_test = test[target]

# from category_encoders import OrdinalEncoder
# from sklearn.pipeline import make_pipeline
# from sklearn.tree import DecisionTreeClassifier

# pipe = make_pipeline(
#     OrdinalEncoder(),
#     DecisionTreeClassifier(max_depth=5, random_state=2)
# )

# pipe.fit(X_train, y_train)
# print('검증 정확도 : ', pipe.score(X_val, y_val))
# print('테스트 정확도 : ', pipe.score(X_test, y_test))

# with open('weather.pkl','wb') as file:
#     pickle.dump(pipe, file)

import pickle

model = None
with open('weather.pkl', 'rb') as file:
    model = pickle.load(file)
