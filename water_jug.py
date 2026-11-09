from collections import deque
from math import gcd

def water_jug(a, b, target):
    if target == 0:
        print("Step 0: Both jugs are empty")
        print("Answer: Target achieved")
        return

    if target > max(a, b) or target % gcd(a, b) != 0:
        print("Solution not possible")
        return

    start = (0, 0)
    queue = deque([start])
    parent = {start: None}
    action = {start: "Start"}

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            goal = (x, y)
            break

        t1 = min(x, b - y)
        t2 = min(y, a - x)

        moves = [
            ((a, y), "Fill Jug A"),
            ((x, b), "Fill Jug B"),
            ((0, y), "Empty Jug A"),
            ((x, 0), "Empty Jug B"),
            ((x-t1, y+t1), "Pour A to B"),
            ((x+t2, y-t2), "Pour B to A")
        ]

        for state, move in moves:
            if state not in parent:
                parent[state] = (x, y)
                action[state] = move
                queue.append(state)
    else:
        print("No solution found")
        return

    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for i, state in enumerate(path):
        print(f"Step {i}: {action[state]} -> A={state[0]}, B={state[1]}")

    print("Answer:", goal)
    print("Total moves:", len(path) - 1)


a = int(input("Enter Jug A capacity: "))
b = int(input("Enter Jug B capacity: "))
target = int(input("Enter target quantity: "))

if a <= 0 or b <= 0 or target < 0:
    print("Enter positive capacities and a non-negative target")
else:
    water_jug(a, b, target)