// 메인 페이지

$(document).ready(function () { //페이지 로딩 후 글 목록 출력
    listing('starbucks')
});

function refresh(){ //새로고침
    window.location.reload();
}

const box = { //토글 함수 만들기
    toggle : function(selector){
        target = document.querySelector(selector); 	
        if(target.style.display === 'none'){ 		
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

function nowSelect(targetName){
    const targetClass = `.nav-${targetName}`
    const targetA = document.querySelector(targetClass)
    const navBrands = document.querySelectorAll('.nav-brand-a')
    let nowSelect = 'now-select' // 클릭 선택 클래스
    for(let i=0; i<navBrands.length; i++){
        let navA = navBrands[i]
        navA.classList.remove(nowSelect)
    }
    targetA.classList.add(nowSelect)
}

function listing(brandName){
    nowSelect(brandName)
    let brandView = brandName
    let boxUl = document.querySelector('#box-ul-list')
    let temp_html = ''
    boxUl.innerHTML = '' //리스트 초기화
    $.ajax({
        type: 'GET',
        url: '/posts',
        data: {},
        success: function (response) {
            let row = response['result']
            let imgSrc = '/static/images/png'
            for(let i=0; i<row.length; i++){
                let getBrand = row[i]['brand']
                let getItem = row[i]['item']
                let getDesc = row[i]['desc']
                if(getBrand === brandView){
                    console.log('brandView : ', brandView)
                    temp_html = `<li class="li-item">
                                    <a href="#">
                                        <img src="${imgSrc}/${getBrand}-${getItem}.png" alt="${getBrand} ${getItem}">
                                        <span class="name-item">${getItem}</span>
                                        <span>${getDesc}</span>
                                    </a>
                                </li>`
                    boxUl.insertAdjacentHTML("beforeend", temp_html)
                }
            }
        }
    })
}
