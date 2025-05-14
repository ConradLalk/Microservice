import json
import os
import time


def sort_difficulty(difficulty, titles, lst):
    temp = []
    for item in lst:
        if item[1] == difficulty:
            temp.append(item)
    speed_sorted = sorted(temp, key=lambda y: y[2])
    sorted_difficulty = [titles] + speed_sorted
    with open('leaderboard.json', 'w', encoding='utf-8') as x:
        json.dump(sorted_difficulty, x, ensure_ascii=False, indent=2)
        print('added')


while True:

    time.sleep(1)
    sorted_leaderboard = None

    with open('leaderboard.json', 'r', encoding='utf-8') as f:

        if os.path.getsize('leaderboard.json') == 0:
            continue
        data = json.load(f)

        # sort by name
        if data[0][0] == '0':
            var = data.pop(0)
            header, *rows = data
            rows_sorted = sorted(rows, key=lambda x: x[0])
            sorted_leaderboard = [header] + rows_sorted
            with open('leaderboard.json', 'w', encoding='utf-8') as file:
                json.dump(sorted_leaderboard, file, ensure_ascii=False, indent=2)
                print('added')

        # sort by speed
        if data[0][0] == '1':
            var = data.pop(0)
            header, *rows = data
            rows_sorted = sorted(rows, key=lambda x: x[2])
            sorted_leaderboard = [header] + rows_sorted
            with open('leaderboard.json', 'w', encoding='utf-8') as file:
                json.dump(sorted_leaderboard, file, ensure_ascii=False, indent=2)
                print('added')

        # sort by difficulty: Easy
        if data[0][0] == '2':
            var = data.pop(0)
            header, *rows = data
            sort_difficulty('Easy', header, rows)

        # sort by difficulty: Medium
        if data[0][0] == '3':
            var = data.pop(0)
            header, *rows = data
            sort_difficulty('Medium', header, rows)

        # sort by difficulty: Hard
        if data[0][0] == '4':
            var = data.pop(0)
            header, *rows = data
            sort_difficulty('Hard', header, rows)

        else:
            pass
