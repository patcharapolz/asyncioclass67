# example of creating an event loop
import asyncio

async def some_async_task():
    print("Sleeping for 1 seconds")
    await asyncio.sleep(1)
    print(1)

# Get the current event loop.
loop = asyncio.new_event_loop()

# Run until the coroutine is completed
loop.run_until_complete(some_async_task())