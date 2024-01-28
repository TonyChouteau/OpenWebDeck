class Session:
    def __init__(self, uuid, websocket):
        self.uuid = uuid
        self.client_websocket = websocket
        self.web_websockets = []

    # Web websocket handlers
    def add_web_websocket(self, websocket):
        self.web_websockets.append(websocket)

    def get_web_websockets(self):
        return self.web_websockets

    def set_web_websockets(self, _web_websockets):
        self.web_websockets = _web_websockets

