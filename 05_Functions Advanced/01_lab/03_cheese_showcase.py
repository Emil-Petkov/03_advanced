def sorting_cheeses(**kwargs):
    result = ''
    cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), (kvp[0])))

    for cheese_name, quantity in cheeses:
        result += f'{cheese_name}\n'
        for q in sorted(quantity, reverse=True):
            result += f'{q}\n'

    return result


print(sorting_cheeses(
    Parmesan=[102, 120, 135],
    Camembert=[100, 100, 105, 500, 430],
    Mozzarella=[50, 125],
)
)
