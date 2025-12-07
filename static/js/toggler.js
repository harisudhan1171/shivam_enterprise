function closetoggle(){
 document.getElementById('sidebar').style.marginLeft='-320px';
 document.getElementById('open').style.display='flex';
}

function opentoggle(){
    const opener = document.getElementById('open');
    opener.addEventListener("click", () =>{
        document.getElementById('sidebar').style.marginLeft=0;
        document.getElementById('open').style.display='none';
    });
}

//questkon answer popup//

document.querySelectorAll('.faq-question').forEach(question => {
  question.addEventListener('click', () => {
    const item = question.parentElement;
    item.classList.toggle('active');
  });
});
 