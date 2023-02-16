i = 2

while i <= 70:
    i = i +2
    print(i)

years = [1998, 1999, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
i = 0

while i < len(years):
    if years[i] % 4 == 0:
        print(years[i], "is leap Year")
    i = i+1
    