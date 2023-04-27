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

function setCookie(cookieName, cookieValue, exdays) {
    const date = new Date();
    date.setTime(date.getTime() + (exdays * 24 * 60 * 60 *1000));
    let expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}

const userId = getCookie('user_id');
console.log(userId);

let usernameSpan = document.getElementById('username');

let logoutBtn = document.getElementById('logout');
logoutBtn.addEventListener('click', logout);

let user = null;

async function getUser() {
    const response = await fetch(`https://642ed5068ca0fe3352da117f.mockapi.io/users/${userId}`);
    user = await response.json();
    usernameSpan.innerHTML = user.username;
    return user;
}

function logout() {
    setCookie('user_id', user._id, -1);
    window.location = 'http://127.0.0.1:5500/login.html';
}

window.addEventListener('DOMContentLoaded', checkAuth);

function checkAuth() {
    if (getCookie("user_id") === "") {
        window.location = 'http://127.0.0.1:5500/login.html';
    }
    else {
        getUser();
    }
}