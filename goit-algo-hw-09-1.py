import timeit


coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(summ: int):
    count_cons = {}
    for coin in coins:
        count = summ // coin
        if count > 0:
            count_cons[coin] = count
        summ = summ - coin*count
    return count_cons

def find_min_coins(summ: int):
    # тут індекс - це сума
    min_coin_required = [0] + [float('inf')] * summ # мінімальна кількість монет
    last_coin_used = [0] * (summ + 1) # остання монета для цієї суми
    
    for s in range(1,summ+1): # s - це сума
        for coin in coins:
            if s >= coin and min_coin_required[s - coin] + 1 < min_coin_required[s]:
                min_coin_required[s] = min_coin_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_summ = summ
    while current_summ > 0:
        coin = last_coin_used[current_summ]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_summ = current_summ - coin
    
    return count_coins





if __name__ == '__main__':
    result1 = find_coins_greedy(98878)
    time_greedy = timeit.timeit('find_coins_greedy(98878)', globals=globals(), number=100)
    result2 = find_min_coins(98878)
    time_dymanic = timeit.timeit('find_min_coins(98878)', globals=globals(), number=100)
    print(result1)
    print("Время выполнения find_coins_greedy:", time_greedy)
    print(' ')
    print(result2)
    print("Время выполнения find_min_coins:", time_dymanic)