let regBtn = document.getElementById('log-btn');
regBtn.addEventListener('click', login);

function setCookie(cookieName, cookieValue, exdays) {
    const date = new Date();
    date.setTime(date.getTime() + (exdays * 24 * 60 * 60 *1000));
    let expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}

function getCookie(cookieName) {
    let name = cookieName + "=";
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) == " ") {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}



async function login(a) {
    a.preventDefault();
    let myUser = null;
    let form = document.forms.login;
    let username = form.elements.username.value;
    let password = form.elements.password.value;

    const response = await fetch('https://642ed5068ca0fe3352da117f.mockapi.io/users');
    const users = await response.json();

    let findUser = false;
    for (let user of users) {
        if (user.username === username && user.password === password) {
           myUser = user;
           findUser = true;
           break;
        }
    }
    if (findUser === false) {
        alert("Cannot find user");
    }
    setCookie('user_id', myUser._id, 30);
    window.location = 'http://127.0.0.1:5500/home.html';
}

window.addEventListener('DOMContentLoaded', checkAuth);

function checkAuth() {
    if (getCookie("user_id") !== "") {
        window.location = 'http://127.0.0.1:5500/home.html';
    }
}