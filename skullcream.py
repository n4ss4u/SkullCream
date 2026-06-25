import colorama

from ui import banner

data = {"email_pattern": "", "first_name": "", "middle_name": "", "last_name_1": "", "last_name_2": "", "birthday_day": "", "birthday_month": "", "birthday_year": ""}
check_exist_data = ""

def main_menu():
    banner()
    for i, (key, value) in enumerate(data.items(), start=1):
        if value == "":
            check_exist_data = f"{colorama.Fore.RED}x{colorama.Fore.RESET}"
        else:
            check_exist_data = f"{colorama.Fore.GREEN}✓{colorama.Fore.RESET} ({value})"
            
        print(f" ├[0{i}]- {key.capitalize().replace("_", " ")} {check_exist_data}")
    
    print(" ├[98]- Reset")
    print(" ├[99]- Exit")
    option = input(f" {colorama.Fore.WHITE}└──> (type RUN to start): {colorama.Fore.RESET}")
    return option 

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
                print(f"{colorama.Fore.GREEN}Running with the provided data...{colorama.Fore.RESET}")