# WS server example
import asyncio
import websockets
import time

async def hello(websocket, path):
    print("websocket requested")
    print("websocket path      :", path)
    cc=0
    while True:
        incoming = await websocket.recv()
        print("got", incoming, cc)
        await websocket.send("take back your " + incoming)
        cc += 1
        
start_server = websockets.serve(hello, 'localhost', 5001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
