#!/usr/bin/env python3
N, Q = [ int(num) for num in input().split(" ") ]

last_answer = 0


def get_seq(seqs, x, last_answer, N):
    return seqs[(x ^ last_answer) % N]

seqs = []
# initialise empty sequences
for i in range(N):
    seqs.append([])

for i in range(Q):
    q, x, y = [ int(num) for num in input().split(" ") ]
    target_seq = get_seq(seqs, x, last_answer, N)
    if q == 1:
        target_seq.append(y)
    elif q == 2:
        last_answer = target_seq[y % len(target_seq)]
        print(last_answer)

