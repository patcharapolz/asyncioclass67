from random import random
from time import sleep, time
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # create menu
    food = ["Rice", "Noodle", "Curry"]

    # generate a random value between 0 and 1
    value = random() + 1

    # block for a moment
    await asyncio.sleep(value)

    # report the value
    print(f">task {food[arg]} done with {value:.2f} sec")

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(3)]

    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when = asyncio.FIRST_COMPLETED)

    # report results
    print("Done")

    # get the first task to complete
        # first = done

# start the asyncio program
asyncio.run(main())