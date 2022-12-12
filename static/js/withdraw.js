function withdraw() {
    let id = $('#userid').val()
    let pw = $('#userpw').val()
    if (id != "" && pw != "") {
        $.ajax({
            type: 'POST',
            url: '/api/withdraw',
            data: {"id_give": id, "pw_give": pw},
            success: function (response) {
                alert(response['msg'])
            }
        })
    } else {
        alert("아이디,비밀번호를 적어주세요")
    }
}

