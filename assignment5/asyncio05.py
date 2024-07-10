from random import random
from time import sleep, time
from os import system
import asyncio

# coroutine to execute in a new task
async def rice():
    # generate a random value between 0 and 1
    value = random() + 1

    print(f">Menu Rice cooking {value} sec")

    # block for a moment
    await asyncio.sleep(value)

    # report the value
    print(f">Menu Rice finish")

async def noodle():
    # generate a random value between 0 and 1
    value = random() + 1

    print(f">Menu Noodle cooking {value} sec")

    # block for a moment
    await asyncio.sleep(value)

    # report the value
    print(f">Menu Noodle finish")

async def curry():
    # generate a random value between 0 and 1
    value = random() + 1

    print(f">Menu Curry cooking {value} sec")

    # block for a moment
    await asyncio.sleep(value)

    # report the value
    print(f">Menu Curry finish")

# main coroutine
async def main():
    system("cls")

    # create many tasks
    makeRice = asyncio.create_task(rice(), name= "Rice")
    makeNoodle = asyncio.create_task(noodle(), name= "Noodle")
    makeCurry = asyncio.create_task(curry(), name= "Curry")

    Menus = [makeRice, makeNoodle, makeCurry]

    # wait for all tasks to complete
    done, pending = await asyncio.wait(Menus, return_when = asyncio.FIRST_COMPLETED)

    # get the first task to complete
    print(f"\nTask Complete: {len(done)}")

    first = done.pop()

    print(f"\t{first.get_name()} is complete.")
    print(f"\nTask Uncomplete: {len(pending)}")
   

# start the asyncio program
asyncio.run(main())