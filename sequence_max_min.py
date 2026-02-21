n = int(input('How many people would you like to verify? '))
weights = []
def ordinal(k):
    if 10 <= k % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(k % 10, "th")
    return f"{k}{suffix}"

for i in range(1, n+1):
    weight_information = float(input(f"What's the weight of the {ordinal(i)} person? "))
    weights.append(weight_information)

max_weight = max(weights)
min_weight = min(weights)
print(f'Maximum weight: {max_weight} kg')
print(f'Minimum weight: {min_weight} kg')
