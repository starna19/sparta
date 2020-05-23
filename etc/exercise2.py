from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# 매트릭스 평점가져오기
result = db.cinema.find_one({'title':'매트릭스'})
print('매트릭스 평점: ',result['star'])

# 매트릭스와 같은 평점 영화 재목 가져오기
mtrx_star = result['star']
same_star = db.cinema.find({'star':mtrx_star})
print('<매트릭스와 동일 평점 영화>')
for title in same_star:
    print(title['title'])

# 위의 영화 평점 0으로 만들기
db.cinema.update_many({'star':mtrx_star},{'$set':{'star':0}})

# 평점 0인 영화 제목 보기
star_zero = db.cinema.find({'star':0})
print('<평점 0인 영화>')
for zero in star_zero:
    print(zero['title'])