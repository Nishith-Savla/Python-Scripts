from typing import List


def calculate_total_weight_gain(pizza_weights: List):
    pizza_weights = sorted(pizza_weights)
    second_minimal_weights = [weight for index, weight in enumerate(
        pizza_weights) if (index - 1) % 4 == 0]
    return sum(second_minimal_weights)


if __name__ == "__main__":
    print(calculate_total_weight_gain([]))
