# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee(): # 1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffe: waiting...")
    await asyncio.sleep(5) # 2: pause, another tasks can be run
    print("coffe: ready")

async def fry_eggs(): # 1
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) # 2: pause, another tasks can be run
    print("eggs: ready")

async def main(): # 1
    start = time()
    makeCoffe = asyncio.create_task(make_coffee()) # create task
    fryEggs = asyncio.create_task(fry_eggs()) # create task

    await makeCoffe
    await fryEggs
    
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main()) # run top-level function concurrently