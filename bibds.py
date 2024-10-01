import json

from pycsp3 import *


def bibd(num_participants, block_size, lambd):
    clear()

    num_blocks = int(
        (lambd * num_participants * (num_participants - 1))
        / (block_size * (block_size - 1))
    )
    num_replicas = int((lambd * (num_participants - 1)) / (block_size - 1))

    # x[i][j] is the value of the matrix at row i and column j
    x = VarArray(size=[num_participants, num_blocks], dom={0, 1})

    satisfy(
        # constraints on rows
        [Sum(row) == num_replicas for row in x],
        # constraints on columns
        [Sum(col) == block_size for col in columns(x)],
        # scalar constraints with respect to lambda
        [row1 * row2 == lambd for row1, row2 in combinations(x, 2)],
        # Increasingly ordering both rows and columns  tag(symmetry-breaking)
        LexIncreasing(x, matrix=True),
    )

    if solve() is SAT:
        return values(columns(x))


with open("bibds.json", "a", encoding="utf-8") as f:
    f.write("[")
    for i in range(8, 101):
        if i % 4 in [0, 1]:
            result = bibd(i, 4, 3)
            json.dump({i: result}, f)
            f.write(",\n")
            f.flush()
    f.write("]")
