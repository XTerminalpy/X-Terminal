# Credits: Chaitanya, Rayirth, Dart, Empty

import shutil
import colorama
from colorama import Back, Fore, Style
import fnmatch
import socket
import time
import os
from re import search
import datetime
import json

colorama.init(autoreset=True)
path = os.getcwd()
os.chdir(path)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(
    f"{Fore.BLACK}{Back.RED}P{Back.YELLOW}y{Back.GREEN}t{Back.BLUE}e{Back.MAGENTA}r{Back.RED}m{Back.YELLOW}i{Back.GREEN}n{Back.BLUE}a{Back.MAGENTA}l")
print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Credits: {Fore.BLUE}{Style.BRIGHT}Chaitanya, Rayirth, Dart, Empty")


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


def generate_help():
    file = open("./help_cmd.json", "r")
    helpFileContent = file.read()
    file.close()

    js = json.loads(helpFileContent)

    for cmd in js["Commands"]:
        register_help([cmd], js["Commands"][cmd]["definition"])

    print(help_menu + "\n")


def processUserInput():
    global path
    while True:
        usr_input = input(
            Fore.GREEN + "( " + os.path.split(path)[1] + " )>>> ")

        if usr_input == "":
            continue

        elif usr_input.startswith("echo"):
            cmd = usr_input.split(" ")
            toEcho = ""
            if len(cmd) > 1:
                toEcho = " ".join(cmd[1:])
            else:
                toEcho = input("What do you want to echo?: ")

            print(toEcho)
            continue

        elif usr_input == "helpall":
            print(help_menu)
            continue

        elif usr_input.startswith("cd"):
            cmd = usr_input.split(" ")
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

        elif usr_input == "ls":
            for files in os.listdir(path):
                print(Fore.CYAN + '-' + files)
            continue

        elif usr_input.startswith("help"):
            cmd = usr_input.split(" ")
            asked_cmd = ""
            if len(cmd) == 2:
                asked_cmd = cmd[1]
            else:
                asked_cmd = input("What command would you like help with?: ")

            with open('help_cmd.json') as fcc_file:
                data = json.load(fcc_file)["Commands"]
                asked_cmd = cmd[1]

                if not (asked_cmd in data):
                    print(Back.RED + Fore.BLACK + '''The command you entered after help is not found. Make sure you enter the command correctly or check even if the command exists.\nMake sure you enter the command after the space''')
                    continue

                for i in data[asked_cmd].values():
                    print(Fore.MAGENTA + i)

        elif usr_input.startswith("mkdir"):
            cmd = usr_input.split(" ")
            newdir = ""
            if len(cmd) == 2:
                newdir = cmd[1]
            else:
                newdir = input("directory name: ")

            newdir_path = os.path.join(path, newdir)

            if os.path.exists(newdir_path):
                print(f"mkdir: {newdir} already exists")
                continue

            os.mkdir(newdir_path)
            print("Directory '% s' created" % newdir)
            continue

        elif usr_input.startswith("rmdir"):
            cmd = usr_input.split(" ")
            dir_to_remove = ""
            if len(cmd) == 2:
                dir_to_remove = cmd[1]
            else:
                dir_to_remove = input("directory name: ")

            rmdir_path = os.path.join(path, dir_to_remove)

            if not os.path.exists(rmdir_path):
                print(f"{rmdir_path}: no such file or directory")
                continue

            if len(os.listdir(rmdir_path)) > 0:
                print(Fore.RED + Style.BRIGHT +
                      "The directory has files in it...")
                sure = input(
                    f"{Fore.RED}{Style.BRIGHT} Are you sure you want to remove it? {Fore.YELLOW}{Style.DIM}[Y/n]{Fore.RESET}: ").lower()
                if sure == "yes" or sure == "y":
                    shutil.rmtree(rmdir_path)
                continue

            os.rmdir(rmdir_path)
            print("Directory '% s' removed" % dir_to_remove)
            continue

        elif usr_input.startswith("rm"):
            cmd = usr_input.split(" ")
            file_to_remove = ""
            if len(cmd) == 2:
                file_to_remove = cmd[1]
            else:
                file_to_remove = input("filename (include file extension): ")

            rmfile_path = os.path.join(path, file_to_remove)

            if not os.path.exists(rmfile_path):
                print(f"{file_to_remove}: no such file")
                continue

            if os.path.isdir(rmfile_path):
                print(f"{file_to_remove}: is a directory, please us rmdir instead")
                continue

            os.remove(rmfile_path)
            print("File '% s' removed" % file_to_remove)
            continue

        elif usr_input.startswith("read"):
            cmd = usr_input.split(" ")
            filename = ""
            if len(cmd) == 2:
                filename = cmd[1]
            else:
                filename = input("file to read(include file extension): ")

            filedir = os.path.join(path, filename)

            if not os.path.exists(filedir):
                print(f"{filename}: no such file ")
                continue

            with open(filedir, "r") as f:
                print("\n\n" + Fore.YELLOW + f.read() + "\n\n")
            continue

        elif usr_input == "search":
            searchinput = input("What would you like to search for?: ")

            def find(pattern, a):
                result = []
                for root, dirs, files in os.walk(a):
                    for name in files:
                        if fnmatch.fnmatch(name, pattern):
                            result.append(os.path.join(root, name))
                return result

            files = find(searchinput, path)
            for i in files:
                print(Fore.CYAN + '-' + i)
            continue

        elif usr_input.startswith("create"):
            cmd = usr_input.split(" ")
            if len(cmd) > 2:
                for i in range(1, len(cmd)):
                    f = open(cmd[i], "x")
                    f.close()
                    print("New file created")
            else:
                newfilename = input("What will be the new file's name?: ")
                newfile = os.path.join(path, newfilename)
                f = open(newfile, "x")
                f.close()
                print("New file created")
            continue

        elif usr_input == "clear" or usr_input == "cls":
            _ = os.system("clear")

        elif usr_input == "pwd":
            print(os.getcwd())

        elif usr_input == "whoami":
            try:
                print(os.getlogin())
            except OSError:
                print("This device has no user")

        elif usr_input.startswith("exec"):
            cmd = usr_input.split(" ")
            if len(cmd) < 2:
                print("Missing argument SYSTEM_COMMAND")
                continue

            _ = os.system(" ".join(cmd[1:]))

        elif usr_input.startswith("ping"):
            cmd = usr_input.split(" ")
            hostname = ""
            if len(cmd) == 2:
                hostname = cmd[1]
            else:
                hostname = input("address: ")

            response = os.system("ping " + hostname)
            # and then check the response...
            if response == 0:
                print(" ")
                print(Fore.LIGHTRED_EX + hostname, 'is up!')
            else:
                print(" ")
                print(Fore.LIGHTRED_EX + hostname, 'is down!')

        elif usr_input == "tday":
            x = datetime.date.today()
            print(x)
            print(Fore.GREEN + x.strftime("%A"))
            continue

        elif usr_input == "stop" or usr_input == "quit":
            print(f"{Fore.YELLOW}BRAVO SIX GOING {Back.WHITE}{Fore.BLACK}DARK!")
            # print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Alright then, have a nice day!")
            time.sleep(2)
            break

        else:
            print(f"pyterminal: {usr_input}: commmand not found")
            continue


if __name__ == "__main__":
    generate_help()
    processUserInput()
