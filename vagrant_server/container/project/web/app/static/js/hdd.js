window.onload = function() {
    var tmp = document.getElementsByClassName("info");
    var tmp2 = document.getElementsByName("button");
    var tmp3 = document.getElementsByClassName('card');
    var moji = "hddID";

    for(var i=0;i<=tmp.length-1;i++){
        //id追加
        tmp[i].setAttribute("id",moji+i);
        tmp2[i].setAttribute("id", i);
        tmp3[i].setAttribute("id","img" + i)
    }
    height_repair();
};

function height_repair(){
  var tmp = document.getElementsByClassName("button");
  var tmp2 = document.getElementsByClassName("button hidden");

  $('#background').css({
    "height": 450 + 147.5 * (tmp.length - tmp2.length)
  })
};


function addPro(id_value){

    var text = document.getElementById('hddID' + id_value);
    var image = document.getElementById('img' + id_value);
    var name = text.getElementsByTagName('h1').item(0).innerText;
    var src = image.getElementsByTagName('img').item(0).src;
    var price = text.getElementsByTagName('h3').item(0).innerText;

    var hdd_price = parent.document.getElementById("hdd_price");
    hdd_price.innerText = price;

    var Name = parent.document.getElementById('hdd_txt');
    Name.innerText = name;

    var Src = parent.document.getElementById('hdd_img');
    Src.src = src;

    parent.calc_sum();

    parent.closeModal();
}
$(function () {
    searchWord = function(){
      var   search_capacityText = $('#hdd_capacity_value').val(),
            search_cashText = $('#hdd_cash_value').val(),
            search_low_price = $('#hdd_low_price').val(),
            search_high_price = $('#hdd_high_price').val(),
            targetText,
            targetPrice;
      search_low_price = parseInt(search_low_price, 10);
      search_high_price = parseInt(search_high_price, 10);
      const words = search_capacityText.split(',');
            
            
      $('.price').each(function(element){
        targetPrice = parseInt($(this).text().replace('¥', ''), 10);
        
        if (isNaN(search_low_price) == false){
          if (isNaN(search_high_price) == false){
            if (targetPrice >= search_low_price && targetPrice <= search_high_price) {
              $(this).parent().parent().parent().removeClass('hidden');
            } else {
              $(this).parent().parent().parent().addClass('hidden');
            }
          } else {
            if (targetPrice >= search_low_price){
              $(this).parent().parent().parent().removeClass('hidden');
            } else {
              $(this).parent().parent().parent().addClass('hidden');
            }
          }
        } else if (isNaN(search_high_price) == false) {
          if (targetPrice <= search_high_price){
            $(this).parent().parent().parent().removeClass('hidden');
          } else {
            $(this).parent().parent().parent().addClass('hidden');
          }
        } else {
          $(this).parent().parent().parent().removeClass('hidden');
        };

      });
      $('.card').each(function(element){
        targetText = $(this).text();

        // 検索対象となるリストに入力された文字列が存在するかどうかを判断
        if (targetText.indexOf(search_cashText) != -1) {
          if (targetText.indexOf(words[0]) != -1 || targetText.indexOf(words[1]) != -1|| targetText.indexOf(search_capacityText) != -1) {
                ; //  何もしない
          } else {
            $(this).parent().addClass('hidden');
          }
        } else {
          $(this).parent().addClass('hidden');
        }
      });
      height_repair();
    };
    // searchWordの実行
    $('#Search1').on('change', searchWord);
    $('#Search2').on('change', searchWord);
});