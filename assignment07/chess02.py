import asyncio
import time

async def chess(game):
    start_time = time.perf_counter()

    print(f"Game: {game+1}")

    for move in range(moves):
        print(f"Judit's move: {move+1}")
        time.sleep(judit_move)
        print(f"Opponent's move: {move+1}")
        await asyncio.sleep(opponent_move)

    return round(time.perf_counter() - start_time)

async def main():
    # create many coroutines
    coros = [chess(i) for i in range(total_opponent)]

    #run the tasks
    await asyncio.gather(*coros)



if __name__ == "__main__":
    judit_move = 0.1
    opponent_move = 0.5
    moves = 30
    total_opponent = 24

    start_time = time.perf_counter()

    asyncio.run(main())
    
    print(round(time.perf_counter() - start_time))