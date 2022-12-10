// 메인 페이지

$(document).ready(function () { //페이지 로딩 후 글 목록 출력
    listing()
});

function refresh(){ //새로고침
    window.location.reload();
}

const box = { //토글 함수 만들기
    toggle : function(selector){
        target = document.querySelector(selector); 	
        if(target.style.display=='none'){ 		
            target.style.display = 'block'; 	
        }else{ 		
            target.style.display = 'none'; 	
        } 
    }
}

function boxToggle(){ //글 작성 박스 제어
    box.toggle("#box-post")
}

function posting(){
    let brand = document.querySelector('#select-brand').value
    let item = document.querySelector('#select-item').value
    let desc = document.querySelector('#textarea-desc').value
    if(brand === 'none' || item === 'none' || desc.replace(/\s/gi, "").length === 0){
        alert('내용을 입력하세요.')
        return false
    }else{ // 입력이 다 되면 ajax
        $.ajax({
            type: 'POST',
            url: '/posts',
            data: {
                brand_give: brand,
                item_give: item,
                desc_give: desc
            },
            success: function (response) {
                let doneMsg = response['msg']
                if(doneMsg !== 'done'){
                    return false
                }else{
                    refresh()
                }
            }
        })
    }
}

function listing(){
    $.ajax({
        type: 'GET',
        url: '/main',
        data: {},
        success: function (response) {

        }
    })
}