#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

USERS = set()

async def register(websocket):
    USERS.add(websocket)

async def unregister(websocket):
    USERS.remove(websocket)

async def notify_state(msg):
    if USERS:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(msg) for user in USERS])

async def time(websocket, path):
    await register(websocket)
    try:
        async for message in websocket:
            await notify_state(message)
    finally:
        await unregister(websocket)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()