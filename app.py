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
        sql = "SELECT * FROM user WHERE user_id = %s"
        mycursor.execute(sql, (payload['id'],))
        myresult = mycursor.fetchall()
        return render_template(page_url, nick=myresult[0][3])
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
def api_signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # sql
    sqlFormula = "INSERT INTO user (user_id, user_pw, user_name) VALUES (%s, %s, %s)"
    newUser = (id_receive, pw_hash, nickname_receive)
    mycursor.execute(sqlFormula, newUser)
    mydb.commit()

    return jsonify({'result': 'success'})
# 중복확인api


@app.route('/api/confrepet', methods=['GET'])
def api_confrepet():

    # mysql
    sql = "SELECT user_id,user_name FROM user"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    id_nick_list = myresult

    return jsonify({'id_nick_list': id_nick_list})

# 로그인 api
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # pw암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
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
        return jsonify({'result': 'success', 'token': token.decode('utf8')})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 유저정보확인api
@app.route('/nick', methods=['GET'])
def nick():
    return render_template('nicktest.html')



@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

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

#마이페이지 좋아요 리스팅
@app.route('/mypage/liked')
def mypage_liked():
    #유저가 누른 좋아요 가져오기
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    # - article_id 기준으로 article - article_vote 테이블 조인해서 가져오기
    #mycursor.execute("SELECT * FROM article LEFT JOIN article_vote ON article.id = article_vote.article_id")
    #mycursor.execute("SELECT * FROM article_vote WHERE user_id = %s")
    sql = "SELECT * FROM article_vote WHERE user_id = %s"
    mycursor.execute(sql, (payload['id'],))
    post_list = mycursor.fetchall()

    list=[]
    for row in post_list:
        row[2]
        sql = "SELECT id, article_brand, article_item, article_desc, article_author FROM article WHERE id = %s"
        mycursor.execute(sql, (row[2],))
        article_list = mycursor.fetchall()
        if article_list != []:
            list.extend(article_list)




    return jsonify({'article_list': list})

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

    # mysql 아이디 비밀번호 동일 조회
    sql = "SELECT * FROM user WHERE user_id = %s AND user_pw = %s"
    mycursor.execute(sql, (id_receive, pw_hash))
    myresult = mycursor.fetchall()

    # 아이디 조회 시, 없을 경우 []리턴, 있을 경우 [(id, user_id, user_pw, user_nickname)] 형식으로 리턴
    if (len(myresult) != 0):
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

    # 현재 user 토큰 가져오기
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    userId = payload['id']
    print(userId)

    mycursor.execute("SELECT * FROM article")
    all_articles = mycursor.fetchall()

    mycursor.execute(f"SELECT article_id FROM article_vote WHERE user_id = '{userId}'")
    favorite_articles = mycursor.fetchall()

    return jsonify({
        'all_articles': all_articles,
        'favorite_articles': favorite_articles,
        'userId': userId})


@app.route('/like', methods=["POST"])
def likeToggle():

    # 좋아요 누른 게시글 index
    postIndex_receive = request.form['postIndex_give']

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

    return jsonify({'likeToggle': postIndex_receive + ' '})


<<<<<<< HEAD
#  수정기능
@app.route('/deit', methods=['POST'])
def edit_posting():
    brand = request.form['brand_give']
    desc = request.form['desc_give']
    image = request.form['image_give']
    item = request.form['item_give']
    index = request.form['index_give']
    nick = request.form['nick_give']
    db.posts.update_one({"_id": user(id)}, {'$set': {'brand': brand, 'desc': desc, 'image': image, 'item': item, 'index': index, 'nick':nick}})
    return jsonify({'msg': '업데이트 완료'})


# 삭제
=======
>>>>>>> d8976162998e65c72edc1883429d406b378359ab
@app.route("/delete", methods=["POST"])
def delete_btn():
    num = request.form['num_give']
    print(type(num))
    num1 = int(num)
    db.post.delete_one({'num': num1})

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
