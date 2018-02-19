#!/usr/bin/env python3
def count_occurences(q, strs):
    count = 0
    for s in strs:
        if s == q:
            count += 1

    return count

N = int(input())
strs = [str(input()) for i in range(N)]
Q = int(input())
queries = [str(input()) for q in range(Q)]

for q in queries:
    print(count_occurences(q, strs))





