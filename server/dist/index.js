

$(document).ready(_ => {
    let socket;

    const onSocketOpen = _ => {
        socket.addEventListener("message", event => {
            if (event.data.length === 0) {
                console.log("/");
                return
            }
            try {
                JSON.parse(event.data);
            } catch (e) {
                console.log("Data is not json");
            }
        })
        console.log(socket);
        socket.send(JSON.stringify({
            "message_id": "web_connect",
            "value": "dev"
        }));
    }
    const startWebsocket = _ => {
        setTimeout(_ => {
            socket = new WebSocket("ws://localhost:433");
            socket.onopen = onSocketOpen;
            socket.onerror = startWebsocket;
        }, 1000);
    };

    startWebsocket();
});