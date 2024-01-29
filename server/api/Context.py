from api.Session import Session


class Context:
    def __init__(self):
        self.clients = {}
        self.web = {}

    # Client
    async def clear_clients(self):
        try:
            client_to_delete = []
            for client_id in self.clients:
                session = self.clients[client_id]
                try:
                    await session.client_websocket.send("")
                    # Web
                    web_websockets = session.get_web_websockets()
                    web_websockets_after = []
                    for web_websocket in web_websockets:
                        try:
                            await web_websocket.send("")
                            web_websockets_after.append(web_websocket)
                        except:
                            pass
                    session.set_web_websockets(web_websockets_after)

                    if len(web_websockets) != 0:
                        print(len(session.get_web_websockets()))
                except:
                    client_to_delete.append(session.uuid)

            for uuid in client_to_delete:
                del self.clients[uuid]
        except:
            pass

    def connect_client(self, data, websocket):
        uuid = data.get("uuid")
        if self.clients.get(uuid):
            print(f"[CONTEXT] Message from client, uuid: {uuid}")
            session = self.clients[uuid]
            return session
        else:
            session = Session(uuid, websocket)
            self.clients[uuid] = session

            print(f"[CONTEXT] New client : {uuid} ({len(self.clients)} clients connected)")
            return session

    def send_to_web(self, data, websocket):
        session = self.connect_client(data, websocket)
        for websocket in session.get_web_websockets():
            try:
                websocket.send(data)
            except:
                pass

    # Web
    def connect_web(self, data, websocket):
        uuid = data.get("uuid")
        if self.clients.get(uuid):
            print(f"[CONTEXT] Message from web, uuid: {uuid}")
            session = self.clients[uuid]
            if websocket in session.web_websockets:
                return session
            else:
                session.add_web_websocket(websocket)
            print(len(session.get_web_websockets()))
        else:
            return None

    def send_to_client(self, data, websocket):
        session = self.connect_client(data, websocket)
        if session:
            try:
                session.get_client_websocket().send(data)
            except:
                pass