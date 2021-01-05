var ws = new WebSocket("ws://127.0.0.1:5678/")
ws.onmessage = function (event) {
    var objDiv = document.getElementById("message_window"),
        messages = document.getElementById('message_window'),
        message = document.createElement('div'),
        content = document.createTextNode(event.data),
        scroll = (objDiv.scrollHeight - objDiv.scrollTop - objDiv.offsetHeight) < 30;
        
    message.innerHTML = event.data;
    messages.appendChild(message);
    if (scroll === true)
    {
        objDiv.scrollTop = objDiv.scrollHeight;
    }
};

document.getElementById("message_send").onclick = function (event) {
    var mb = document.getElementById("message_box");
    ws.send(mb.value);
    mb.value = "";
    var objDiv = document.getElementById("message_window");
    objDiv.scrollTop = objDiv.scrollHeight;
};

document.getElementById("message_box").addEventListener("keyup", function (event) {
    var key = event.key || event.keyCode;
    if (key === 'Enter' || key === 13) {
        event.preventDefault();
        document.getElementById("message_send").click();
    }
});
