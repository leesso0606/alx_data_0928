# 판다스 변환하는 이유:파이썬 리스트타입보다 계산이 더 용이
import pandas as pd

# 1차원 데이터-Series
temp=pd.Series([-20,-10,0,10,20],index=['1월','2월','3월','4월','5월']) #index와 시리즈 리스트 개수가 맞아야함
print(temp)
print(temp['1월'])
print(temp[['1월','2월']]) #2개 데이터 검색시 [[]]

# 2차원 데이터-DataFrame:딕셔너리타입의 리스트형태
data = {
    '이름':['강나래','강태원','강호림','김수찬','김재욱','박동현','박혜정','승근열'],
    '학교':['신림고','신림고','신림고','신림고','신림고','디지털고','디지털고','디지털고'],
    '키':[197,184,168,187,188,202,188,190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# DataFrame변환
df=pd.DataFrame(data)
print(df)

# # index추가
# df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# print(df)

# # DataFrame생성후 index를 지정
# df=pd.DataFrame(data)
# df.set_index('이름')
# print(df)

# # DataFrame생성후 index를 지정, inplace=True:index가 지정되어 반영됨
# df=pd.DataFrame(data)
# print(df.set_index('이름',inplace=True)) #이름컬럼을 index지정
# print(df)

# # index를 지정-index컬럼 이름을 지정할 수 있음
# df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원번호'
# print(df)

# # index지정 해제-drop=True:index를 삭제함,inplace=True:완전반영시켜져 저장
# df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원번호'
# # print(df.reset_index())
# # print(df.reset_index(drop=True))
# print(df.reset_index(drop=True,inplace=True))
# print(df)

# sort_index:index정렬,inplace=True:완전지정되어 저장
# asecnding=True:순차정렬, ascending=false:역순정렬
df=pd.DataFrame(data)
df.set_index('이름',inplace=True)
df.sort_index(inplace=True)
df.sort_index(inplace=True,ascending=False)#역순정렬
print(df)