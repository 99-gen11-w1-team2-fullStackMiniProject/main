// 아이디, 비밀번호, 닉네임을 받아 DB에 저장합니다.
//아이디 중복확인, 비밀번호 확인

//아래는 아이디 패스워드 정규식 검색해서 넣음
const reg_id = /^[a-z]+[a-z0-9]{4,}$/;
const reg_pw = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/

function check_id() {
    let id = $('#userid').val()
    if(reg_id.test(id)){
        $.ajax({
                    type: "GET",
                    url: "/api/confrepet",
                    data: {},
                    success: function (response) {
                        let id_nick_list = response['id_nick_list']
                        for (let i = 0; i < id_nick_list.length; i++) {
                            if (id == id_nick_list[i][0]) {
                                $('#idcheck').val("uncheck")
                                alert("동일한 아이디가 있습니다")
                                return;
                            }
                        }
                        $('#idcheck').val('check')
                        alert("사용가능합니다")
                    }
                })
    }else{
        alert("아이디가 형식에 맞지않습니다")
    }
}

function signup() {
    let userpw = $('#userpw').val()
    let re_userpw = $('#re_userpw').val()
    if(reg_pw.test(userpw) && userpw == re_userpw && $('#idcheck').val() == "check" && $('#nickcheck').val() == "check" ){
        $.ajax({
            type: "POST",
            url: "/api/signup",
            data: {
                id_give: $('#userid').val(),
                pw_give: $('#userpw').val(),
                nickname_give: $('#usernick').val()
            },
            success: function (response) {
                if (response['result'] == 'success') {
                    alert('회원가입이 완료되었습니다.')
                    window.location.href = '/login'
                } else {
                    alert(response['msg'])
                }
            }
        })
    }else{
        alert("비밀번호가 형식에 맞지 않거나 아이디중복확인이필요")
    }
}

function check_nick() {

    let nick = $('#usernick').val()

    if (nick.length != 0) {
        $.ajax({
            type: "GET",
            url: "/api/confrepet",
            data: {},
            success: function (response) {
                let id_nick_list = response['id_nick_list']
                for (let i = 0; i < id_nick_list.length; i++) {
                    if (id_nick_list[i][1] == nick) {
                        $('#nickcheck').val('uncheck')
                        alert("이미 있는 닉네임입니다 불가합니다")
                        return;
                    }
                }
                $('#nickcheck').val("check")
                alert("사용가능한 닉네임입니다 😃")
            }
        })
    }

}
