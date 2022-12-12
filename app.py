import hashlib  # 해쉬함수용 패키지
import datetime  # 시간관련 패키지
import jwt  # 토큰생성용 패키지
import mysql.connector
from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

SECRET_KEY = 'SPARTA'

# Database ============================================================================


def usercheck(page_url):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        # 진환님 기존 소스 db
        # user = db.user.find_one({'id': payload['id']})
        # return render_template(page_url, nick=user['nick'])

        # Mysql 신규 소스로 수정 db <여기서부터
        sql = "SELECT * FROM user WHERE user_id = %s"
        mycursor.execute(sql, (payload['id'],))
        myresult = mycursor.fetchall()
        return render_template(page_url, nick=myresult[0][3])
        # 여기까지>

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인정보가 없습니다"))
# 디비내용


# mysql-connector-python package
mydb = mysql.connector.connect(
    host="52.79.45.187",
    user="hello",
    passwd="mysqlserver",
    database="coffee"
)
mycursor = mydb.cursor()


# SERVER ============================================================================


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/main')
def main_render():
    page_url = "main.html"
    a = usercheck(page_url)
    return a


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)
    # return render_template('login.html')


@app.route('/signup')
def register():
    return render_template('signup.html')

# 회원가입api


@app.route('/api/signup', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # mongoDB
    # db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    # sql
    sqlFormula = "INSERT INTO user (user_id, user_pw, user_name) VALUES (%s, %s, %s)"
    newUser = (id_receive, pw_hash, nickname_receive)
    mycursor.execute(sqlFormula, newUser)
    mydb.commit()

    return jsonify({'result': 'success'})
# 중복확인api


@app.route('/api/confrepet', methods=['GET'])
def api_confrepet():

    # mongoDB
    # nick_id_list = list(db.user.find({},{'_id':False,'pw':False}))

    # mysql
    sql = "SELECT user_name FROM user"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    nick_id_list = myresult

    return jsonify({'nick_id_list': nick_id_list})

# 로그인 api


@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # pw암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # mongodb
    # result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    # mysql
    sql = "SELECT * FROM user WHERE user_id = %s"
    mycursor.execute(sql, (id_receive, ))
    myresult = mycursor.fetchall()

    # 아이디 조회 시, 없을 경우 []리턴, 있을 경우 [(id, user_id, user_pw, user_nickname)] 형식으로 리턴

    if (len(myresult) == 0):

        return jsonify({'result': 'fail', 'msg': '아이디가 없네요.'})
    if (myresult[0][2] == pw_hash):
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 유저정보확인api
@app.route('/nick', methods=['GET'])
def nick():
    return render_template('nicktest.html')
# 유저정보확인api


@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')
    # try:
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #     userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
    #     return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    # except jwt.ExpiredSignatureError:
    #     # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
    #     return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    # except jwt.exceptions.DecodeError:
    #     return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})

    try:
        # token을 시크릿키로 디코딩(해독)
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # mysql ------------------------------------------------------
        sql = "SELECT * FROM user WHERE user_id = %s"
        mycursor.execute(sql, (payload['id'],))
        myresult = mycursor.fetchall()
        return jsonify({'result': 'success', 'nickname': myresult[0][3]})
    # 만료 시간 지날 경우
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간 만료!!'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})
# 마이페이지 렌더링


@app.route('/mypage')
def mypage():
    page_url = "mypage.html"
    a = usercheck(page_url)
    return a


# 회원탈퇴 렌더링
@app.route('/withdraw')
def withdraw():
    page_url = "withdraw.html"
    a = usercheck(page_url)
    return a

# 회원탈퇴 api


@app.route('/api/withdraw', methods=['POST'])
def api_withdraw():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # mongoDB 조회
    # result = db.user.find({'id':id_receive,'pw':pw_hash})

    # mysql 아이디 비밀번호 동일 조회

    sql = "SELECT * FROM user WHERE user_id = %s AND user_pw = %s"
    mycursor.execute(sql, (id_receive, pw_hash))

    myresult = mycursor.fetchall()

    # 아이디 조회 시, 없을 경우 []리턴, 있을 경우 [(id, user_id, user_pw, user_nickname)] 형식으로 리턴

    if (len(myresult) == 0):
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

    if myresult is not None:

        # mongoDB 삭제
        # db.user.delete_one({'id':id_receive})

        # 삭제
        id_give = id_receive
        pw_give = pw_hash

        sql = "DELETE FROM user WHERE user_id = %s AND user_pw = %s"
        mycursor.execute(sql, (id_give, pw_give))
        mydb.commit()

        return jsonify({'msg': '탈퇴완료'})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# *메인 페이지
# 글 작성
@app.route('/posts', methods=["POST"])
def posts():
    brand_receive = request.form['brand_give']
    item_receive = request.form['item_give']
    desc_receive = request.form['desc_give']

    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userId = payload['id']

    author_receive = userId

    # mongodb
    # doc = {
    #     'brand':brand_receive,
    #     'item':item_receive,
    #     'desc':desc_receive
    # }
    # db.user.insert_one(doc)
    # print(brand_receive, item_receive, desc_receive)

    # sql insert
    # - article_brand
    # - article_item
    # - article_desc
    # - article_author
    # - article_like_count

    sqlFormula = "INSERT INTO article (article_brand, article_item, article_desc, article_author) VALUES (%s, %s, %s, %s)"
    newArticle = (brand_receive, item_receive, desc_receive, author_receive)
    mycursor.execute(sqlFormula, newArticle)
    mydb.commit()

    return jsonify({'msg': 'done'})

# 글 목록 출력


@app.route('/posts', methods=["GET"])
def post_list():
    # mongoDB
    # post_list = list(db.user.find({}, {'_id': False, 'id' : False, 'nick' : False, 'pw' : False}))

    # mycursor.execute("SELECT * FROM article")

    # 게시글에 좋아요 누른 사람 정보 가져오기
    # - article_id 기준으로 article - article_vote 테이블 조인해서 가져오기
    mycursor.execute("SELECT * FROM article LEFT JOIN article_vote ON article.id = article_vote.article_id")
    post_list = mycursor.fetchall()

    # 현재 user 토큰 가져오기
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userId = payload['id']

    print(post_list)
    return jsonify({'result': post_list, 'userId': userId})


@app.route('/like', methods=["POST"])
def likeToggle():

    # 좋아요 누른 게시글 index
    postIndex_receive = request.form['postIndex_give']

    # 닉네임 대신 ID에서 가져오는 걸로 수정함
    # nickName_receive = request.form['nickName_give']

    # 좋아요 누른 ID: 토큰에서 아이디 정보 얻기
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userId = payload['id']


    # DB: 좋아요 데이터 조회
    # - 이 유저 id가 해당 index 게시글을 누른 이력이 있냐?
    sql = "SELECT * FROM article_vote WHERE user_id = %s AND article_id = %s"
    mycursor.execute(sql, (userId, postIndex_receive))
    myresult = mycursor.fetchall()

    # like: DB에 like 이력이 없다면 이력 추가
    if len(myresult) == 0:
        print('좋아요 추가 완료')

        sqlFormula = "INSERT INTO article_vote (user_id, article_id) VALUES (%s, %s)"
        likeLog = (userId, postIndex_receive)
        mycursor.execute(sqlFormula, likeLog)
        mydb.commit()

    # unlike: DB 이력이 있다면 해당 이력 삭제
    else:
        print('좋아요 취소')
        sql = "DELETE FROM article_vote WHERE user_id = %s AND article_id = %s"
        mycursor.execute(sql, (userId, postIndex_receive))
        mydb.commit()

    # done 값을 찾아서
    # done 이 0 이면 1로 수정
    # done 이 1 이면 0으로 수정


    # vote 테이블에 저장
    # 게시글 고유 번호, 좋아요 누른 사람 닉네임, done

    return jsonify({'likeToggle': postIndex_receive + ' '})

# 삭제


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
