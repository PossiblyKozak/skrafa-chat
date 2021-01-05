#!/usr/bin/env python

# WS server example

import asyncio
import websockets

sockets = set()

async def send(websocket, msg):
    for w in sockets:
        if w != websocket:
            await w.send(msg)

async def hello(websocket, path):
    sockets.add(websocket)
    while True:
        msg = await websocket.recv()
        await send(websocket, msg)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()