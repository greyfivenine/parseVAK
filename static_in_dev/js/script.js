window.onscroll = function showHeader(){

    var header = document.querySelector('.border');

    if(window.pageYOffset > 1){
        header.classList.add('header-fixed');
    }else{
        header.classList.remove('header-fixed');
    }

}
