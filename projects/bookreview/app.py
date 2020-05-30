from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    print(request.form)
    ## 1. 데이터 읽어오기 (저자 / 제목 / 리뷰)
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    review={
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    ## 2. DB에 넣는다
    db.review.insert_one(review)
    print(review)
    return jsonify({'result':'success', 'msg': '성공적으로 등록을 완료하였습니다'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    ## 1. DB에 리뷰 데이터 요청
    reviews = list(db.review.find({},{'_id':False}))
    print(reviews)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)