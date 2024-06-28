count_symbols = {}

text = input()

for ch in text:
    if ch not in count_symbols:
        count_symbols[ch] = 0

    count_symbols[ch] += 1

for symbol, count in sorted(count_symbols.items()):
    print(f'{symbol}: {count} time/s')
