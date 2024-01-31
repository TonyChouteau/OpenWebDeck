from handlers.Base import Base


# Handler example
class HandlerPong(Base):
    def __init__(self):
        super().__init__("print", None)

    def get_config(self):
        base_config = super().get_config()
        return {
            "id": base_config.get("id"),
            "value": base_config.get("value"),
            "name": "Ping/Pong",
            "sub-cells": [{
                "name": "Ping",
                "value": "ping"
            }, {
                "name": "Pong",
                "value": "pong"
            }]
        }

    def execute(self, value):
        super().execute(value)
        if self.value == "ping":
            return "pong"
        elif self.value == "pong":
            return "ping"