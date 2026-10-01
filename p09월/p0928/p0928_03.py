import pandas as pd

data={
    '이름':['강나래','강태원','강호림','김수찬','김재욱','박동현','박혜정','승근열'],
    '학교':['심림고','신림고','신림고','신림고','심림고','디지털고','디지털고','디지털고'],
    '키':[197,184,168,187,188,202,188,190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
# print(data) #딕셔너리 형태


# 1.딕셔너리 ->판다스 형태변환
# df=pd.DataFrame(data)
# print(df)



# 2. 2차원데이터-index,index.name추가
# df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
# df.index.name='지원번호'
# 3. 컬럼1개 출력
# print(df['이름']) #판다스 형태로 출력
# 3-2. 컬럼2개 출력-[]리스트형태로 입력을 해야함
# print(df[['이름','학교','키']])


# 4.index삭제
df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name='지원번호'
# print(df.reset_index()) #inplace를 하지 않으면 출력만 삭제되고 적용이 안됨
# df.reset_index(inplace=True) #index삭제 적용됨. index가 컬럼에 적용/기존 index를 컬럼으로 이동하고, df에 그 변경을 바로 적용한다
df.reset_index(drop=True,inplace=True) #index완전삭제됨

print(df)


# 5. 2차원 데이터-원하는 컬럼만 분리, 없는 키 넣으면 Nan
# df=pd.DataFrame(data,columns=['이름','국어','키','학교'])
# print(df)
# print(df['이름']) #key입력시 key출력
# print(df['합계']) #없는 key입력시 에러