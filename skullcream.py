import colorama

from ui import banner
from utils.pattern_generator import generate_pattern
from utils.pattern_comparer import compare_pattern
from utils.verify_gmail import verify_gmail

data = {"email_pattern": "", "first_name": "", "middle_name": "", "last_name_1": "", "last_name_2": "", "birthday_day": "", "birthday_month": "", "birthday_year": ""}
check_exist_data = ""

def main_menu():
    banner()
    print("")
    for i, (key, value) in enumerate(data.items(), start=1):
        if value == "":
            check_exist_data = f"{colorama.Fore.RED}x{colorama.Fore.RESET}"
        else:
            check_exist_data = f"{colorama.Fore.GREEN}✓{colorama.Fore.WHITE} ({colorama.Fore.GREEN}{value}{colorama.Fore.WHITE}){colorama.Fore.RESET}"
            
        print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}0{i}{colorama.Fore.WHITE}]- {colorama.Fore.WHITE}{key.capitalize().replace("_", " ")} {check_exist_data}")
    
    print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}98{colorama.Fore.WHITE}]- {colorama.Fore.RESET}Reset")
    print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}99{colorama.Fore.WHITE}]- {colorama.Fore.RESET}Exit")
    option = input(f" {colorama.Fore.WHITE}└──> ({colorama.Fore.GREEN}type RUN to start{colorama.Fore.WHITE}): {colorama.Fore.RESET}")
    return option 

def runnig_info(patterns_amount, valid_patterns_amount, valid_patterns):
    banner()
    print("")
    print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}INFO{colorama.Fore.WHITE}]- {colorama.Fore.RESET}Total patterns generated: {colorama.Fore.GREEN}{patterns_amount}{colorama.Fore.RESET}")
    print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}INFO{colorama.Fore.WHITE}]- {colorama.Fore.RESET}Valid patterns found: {colorama.Fore.GREEN}{valid_patterns_amount}{colorama.Fore.RESET}")

    print("")

    for i in valid_patterns:
        if data["email_pattern"].split("@")[1] == "gmail.com":
            veryfied = verify_gmail(i)

            if veryfied:
                print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] {i} {colorama.Fore.GREEN}(exist){colorama.Fore.RESET}")
            else:
                print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}-{colorama.Fore.WHITE}] {i} {colorama.Fore.RED}(doesn't exist){colorama.Fore.RESET}")
        else:
            print(f" {colorama.Fore.WHITE}[{colorama.Fore.GREEN}*{colorama.Fore.WHITE}] {i} {colorama.Fore.YELLOW}(unknown){colorama.Fore.RESET}")

    input(f"\n {colorama.Fore.WHITE}[{colorama.Fore.GREEN}INFO{colorama.Fore.WHITE}]- {colorama.Fore.RESET}Report completed. Press ENTER to go back to main menu")

if __name__ == "__main__":
    while True:
        option = main_menu()

        if option == "01" or option == "1":
            data["email_pattern"] = input(f" {colorama.Fore.WHITE}[Enter email pattern]> {colorama.Fore.RESET}")
        elif option == "02" or option == "2":
            data["first_name"] = input(f" {colorama.Fore.WHITE}[Enter first name]> {colorama.Fore.RESET}")
        elif option == "03" or option == "3":
            data["middle_name"] = input(f" {colorama.Fore.WHITE}[Enter middle name]> {colorama.Fore.RESET}")
        elif option == "04" or option == "4":
            data["last_name_1"] = input(f" {colorama.Fore.WHITE}[Enter first last name]> {colorama.Fore.RESET}")
        elif option == "05" or option == "5":
            data["last_name_2"] = input(f" {colorama.Fore.WHITE}[Enter second last name]> {colorama.Fore.RESET}")
        elif option == "06" or option == "6":
            data["birthday_day"] = input(f" {colorama.Fore.WHITE}[Enter birthday day]> {colorama.Fore.RESET}")
        elif option == "07" or option == "7":
            data["birthday_month"] = input(f" {colorama.Fore.WHITE}[Enter birthday month]> {colorama.Fore.RESET}")
        elif option == "08" or option == "8":
            data["birthday_year"] = input(f" {colorama.Fore.WHITE}[Enter birthday year]> {colorama.Fore.RESET}")
        elif option == "98":
            for key in data.keys():
                data[key] = ""
        elif option == "99":
            break
        elif option.lower() == "run":
            if not data["email_pattern"]:
                print(f"{colorama.Fore.RED}Please fill email pattern field before running.{colorama.Fore.RESET}")
                input("Press Enter to continue...")
            else:
                generated_patterns = generate_pattern(data["first_name"].lower(), data["middle_name"].lower(), data["last_name_1"].lower(), data["last_name_2"].lower(), data["birthday_day"], data["birthday_month"], data["birthday_year"])
                valid_patterns_amount = compare_pattern(data["email_pattern"], generated_patterns)

                runnig_info(len(generated_patterns), len(valid_patterns_amount), valid_patterns_amount)

                for key in data.keys():
                    data[key] = ""