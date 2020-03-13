window.onscroll = function showHeader(){

    var header = document.querySelector('.border');

    if(window.pageYOffset > 120){
        header.classList.add('header-fixed');
    }else{
        header.classList.remove('header-fixed');
    }

}
