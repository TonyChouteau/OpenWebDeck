import asyncio
import websocket
from websocket.server import serve
import json

from api.Context import Context

context = Context()


async def handler(websocket):
    try:
        async for message in websocket:
            await context.clear_clients()

            if len(message) > 0 and message[0] == "{":
                try:
                    data = json.loads(message)
                except:
                    continue

                message_id = data.get("message_id")
                if message_id == "client_init":
                    context.connect_client(data, websocket)
                elif message_id == "client_message":
                    context.send_to_web(data, websocket)

                elif message_id == "web_connect":
                    context.connect_web(data, websocket)
                elif message_id == "web_message":
                    context.send_to_client(data, websocket)

    except websockets.ConnectionClosed:
        pass


async def main():
    async with serve(handler, "localhost", 433):
        await asyncio.Future()  # run forever


asyncio.run(main())
