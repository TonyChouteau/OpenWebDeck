

$(document).ready(_ => {
    let socket;
    let uuid;

    const onSocketOpen = _ => {
        socket.addEventListener("message", event => {
            if (event.data.length === 0) {
                console.log("/");
                return
            }
            let data;
            try {
                data = JSON.parse(event.data);
                console.log(data);
            } catch (e) {
                console.log("Data is not json");
            }
            if (data) {
                if (data.message_id === "config") {
                    displayConfig(data.list, (id, value) => {
                        socket.send(JSON.stringify({
                            uuid: uuid,
                            message_id: "web_message",
                            id: id,
                            value: value
                        }));
                    });
                } else if (data.message_id === "client_message") {
                    console.log("Output", data);
                    updateConfig(data);
                }
            }
        })

        displayLogin(_uuid => {
            uuid = _uuid
            socket.send(JSON.stringify({
                message_id: "web_connect",
                uuid: _uuid
            }));
        });
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