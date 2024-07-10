from random import random
from time import sleep, time
from os import system
import asyncio

# coroutine to execute in a new task
async def task_coro(menu):
    # generate a random value between 0 and 1 and plus 1
    value = random() + 1

    print(f"Microwave {menu} cooking {value} second")

    # block for a moment
    await asyncio.sleep(value)

    # report the value
    print(f"Microwave {menu} finish")

    return value

# main coroutine
async def main():
    system("cls")

    # create many tasks
    Menus = [asyncio.create_task(task_coro("Rice"), name = "Rice"),
             asyncio.create_task(task_coro("Noodle"), name = "Noodle"),
             asyncio.create_task(task_coro("Curry"), name = "Curry")]

    # wait for first tasks to complete
    done, pending = await asyncio.wait(Menus, return_when = asyncio.FIRST_COMPLETED)

    # get the first task to complete
    print(f"\nTask Complete: {len(done)}")

    complete_menu = done.pop()

    print(f" - {complete_menu.get_name()} is complete in {complete_menu.result()} second.")
    print(f"Task Uncomplete: {len(pending)}")
    for uncomplete_menu in pending:
        print(f" - {uncomplete_menu.get_name()} is uncomplete")
   

# start the asyncio program
asyncio.run(main())