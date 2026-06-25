# Email Pattern Guesser & Validator

## Overview

This project is a script designed to reconstruct and validate possible email addresses based on partially masked email patterns and additional personal information.

When users request a password reset, many services display a censored version of the email address (e.g., `j******2@gmail.com`). This tool attempts to generate possible full email candidates using known personal data and then verifies which ones are valid.

---

## Images

![Screenshot 1](https://raw.githubusercontent.com/n4ss4u/SkullCream/refs/heads/main/media/screen1.png)

--- 

![Screenshot 2](https://raw.githubusercontent.com/n4ss4u/SkullCream/refs/heads/main/media/screen2.png)

--- 

## How It Works

The script operates in two main stages:

### 1. Pattern Generation

Given a partially masked email (e.g., `j******2@gmail.com`) and optional personal data such as:

- First name
- Middle name
- Last name
- Date of birth
- Known aliases or variations

The system generates possible email combinations by:
- Matching the visible prefix and suffix of the masked email
- Expanding possible name-based permutations
- Applying common email formatting patterns (e.g., `john.doe`, `jdoe`, `john123`, etc.)

---

### 2. Email Verification

After generating candidate emails, the script checks which ones are valid by querying a verification method or endpoint.

The validation step filters out invalid candidates and returns only those that are likely active or registered.

---

## Input Example

Masked email: j******2@gmail.com

Personal data:
- First name: John
- Last name: Doe
- Birth year: 1992

---

## Output Example

Possible matches:
- john.doe2@gmail.com
- jdoe92@gmail.com
- john2@gmail.com

---

## Getting Started
- ```git clone https://github.com/n4ss4u/SkullCream```
- ```cd SkullCream```
- ```pip install -r requirements.txt```
- ```python3 skullcream.py```

---

## Disclaimer

> [!WARNING]
> This project is provided for educational and research purposes only. The author is not responsible for any misuse of this tool. Users must comply with all applicable laws and service terms when using this software.

