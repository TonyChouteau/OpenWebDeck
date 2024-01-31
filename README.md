
# OpenWebDeck

## Project Description

Online Python Script Executor is like an online version of a stream deck, enabling the execution of Python scripts remotely on a client machine from a web application. Users can add as many scripts (handlers) as desired to the client. The client generates a UUID necessary for the web app to connect.

## Operation

+---------------------+      +---------------------+      +---------------------+
|     Web App         |      |       Server        |      |       Client        |
|                     |      |                     1<-----+   Send the handler  |
|   Request UUID      +----->2    Receive UUID     |      |       config        |
| if UUID get config  3<-----+  and Handler Config |      |                     |
|                     |      |    from Client      |      |                     |
|   Display Handlers  |      |                     |      |                     |
|     as Buttons      |      |                     |      |                     |
|      onClick        +----->4   proxy to client   +----->5       Execute       |
|   display output    7<-----+   proxy to client   6<-----+    return output    |
|                     |      |                     |      |                     |
+---------------------+      +---------------------+      +---------------------+


## Personalizing the Client

Personalize the client by creating new scripts inheriting from the `client/handlers/Base.py` class with the following methods:

- `.get_config()`: Return a configuration (JSON) with the "id", default "value", and list of possible values, "sub-cells" ("name" and "value") of the handler.
- `.execute(value)`: The function that modifies the handler's value, executes the script/action, and returns the value after execution.

The `client/handlers/handlers.py` file contains a list called "config" of instances of all handlers. Simply add your handlers to include them in the web app.

For example, imagine launching a script and receiving a value "OK" or "ERROR."

Check the example of the already defined handler: `client/handlers/HandlerPong.py`. This handler, for example purposes, allows sending two values from the web app: ping or pong. 
The execution of the handler modifies the value on the client with the value sent by the web app, displays it in the client's console, and returns the opposite value.

# Installation

## Install the Server (Locally or on a Distant Server)

Install Python 3.8+ and pip
```bash
python3 -m pip install flask flask_session websockets asyncio
```
Run the server:
```bash
python3 server/server.py # Webapp
python3 server/websocket.py # Server
```

## Install the Client

Add new handlers in `client/handlers/` and edit the config list in `handlers.py` to add the new handler.

Install Python 3.8+ and pip
```bash
python3 -m pip install websockets asyncio uuid
```
Run the client:
```bash
python3 client.py
```

## Using the Web App

On the web app, enter the UUID generated by the client, then click on the desired buttons to perform actions on the client.

# License 

Apache2
