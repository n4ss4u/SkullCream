def compare_pattern(email_pattern, generated_patterns):
    email_local, email_service = email_pattern.lower().split("@")
    valid_patterns = []

    for pattern in generated_patterns:
        pattern = pattern.lower()

        if len(pattern) != len(email_local):
            continue

        if pattern[0] == email_local[0] and pattern[-1] == email_local[-1]:
            valid_patterns.append(pattern + "@" + email_service)

    return valid_patterns