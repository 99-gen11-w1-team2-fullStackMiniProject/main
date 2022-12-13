$(document).ready(function () { //페이지 로딩 후 글 목록 출력
    listing()
});
function listing(){
    // nowSelect(brandName)
    //brandName
    // let brandView = brandName
    //
    let boxUl = document.querySelector('#box-ul-list')
    let temp_html = ''
    boxUl.innerHTML = '' //리스트 초기화

    $.ajax({
        type: 'GET',
        url: '/mypage/liked',
        data: {},
        success: function (response) {

            let row = response['article_list']

            // const userId = response['userId']

            let imgSrc = '/static/images/png'
            // let heart = {
            //     blank:'🤍',
            //     fill:'❤️'
            // }
            for(let i=0; i<row.length; i++){
                let getBrand = row[i][1] // brand
                let getItem = row[i][2] // item
                let getDesc = row[i][3] // desc
                //let getNick = row[i][3] // desc

                let getIndex = row[i][0] // 게시글 고유 id 값
                // let liked = (row[i][7] == userId)? 1 : 0;
                //if(getBrand === brandView){
                    // done 0 일때

                    temp_html = `<li class="li-item ${getIndex}">
                                   <div class="item-wrap">
                                       <div class="img">
                                           <a href="#">
                                                <img src="${imgSrc}/${getBrand}-${getItem}.png" alt="${getBrand} ${getItem}">
                                           </a> 
                                       </div>        
                                       <div class="mypage-content">
                                          <p><span class="name-item">${getItem}</span></p>
                                          <p><span>${getDesc}</span></p>
                                       </div> 
                                   </div>
                                                                                                                                                         
                                </li>`
                    // done 1 일때
                    boxUl.insertAdjacentHTML("afterbegin", temp_html)
                //}
            }
        }
    })
}