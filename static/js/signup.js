// 아이디, 비밀번호, 닉네임을 받아 DB에 저장합니다.
//아이디 중복확인, 비밀번호 확인
function check_id() {
    let id = $('#userid').val()
    let space = id.includes(" ")

    if (space == false && id.length >= 3) {
        $.ajax({
            type: "GET",
            url: "/api/confrepet",
            data: {},
            success: function (response) {
                let id_list = response['nick_id_list']
                if (id_list.length == 0) {
                    $('#idcheck').val("check")
                }
                for (let i = 0; i < id_list.length; i++) {
                    if (id != id_list[i]['id']) {
                        $('#idcheck').val("check")
                    } else {
                        $('#idcheck').val("uncheck")
                        alert("동일한 아이디가 있습니다")
                        break;
                    }
                }
                if ($('#idcheck').val() == "check") {
                    alert("사용가능합니다")
                }


            }
        })
    } else {
        alert("아이디가 너무 짧습니다")
    }

}

function signup() {
    let userpw = $('#userpw').val()
    let re_userpw = $('#re_userpw').val()
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

    $.ajax({
        type: "GET",
        url: "/api/confrepet",
        data: {},
        success: function (response) {
            let nick_list = response['nick_id_list']
            console.log(nick_list);

            if (nick_list.length == 0) {
                $('#nickcheck').val("check")
            }

            for (let i = 0; i < nick_list.length; i++) {
                console.log(nick_list[i])

                // nick 있는 경우
                if (nick_list[i][0] == nick) {
                    $('#nickcheck').val() == "uncheck"
                    alert("이미 있는 아이디 불가합니다")
                    return;
                }
                // nick 없는 경우

                // if (nick != nick_list[i]['nick']) {
                //     $('#nickcheck').val("check")
                // } else {
                //     $('#nickcheck').val("uncheck")
                //     alert("동일한 닉네임이 있습니다")
                //     break;
                // }
            }
            $('#nickcheck').val("check")
            alert("사용가능한 닉네임입니다 😃")


            // if($('#nickcheck').val() == "check"){
            //     alert("사용가능합니다")
            // }
        }
    })
}
