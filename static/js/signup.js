// 아이디, 비밀번호, 닉네임을 받아 DB에 저장합니다.
//아이디 중복확인, 비밀번호 확인
// const reg_id = /허용하는 문자/
// const reg_pw = /허용하는 문자/ 시간남으면 하자
function check_id() {

    let id = $('#userid').val()
    let space = id.includes(" ")

    if (space == false && id.length >= 3) {
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
    } else {
        alert("아이디가 너무 짧거나 공백이있습니다.")
    }
}

function signup() {
    let userpw = $('#userpw').val()
    let re_userpw = $('#re_userpw').val()
    if(userpw.includes(" ")) {
        alert("비밀번호를 입력하세요")
        return;
    }
    if (userpw == re_userpw && $('#idcheck').val() == "check") {
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
    } else {
        alert("비밀번호가 다르거나 아이디중복확인이필요")
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
