if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    winner = float('-inf')
    runnerup = float('inf')
    for i in range(0, n):
        if scores[i] > winner:
            runnerup = winner
            winner = scores[i]
        elif scores[i] > runnerup and winner != scores[i]:
            runnerup = scores[i]
    print(runnerup)
