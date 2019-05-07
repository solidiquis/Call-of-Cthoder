var imagewrap = document.querySelectorAll('.imagewrap img')
var aligner = document.querySelectorAll('.aligner')

for (let i = 0; i < aligner.length; i++){
  (function(i){
    aligner[i].addEventListener('mouseover', function(){
      imagewrap[i].classList.add('imgfade')
    });
  }(i));
}

for (let i = 0; i < aligner.length; i ++){
  (function(i){
    aligner[i].addEventListener('mouseout', function(){
      imagewrap[i].classList.remove('imgfade')
    });
  }(i));
}
