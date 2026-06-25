def compare_pattern(email_pattern, generated_patterns):
    email_pattern, email_service = email_pattern.lower().split("@")
    valid_patterns = []

    for pattern in generated_patterns:
        if len(pattern) != len(email_pattern):
            continue
        if pattern.startswith(email_pattern[0]) and pattern.endswith(email_pattern[-1]):
            valid_patterns.append(pattern + "@" + email_service)
    return valid_patterns