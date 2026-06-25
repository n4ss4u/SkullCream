from itertools import permutations

def generate_pattern(first_name, middle_name, last_name_1, last_name_2, birthday_day, birthday_month, birthday_year):
    birthday_year_last_two = None
    birthday_month_with0 = None
    birthday_day_with0 = None

    if birthday_year and len(birthday_year) >= 2:
        birthday_year_last_two = birthday_year[-2:]

    if birthday_month and len(birthday_month) == 1:
        birthday_month_with0 = f"0{birthday_month}"
    
    if birthday_day and len(birthday_day) == 1:
        birthday_day_with0 = f"0{birthday_day}"

    data = [first_name, middle_name, last_name_1, last_name_2, birthday_day_with0, birthday_month_with0, birthday_year, birthday_year_last_two]

    data = [str(x) for x in data if x]

    patterns = []
    seen = set()

    for r in range(1, len(data) + 1):
        for p in permutations(data, r):
            pattern = "".join(p)

            if pattern not in seen:
                seen.add(pattern)
                patterns.append(pattern)

    return patterns