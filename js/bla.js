
var button = document.getElementById("myButt")
button.addEventListener('click', myFunc , false);

function myFunc(){
    var myp = document.querySelector("p#data")

    const Http = new XMLHttpRequest();
    const url='http://127.0.0.1:5000/getData';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        var text = Http.responseText;
        myp.innerText = text;
    }
}

