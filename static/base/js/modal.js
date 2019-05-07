document.getElementsByClassName('sign-up')[0].addEventListener('click',
function(){
    document.querySelector('.signup').style.display = 'flex';
  });

document.getElementsByClassName('close')[0].addEventListener('click',
function(){
    document.querySelector('.signup').style.display = 'none';
});

document.getElementsByClassName('log-in')[0].addEventListener('click',
function(){
    document.querySelector('.login').style.display = 'flex';
  });

document.getElementsByClassName('close')[1].addEventListener('click',
function(){
    document.querySelector('.login').style.display = 'none'
});

document.getElementsByClassName('sign-up-btn')[0].addEventListener('click',
function(){
    document.querySelector('.signup').style.display = 'flex';
  });

document.getElementsByClassName('log-in-btn')[0].addEventListener('click',
function(){
    document.querySelector('.login').style.display = 'flex';
  });

$(document).ready(function(){
  $('.vote-unauth').click(function(e){
    $('.signup').css('display', 'flex')
  })
});
