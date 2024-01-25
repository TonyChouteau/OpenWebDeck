import asyncio
from websockets.server import serve
import json

from handlers import handlers


async def handler(websocket):
    async for message in websocket:
        if message[0] == "{":
            data = json.loads(message)
            print("Message received :")
            print(data, end="\n\n")

            handler_value = None
            for handler in handlers.config:
                if handler.id == data.get("id"):
                    print("Handler : " + handler.id)
                    handler.set_value(data.get("value"))
                    handler.execute()
                    handler_value = handler.get_value()

            print("\n")
            if handler_value is not None:
                await websocket.send(json.dumps({
                    "data": data,
                    "id": data.get("id"),
                    "value": handler_value
                }))
            else:
                await websocket.send(json.dumps({
                    "id": None,
                    "value": None,
                    "error": "No handler for this id"
                }))
        else:
            print("Error, message is not JSON", end="\n\n")


async def main():
    async with serve(handler, "localhost", 433):
        await asyncio.Future()  # run forever


asyncio.run(main())
