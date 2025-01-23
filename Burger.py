recipe = input()
nb, ns, nc = list(map(int, input().split()))
pb, ps, pc = list(map(int, input().split()))
r = int(input().strip())  # Input for the budget

def can_make_hamburgers(x, recipe_count, available, prices, budget):
    needed_b = max(0, recipe_count['B'] * x - available['B'])
    needed_s = max(0, recipe_count['S'] * x - available['S'])
    needed_c = max(0, recipe_count['C'] * x - available['C'])
    
    total_cost = (needed_b * prices['B']) + (needed_s * prices['S']) + (needed_c * prices['C'])
    
    return total_cost <= budget

def max_hamburgers(recipe, available, prices, budget):
    recipe_count = {'B': 0, 'S': 0, 'C': 0}
    for char in recipe:
        recipe_count[char] += 1
    
    low, high = 0, 10**13
    while low < high:
        mid = (low + high + 1) // 2
        if can_make_hamburgers(mid, recipe_count, available, prices, budget):
            low = mid
        else:
            high = mid - 1
    
    return low

available = {'B': nb, 'S': ns, 'C': nc}
prices = {'B': pb, 'S': ps, 'C': pc}

result = max_hamburgers(recipe, available, prices, r)
print(result)
