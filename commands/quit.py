description = "Quits the terminal"
usage = ["'quit'. The terminal will stop and close"]

import time
from sys import exit
from colorama import Fore, Back
def run(args: str, ro_path):# must have
    print(f"{Fore.YELLOW}BRAVO SIX GOING {Back.WHITE}{Fore.BLACK}DARK!{Fore.RESET}{Back.RESET}")
    # print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Alright then, have a nice day!")
    time.sleep(2)
    exit()


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
