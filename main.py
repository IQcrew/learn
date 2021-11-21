rozvrh = lambda x = input("zadaj hodinu: ") : "ANO" if x.upper() in {"ANJ", "DEJ", "NEJ", "PRO", "COW"} else "NIE"
print(rozvrh())