// 메인 페이지

const selectId = { //토글 함수 만들기
    toggle : function(selector){
        target = document.getElementById(selector); 	
        if(target.style.display=='none'){ 		
            target.style.display = 'block'; 	
        }else{ 		
            target.style.display = 'none'; 	
        } 
    }
}

function boxToggle(){ //글 작성 박스 제어
    selectId.toggle("box-post")
}

function refresh(){ //새로고침
    window.location.reload();
}

function posting(){
    let brand = document.getElementById('select-brand').value
    let item = document.getElementById('select-item').value
    let desc = document.getElementById('textarea-desc').value
    $.ajax({
        type: 'POST',
        url: '/posts',
        data: {
            brand_give: brand,
            item_give: item,
            desc_give: desc
        },
        success: function (response) {
            console.log(response['msg'])
            refresh()
        }
    })
}