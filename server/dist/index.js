

$(document).ready(_ => {
    let socket;

    const onSocketOpen = _ => {
        socket.addEventListener("message", event => {
            console.log(event.data);
        })
        socket.send("not handled");
        socket.send(JSON.stringify({
            "id": "switch_branch",
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