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

    output_value = None
    for handler in handlers.handler_list:
        if handler.id == data.get("id"):
            print("Handler : " + handler.id)
            output_value = handler.execute(data.get("value"))

    print("\n")
    if output_value is not None:
        await websocket.send(json.dumps({
            "uuid": str(UUID),
            "message_id": "client_message",
            "data": data,
            "id": data.get("id"),
            "value": output_value
        }))
    else:
        await websocket.send(json.dumps({
            "uuid": str(UUID),
            "message_id": "client_message",
            "data": data,
            "id": None,
            "value": None,
            "error": "No handler for this id or the execution returned nothing"
        }))


async def main():
    async for _websocket in websockets.connect("ws://localhost:433"):
        config = []
        for handler in handlers.handler_list:
            config.append(handler.get_config())

        print("Waiting for the server...")
        await _websocket.send(json.dumps({
            "message_id": "client_init",
            "uuid": str(UUID),
            "config": {
                "message_id": "config",
                "list": config
            }
        }))
        print("Connected to the server !\n")
        print(f"\nUUID : {UUID}\n")
        try:
            async for message in _websocket:
                await process_message(_websocket, message)

        except websockets.ConnectionClosed:
            continue

asyncio.run(main())
