import time

def chess(game):
    start_time = time.perf_counter()

    print(f"Game: {game+1}")

    for move in range(moves):
        print(f"Judit's move: {move+1}")
        print(f"Opponent's move: {move+1}")
        time.sleep(judit_move + opponent_move)

    return round(time.perf_counter() - start_time)


if __name__ == "__main__":
    judit_move = 0.1
    opponent_move = 0.5
    moves = 30
    total_opponent = 3

    start_time = time.perf_counter()

    for game in range(total_opponent):
        chess(game)

    print(round(time.perf_counter() - start_time))
