let image= document.getElementById('image'); // 1 element
let addBtn = document.getElementsByTagName('button')[0]; // collection [...]
let ClrBtn = document.getElementById('clr');

addBtn.addEventListener("click", add);
ClrBtn.addEventListener("click", del);
// addBtn.removeEventListener("click", add);

function add() {
    let imgg = document.createElement('img');
    imgg.src = "https://img.buzzfeed.com/buzzfeed-static/static/2018-10/2/18/campaign_images/buzzfeed-prod-web-06/15-of-the-weirdest-and-darkest-stock-photos-that--2-21628-1538520564-0_dblbig.jpg?resize=1200:*";
    let delBtn = document.createElement('button');
    delBtn.addEventListener("click", del);
    delBtn.innerHTML = 'Delete';
    document.querySelector('.container').appendChild(imgg);
    document.querySelector('.container').appendChild(delBtn);
}

function del() {
    this.parentNode.remove();
}