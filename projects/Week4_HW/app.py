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
@app.route('/orders', methods=['POST'])
def write_orders():
    print(request.form)
    ## 1. 데이터 읽어오기 (이름 / 수량 / 주소 / 전화번호)
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    order={
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    ## 2. DB에 넣는다
    db.orders.insert_one(order)
    print(order)
    return jsonify({'result':'success'})


@app.route('/orders', methods=['GET'])
def read_orders():
    ## 1. DB에 리뷰 데이터 요청
    orders = list(db.orders.find({},{'_id':False}))
    # print(orders)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'orders':orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)