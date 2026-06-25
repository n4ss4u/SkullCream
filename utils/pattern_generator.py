from itertools import permutations

def generate_pattern(first_name, middle_name, last_name_1, last_name_2, birthday_day, birthday_month, birthday_year):

    data = [first_name, middle_name, last_name_1, last_name_2, birthday_day, birthday_month, birthday_year]

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