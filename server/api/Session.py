import json


class Session:
    def __init__(self, uuid, websocket, config):
        self.uuid = uuid
        self.client_websocket = websocket
        self.config = config

        self.web_websockets = []

    # Client
    def get_client_websocket(self):
        return self.client_websocket

    # Config
    def get_str_config(self):
        return json.dumps(self.config)

    # Web websocket handlers
    def add_web_websocket(self, websocket):
        self.web_websockets.append(websocket)

    def get_web_websockets(self):
        return self.web_websockets

    def set_web_websockets(self, _web_websockets):
        self.web_websockets = _web_websockets
