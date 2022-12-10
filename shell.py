import os
import importlib
from colorama import Back, Fore, Style

commands_dir = "./commands"

commands = []
commands_names = []

path = os.getcwd()
os.chdir(path)

help_menu = f"""
{Fore.RED}pyterminal{Fore.RESET} version {Fore.BLUE}0.0.1{Fore.RESET}
{Fore.RED}pyterminal{Fore.RESET} is a terminal (shell) written in pure {Fore.BLUE}python{Fore.RESET}.

{Fore.RED}COMMANDS{Fore.RESET}:"""

def register_help(calls, desc):
    options = ", ".join(calls)
    thing = f"\n      {Fore.BLUE}{options}{Fore.RESET}"
    space = " " * (50 - len(thing))
    global help_menu
    help_menu += thing + space + desc

def print_banner():
    print(f"{Fore.BLACK}{Back.RED}P{Back.YELLOW}y{Back.GREEN}t{Back.BLUE}e{Back.MAGENTA}r{Back.RED}m{Back.YELLOW}i{Back.GREEN}n{Back.BLUE}a{Back.MAGENTA}l{Back.RESET}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Credits: {Fore.BLUE}{Style.BRIGHT}Chaitanya, Rayirth, Dart, Empty{Back.RESET}{Fore.RESET}")


def load_commands():
    ## Note that commands that mutate anything being
    ## in this file must be with the other built-ins starting at line 67

    for file in os.listdir(commands_dir):
        if not file.endswith(".py"):
            continue
        name = file[:-3]
        dir = commands_dir
        if dir.startswith("./"):
            dir = dir[2:]
        pkg = f"{dir}.{name}"
        globals()[name] = importlib.import_module(pkg)
        # globals()[name].constructor()["exec"]("hi")
        commands_names.append(name)
        commands.append(globals()[name].constructor())

        register_help([name], globals()[name].description)


def process_user_input():
    global path
    while True:
        user_input = input(
            Fore.GREEN + "( " + os.path.split(path)[1] + " )>>> ")
        requested_cmd = user_input.split(" ")[0]

        # process returns and spaces
        if requested_cmd in ["", " "]:
            continue

        # check if the requested commands is in an external file
        if requested_cmd in commands_names:
            index = commands_names.index(requested_cmd)
            commands[index]["exec"](user_input, path)

        # check built-ins
        elif requested_cmd == "help":
            print(help_menu + "\n")

        elif requested_cmd == "cd":
            cmd = user_input.split(" ")
            new_path = path
            if len(cmd) == 2:
                new_path = cmd[1]

            else:
                new_path = input("path: ")

            if os.path.exists(new_path):
                os.chdir(new_path)
                path = os.getcwd()
            else:
                print(f"{new_path}: no such file or directory")

            continue

        else:
            print(f"pyterminal: {user_input}: commmand not found")


if __name__ == "__main__":
    load_commands()
    print_banner()
    print(help_menu + "\n")
    process_user_input()
