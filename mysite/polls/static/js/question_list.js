
var xmlhttp;

function sendRequest() {
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = onChange;
    xmlhttp.open("GET", "question-list-json/", true);
    xmlhttp.send();
}

function onChange() {
    if (xmlhttp.readyState!=4 || xmlhttp.status!=200) {
        return;
    }

    var items = JSON.parse(xmlhttp.responseText);

    var list = document.getElementById('question_list');
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }


    for (var pk in items) {
        var text = items[pk];
        var newItem = document.createElement("li");
        newItem.id = "question_"+pk;
        newItem.class = "question";
        newItem.innerHTML = "<a href=\"" + pk +"\">"
                            + text + "</a>";
        list.appendChild(newItem);
    }

    // document.getElementsByTagName('h1')[0].innerHTML=xmlhttp.responseText;

}

setInterval(sendRequest, 5000);