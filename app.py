from flask import Flask, render_template, jsonify, request, session, redirect, url_for
app = Flask(__name__)
from pymongo import MongoClient

import jwt #토큰생성용 패키지
import datetime #시간관련 패키지
import hashlib #해쉬함수용 패키지
SECRET_KEY = 'SPARTA'

client = MongoClient("mongodb+srv://test:sparta@cluster0.053coum.mongodb.net/?retryWrites=true&w=majority")
db = client.cofee
def usercheck(page_url):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({'id': payload['id']})
        return render_template(page_url, nick=user['nick'])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인정보가 없습니다"))


#디비내용
@app.route('/')
def home():
   return render_template('login.html')

@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)
    # return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('signup.html')

#회원가입api
@app.route('/api/signup', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    return jsonify({'result': 'success'})
#중복확인api
@app.route('/api/confrepet', methods=['GET'])
def api_confrepet():
    nick_id_list = list(db.user.find({},{'_id':False,'pw':False}))

    return jsonify({'nick_id_list': nick_id_list})

#로그인 api
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    #pw암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success','nick':result['nick'], 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


#유저정보확인api
@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
#마이페이지 렌더링
@app.route('/mypage')
def mypage():
    page_url="mypage.html"
    a = usercheck(page_url)
    return a
    # token_receive = request.cookies.get('mytoken')
    # try:
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #     user = db.user.find_one({'id': payload['id']})
    #     return render_template(page_url, nick = user['nick'])
    # except jwt.ExpiredSignatureError:
    #     return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    # except jwt.exceptions.DecodeError:
    #     return redirect(url_for("login", msg="로그인정보가 없습니다"))



#회원탈퇴 렌더링
@app.route('/withdraw')
def withdraw():
    page_url = "withdraw.html"
    a = usercheck(page_url)
    return a

#회원탈퇴
@app.route('/api/withdraw', methods=['POST'])
def api_withdraw():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw-give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.user.find({'id':id_receive,'pw':pw_hash})
    if result is not None:
        db.user.delete_one({'id':id_receive})
        return jsonify({'msg': '탈퇴완료'})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


#*메인 페이지
#글 작성
@app.route('/posts', methods=["POST"])
def posts():
    brand_receive = request.form['brand_give']
    item_receive = request.form['item_give']
    desc_receive = request.form['desc_give']

    doc = {
        'brand':brand_receive,
        'item':item_receive,
        'desc':desc_receive
    }

    db.user.insert_one(doc)
    print(brand_receive, item_receive, desc_receive)
    return jsonify({'msg':'done'})

#글 목록
@app.route('/posts', methods=["GET"])
def post_list():
    print('리스트 파이썬')
    post_list = list(db.user.find({}, {'_id': False, 'id' : False, 'nick' : False, 'pw' : False}))
    print(post_list)
    return jsonify({'result':post_list})

@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)