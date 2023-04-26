from collections import defaultdict

def solution(kor, usa, incs):
    answer = 0

    country = {}
    for i in kor:
        country[i] = 0
    for i in usa:
        country[i] = 1
    combs = defaultdict(int)
    for stocks in incs:
        stocks = stocks.split()

        for i in range(len(stocks)):
            for j in range(i+1, len(stocks)):
                if country[stocks[i]] != country[stocks[j]]:
                    if country[stocks[i]] == 0:
                        combs[(stocks[i], stocks[j])] += 1
                    else:
                        combs[(stocks[j], stocks[i])] += 1

    if len(combs) == 0:
        return 0
    combs = sorted(combs.values(), reverse=True)

    return(combs[0])