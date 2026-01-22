def fractional_knapsack(items, capacity):
    # Sort by value/weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    current_weight = 0

    for value, weight in items:
        if current_weight + weight <= capacity:
            current_weight += weight
            total_value += value
        else:
            remaining = capacity - current_weight
            total_value += (value / weight) * remaining
            break

    return total_value


T=int(input())

for _ in range(T):
    N, W = map(int, input().split())
    items = []

    for _ in range(N):
        V, Wi = map(int, input().split())
        items.append((V, Wi))

    result = fractional_knapsack(items, W)
    print(f"{result:.6f}")
