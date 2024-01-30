import json
from api.Session import Session


class Context:
    def __init__(self):
        self.clients = {}
        self.web = {}

    # Clear client & web websockets when timeout
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

                except:
                    client_to_delete.append(session.uuid)

            for uuid in client_to_delete:
                del self.clients[uuid]
                print(f"[CONTEXT] Removing client, uuid: {uuid} ({len(self.clients)} clients connected)")
        except:
            pass

    # Connect client
    def connect_client(self, data, websocket):
        uuid = data.get("uuid")
        if self.clients.get(uuid):
            session = self.clients[uuid]
            return session
        else:
            session = Session(uuid, websocket, data.get("config"))
            self.clients[uuid] = session

            print(f"[CONTEXT] New client : {uuid} ({len(self.clients)} clients connected)")
            return session

    # Connect web
    async def connect_web(self, data, websocket):
        uuid = data.get("uuid")
        if self.clients.get(uuid):
            print(f"[CONTEXT] New web connected, uuid: {uuid}")
            session = self.clients[uuid]
            if websocket not in session.web_websockets:
                session.add_web_websocket(websocket)
                await websocket.send(session.get_str_config())
            return session
        else:
            return None

    # Client -> [Server] -> Web
    async def send_to_web(self, data, websocket):
        session = self.connect_client(data, websocket)
        print(f"[CONTEXT] Message from web")
        for websocket in session.get_web_websockets():
            try:
                data["uuid"] = "***"
                await websocket.send(json.dumps(data))
            except:
                pass

    # Web -> [Server] -> Client
    async def send_to_client(self, data, websocket):
        session = await self.connect_web(data, websocket)
        print(f"[CONTEXT] Message from client")
        if session:
            try:
                await session.get_client_websocket().send(json.dumps(data))
            except:
                pass