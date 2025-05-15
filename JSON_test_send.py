import json
import os
import time
from tabulate import tabulate

leaderboard = [
    ['Name', 'Difficulty', 'Time'],
    ['MDD', 'Hard', 600],
    ['MD2', 'Easy', 60],
    ['MD3', 'Medium', 6000],
    ['MDD', 'Hard', 600],
    ['MD2', 'Hard', 60],
    ['MD3', 'Easy', 6000],
    ['MDD', 'Medium', 600],
    ['MD2', 'Easy', 60],
    ['MD3', 'Hard', 6000],
]

while True:

    user_input = input("0 - to sort by name\n1 - to sort by time\n2 - to show easy completions\n"
                       "3 - to show medium completions\n4 - to show hard completions\n5 - to cancel\ninput: ")
    if user_input in ('0', '1', '2', '3', '4'):
        leaderboard.insert(0, [user_input])

        with open('leaderboard.json', 'w') as f:
            json.dump(leaderboard, f, ensure_ascii=False, indent=2)

        leaderboard.pop(0)

        while True:
            if os.path.getsize('leaderboard.json') > 0:
                time.sleep(1)  # added to prevent program crashes
                with open('leaderboard.json', 'r') as f:
                    data = json.load(f)
                    if data[0][0] == 'Name':
                        break

        print('\n' + tabulate(data, headers='firstrow', tablefmt='fancy_grid') + '\n')

    elif user_input == '5':
        break

    else:
        print("unknown option")
