import asyncio
import websockets
import json
import uuid

from handlers import handlers

UUID = uuid.uuid4()


async def process_message(websocket, message):
    if len(message) == 0 or message[0] != "{":
        return

    try:
        data = json.loads(message)
    except:
        await websocket.send(json.dumps({
            "id": None,
            "value": None,
            "error": "Data must be json"
        }))
        return

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


async def main():
    async for _websocket in websockets.connect("ws://localhost:433"):
        print("\nWaiting for the server...")
        await _websocket.send(json.dumps({
            "message_id": "client_init",
            "uuid": str(UUID)
        }))
        print("Connected to the server !\n")
        try:
            async for message in _websocket:
                await process_message(_websocket, message)

        except websockets.ConnectionClosed:
            continue

print(f"\nUUID : {UUID}\n")

asyncio.run(main())
