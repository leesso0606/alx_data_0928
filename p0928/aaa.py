import pandas as pd
# 1.1차원: Series, 2차원:DataFrame
# []리스트 구조-> 데이터분석에 용이하게 만든 라이브러리


# Series변환
temp=pd.Series([-20,-10,10,20])
print(temp)
print(temp[0])
# print(type(temp))
# print(type(1))
# print(type([1,2,3,4,5]))

# index추가
temp=pd.Series([-20,-10,10,20],index=['Jan','Feb','Mar','Apr'])
print(temp)
# print(temp[0]) #error: index 주어졌을 때는 0주소로 x
print(temp['Jan'])


# pip install pandas
# pip install matplotlib
# pip install xlrd
#  pip install openpyxl 설치