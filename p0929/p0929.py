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
# df.reset_index(inplace=True) : index를 컬럼으로 옮기고 새로운 인덱스 만듬
# df.reset_index(drop=True, inplace=True) :index 삭제
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

# -------------------------------------------------------------------------------
import pandas as pd
df = pd.read_excel('file/score.xlsx',index_col='지원번호')

# 컬럼 슬라이싱
# 컬럼선택 : df[컬럼] , 2개이상 []리스트로 추가
df[['이름','키','학교']]
df.columns # 컬럼전체출력
df.columns[0]
df.columns[1]
df.columns[-1]     # 마지막 컬럼명 출력
df['SW특기']       # 마지막 컬럼 출력
df[df.columns[-1]] # 마지막 컬럼 출력
df[['이름','학교']]

df['이름']  #df[컬럼명만 들어갈수 있음]

# 컬럼 슬라이싱
df[ df.columns[[0,3,-1]] ] # 컬럼 슬라이싱
df[df.columns[1:4]]        # 컬럼 슬라이싱
df.columns[1:4]   # 컬럼명

# ------------------------------------------

# pandas 에서 파일 저장하기-.ipynb에서
# database프로그램과 호환가능
import pandas as pd

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

df=pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name='지원번호'
# csv
df.to_csv('file/score.csv',encoding='utf-8-sig')#utf-8-sig:excel파일에 확인가능

# txt -어느 기준에서 분리할 지 설정할 수 있음
df.to_csv('file/score.txt') # ,를 기준으로 분리
df.to_csv('file/score.txt',sep='\t') # 탭 간격으로 분리
df.to_csv('file/score.txt',sep='*') # * 간격으로 분리

# xlsx(엑셀)
df.to_excel('file/score.xlsx')

# ----------------------------------------------------

# 파일 읽기-read_csv,txt,xlsx
# skiprows=n : 상단 n줄 만큼 제외하고 가져옴
# usecols=n:m :n에서m 까지의 컬럼을 가져올 수 있음
# nrows : 설정한 줄만큼 가져옴

# read_csv
df=pd.read_csv('file/score.csv')
df=pd.read_csv('file/score.csv',skiprow=3)
df=pd.read_csv('file/score.csv',skiprows=[1,3,5])

df=pd.read_csv('file/score.csv',nrows=4)

# read_txt
df=pd.read_csv('file/score.txt')
df=pd.read_csv('file/score.txt',sep='\t') #읽어올 때 어떤 구분자를 사용할지 지정
df=pd.read_csv('file/score.txt',sep='*') 

# read_excel
# xlsx파일 불러오기-index지정해서 가져오기:index_col
df=pd.read_excel('file/score.xlsx')
df=pd.read_excel('file/score.xlsx', index_col='지원번호')

# -----------------------------------------------------------------------------

# DataFrame 합치기:concat
# usecole :컬럼 선택해서 가져오기
# skiprows:상단부분 제외 후 가져오기


df1=pd.read_csv('file/2014년졸음운전교통사고.csv',encoding='euc-kr')
df2=pd.read_csv('file/2015년졸음운전교통사고.csv',encoding='euc-kr')
df3=pd.read_csv('file/2016년졸음운전교통사고.csv',encoding='euc-kr')

# df=pd.concat([df1,df2,df3]) #DataFrame합치기

# --------------------------------------------------------------------------------------

import pandas as pd
df=pd.read_excel('file/score.xlsx',index_col='지원번호')

# 1차원 데이터(Series)의 값을 가져옴
# df.[컬럼명].max()...
df['키'].max() #최대값
df['키'].nlargest(3) #최대값3명
df['키'].nsmallest(3) #최소값3명

df['학교'].unique() #중복제거 후 리스트
df['학교'].nunique() #중복 제거 후 개수

# 컬럼의 기본정보:타입, 크기,이름,null값,개수 확인
df.info()

# 기본통계확인-숫자로 된 컬럼의 통계 정보를 한 번에 보여주는 함수, 기본적인 통계를 보여줌
df.describe()
# count:데이터 개수 / mean:평균 /std:표준편차/ min:최소값 / max:최대값 / 25%,505,75%는 각 지점의 값

# 크기확인 (행,열)-row,cols
df.shape

df.head() #상단에 5개만 확인
df.tail() #하단에 5개만 확인
df.head(3) #상단에 3개만 확인
df.tail(3) #하단에 3개만 확인
df.values #배열구조로 확인
df.index #index리스트
df.columns #컬럼 확인

# ------------------------------------------------------------------

import pandas as pd
df=pd.read_excel('file/score.xlsx',index_col='지원번호')

# 컬럼 선택: df[컬럼명], 2개 이상 df[[컬럼명,컬럼]]
df[['이름','키','학교']]
df.columns #컬럼 전체 출력
df.columns[0]
df.columns[1]
df.columns[-1] #마지막 컬럼명 출력
df['SW특기']       #마지막 컬럼 출력
df[df.columns[-1]] #마지막 컬럼 출력
df[df.columns[[0,3,-1]]] #컬럼명을 여러개 사용해서 출력

# 컬럼 슬라이싱(세로)
df[df.columns[[0,3,-1]]] #컬럼 슬라이싱(세로 전체)
df[df.columns[1:4]]      #컬럼 슬라이싱(세로 전체)
df.columns[1:4] #컬럼 명만

# rows 슬라이싱(가로)
df['이름'][:3]
df[['이름','학교','SW특기']][2:] # 3개의컬럼+2번째rows부터 끝까지
df[0:3] #rows 에 대한 슬라이싱 # 주소값이 0-2까지 rows 출력

# ------------------------------------------------

# 타입변경 : astype():int, float, str
df=pd.read_excel('file/연령별인구현황_2025.xlsx',skiprows=3,usecols='C:D,H:I')
#str타입 replace 함수 :천단위 쉼표 삭제
# 타입변경: astype(int)-int타입으로 변경가능 또는 float,str도 가능
df[:1]['총 인구수'].str.replace(",","").astype(int) 

# -------------------------------------------------------

df=pd.read_excel('file/합계출산율_2026.xlsx',skiprows=28, nrows=2)
df.columns
df.set_index('Unnamed: 0',inplace=True)
df.index.name='제목'
df

# index의 유니코드까지 출력가능
df.index.values
df.index
df.index.values #index안에 유니코드까지 출력이 가능
df.index.values[1]

# index의 이름 변경 : df.rename(index={'원래 index values:'변경할 index values},inplace=True)
df.rename(index={'출생아\xa0수':'출생아 수'},inplace=True)
df.rename(index={'합계\xa0출산율':'합계 출산율'},inplace=True)

# 컬럼 축을 변경
df=df.T #row,index변경가능
df


# -----------------------------------------------------------------------

# 데이터 선택-rows

# loc-이름검색,ilco-index주소로 검색
df.loc['1번'] #index가 1번인 rows출력
df.iloc[0] #index의 주소가 0인 rows출
df.index #index의 모든 이름 출력

# loc 형태-row출력 -> index의 값으로
df.loc[['1번','2번']] #2개출력
df.loc['3번']        #1개 출력
df.loc['3번','국어'] #1개의 row에서 국어컬럼만 출력
df.loc['1번':'4번'] #1번~4번까지 출력
df.loc['1번':'4번',['학교','영어']] #loc는 index슬라이싱가능, column슬라이싱 가능
df.loc['1번':'4번','학교':'영어'] #loc는 index슬라이싱가능, column슬라이싱 가능
df.loc[['1번','4번'],['학교','영어']] #loc는 index슬라이싱가능, column슬라이싱 가능

# iloc-row출력 ->index의 주소로
df.loc['1번']
df.loc['1번':'4번']
df.iloc[0]
df.iloc[0:4]    # ilco슬라이싱 가능
df.iloc[[0,2,4]] #2개는 리스트
df.iloc[0:3,1:5] #index슬라이싱, columns슬라이싱
df.iloc[[0,2],1:5] #index2개는 리스트
df.iloc[[0,2],[1,3,5]] #index,columns2개는 리스트
df.iloc[:,[0,3,4,6]] #모든 index, columns 슬라이싱


# -----------------------------------------------------

# 조건문
# 조건:필터적용해서 조건적용
df['키']>=185 #True,False 형태로 출력
df[df['키']>=185]
# 변수로 입력받아 적용
filt=df['키']>=185 
df[filt]
df[~filt] #not적용

df2=df[filt]
df3=df2[['이름','키','국어']]
df3

#  &와 | 를 사용
# df[컬럼명] / df.loc,iloc[index명]
df3=df2[df2['국어']>=80]
# 키가 185이상 and 국어가90점 이상
df[(df['키']>=185)& (df['국어']>=90)]
# 키가 185이상 or 국어가90점 이상
df[(df['키']>=185)| (df['국어']>=90)]
# 키가 185이상 and 국어가90점 이상인 출력 중 수학점수만
df[(df['키']>=185)& (df['국어']>=90)]['수학']
df.loc[(df['키']>=185)& (df['국어']>=90),'수학']