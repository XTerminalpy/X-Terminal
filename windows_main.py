# Credits: Chaitanya, Rayirth, Dart, Empty

import shutil
import colorama
import colorama
from colorama import Back, Fore, Style
import fnmatch
import socket
import time
import os

colorama.init(autoreset=True)
path = os.getcwd()
os.chdir(path)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(f"{Fore.BLACK}{Back.RED}P{Back.YELLOW}y{Back.GREEN}t{Back.BLUE}e{Back.MAGENTA}r{Back.RED}m{Back.YELLOW}i{Back.GREEN}n{Back.BLUE}a{Back.MAGENTA}l")
print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Credits: {Fore.BLUE}{Style.BRIGHT}Chaitanya, Rayirth, Empty, Dart")

sure = False

help_menu = f"""
{Fore.RED}pyterminal{Fore.RESET} version {Fore.BLUE}0.0.1{Fore.RESET}
{Fore.RED}pyterminal{Fore.RESET} is a terminal (shell) written in pure {Fore.BLUE}python{Fore.RESET}.

{Fore.RED}COMMANDS{Fore.RESET}:"""


def register_help(calls, desc):
    options = ", ".join(calls)
    thing = f"\n    {Fore.BLUE}{options}{Fore.RESET}"
    space = " " * (50 - len(thing))
    global help_menu
    help_menu += thing + space + desc


register_help(["echo"], "says what you want")
register_help(["help"], "prints all the commands")
register_help(["help 'name of command' "], "prints how the command works and how to use it")
register_help(["cd"], "change directory")
register_help(["mkdir"], "create new directory")
register_help(["remove", "rm"], "removes the selected file")
register_help(["ls"], "lists all files in the current directory")
register_help(["rmdir"], "remove the selected directory")
register_help(["search"], "search for the a file")
register_help(["create"], "creates a file with the given name")
register_help(["clear"], "clears the screen")
register_help(["read"], "prints the content of a selected file")
register_help(["pwd"], "prints the current working directory")
register_help(["exec"], "execute the provided system command")
register_help(["stop"], "exits pyterminal")
register_help(["whoami"], "gets the current logged in user's name")
register_help(["ping"], "pings an address")

print(help_menu)
print(" ")
while True:
    usr_input = input(Fore.GREEN + "( " + os.path.split(path)[1] + " )>>> ")
    if usr_input == "echo":
        echoinput = input("input to echo: ")
        print(echoinput)
        continue
#help cmd
    
    elif usr_input == "help":
        print(help_menu)
        continue
#cd cmd
    
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
#ls cmd
    elif usr_input == "ls":
        list = os.listdir(path)
        for files in list:
            print(Fore.CYAN + '-' + files)
        continue

#mkdir cmd
    elif usr_input.startswith("mkdir"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            newdir = cmd[1]
            newdir_path = os.path.join(path, newdir)
            os.mkdir(newdir_path)
            print("Directory '% s' created" % newdir)

        else:
            newdir = input("directory name: ")
            newdir_path = os.path.join(path, newdir)
            os.mkdir(newdir_path)
            print("Directory '% s' created" % newdir)
        continue
#rmdir cmd
    elif usr_input.startswith("rmdir"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            try:
                dir_to_remove = cmd[1]
                rmdir_path = os.path.join(path, dir_to_remove)
                os.rmdir(rmdir_path)
                print("Directory '% s' removed" % dir_to_remove)
            except OSError:
                print(Fore.RED + Style.BRIGHT + "The direcotry has files in it...")
                sure = input(
                    f"{Fore.RED}{Style.BRIGHT} Are you sure you want to remove it? {Fore.YELLOW}{Style.DIM}[Y/n]: ").lower()
                if sure == "yes" or sure == "y":
                    shutil.rmtree(rmdir_path)
                else:
                    print("canceled..")
                continue
        else:
            try:
                dir_to_remove = input("directory name: ")
                rmdir_path = os.path.join(path, dir_to_remove)
                os.rmdir(rmdir_path)
                print("Directory '% s' removed" % dir_to_remove)
            except OSError:
                print(Fore.RED + Style.BRIGHT + "The direcotry has files in it...")
                sure = input(
                    f"{Fore.RED}{Style.BRIGHT} Are you sure you want to remove it? {Fore.YELLOW}{Style.DIM}[Y/n]: ").lower()
                if sure == "yes" or sure == "y":
                    shutil.rmtree(rmdir_path)
                else:
                    print("canceled..")
        continue

    elif usr_input.startswith("rm"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            try:
                file_to_remove = cmd[1]
                rmfile_path = os.path.join(path, file_to_remove)
                os.remove(rmfile_path)
                print("File '% s' removed" % file_to_remove)
            except FileNotFoundError:
                print("Make sure you entered the file name correctly")
            except IsADirectoryError:
                print("Make sure you entered the file name after the space")
        else:
            file_to_remove = input("file name(include file extension): ")
            rmfile_path = os.path.join(path, file_to_remove)
            os.remove(rmfile_path)
            print("File '% s' removed" % file_to_remove)
        continue
#read cmd
    elif usr_input.startswith("read"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            filename = cmd[1]
            filedir = os.path.join(path, filename)
            with open(filedir) as f:
                lines = f.read()
                print("")
                print("")
                print(Fore.YELLOW + lines)
                print("")
                print("")
        else:
            filename = input("file to read(include file extension): ")
            filedir = os.path.join(path, filename)
            with open(filedir) as f:
                lines = f.read()
                print("")
                print("")
                print(Fore.YELLOW + lines)
                print("")
                print("")
        continue
#search cmd
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
#create cmd
    elif usr_input.startswith("create"):
        cmd = usr_input.split(" ")
        if len(cmd) < 1:
            print("Missing argument FILE_NAME")
            continue
        for i in range(1, len(cmd)):
            f = open(cmd[i], "x")
#clear smd
    elif usr_input == "clear":
        lines = 0
        while lines != 50:
            print(" ")
            lines += 1
        continue
#pwd cmd
    elif usr_input == "pwd":
        print(os.getcwd())
#whoami cmd
    elif usr_input == "whoami":
        try:
            print(os.getlogin())
        except OSError:
            print("This device has no user")
#exec cmd
    elif usr_input.startswith("exec"):
        cmd = usr_input.split(" ")
        if len(cmd) < 2:
            print("Missing argument SYSTEM_COMMAND")
            continue

        _ = os.system(" ".join(cmd[1:]))
#ping cmd
    elif usr_input.startswith("ping"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            hostname = cmd[1]
            response = os.system("ping " + hostname)

            # and then check the response...
            if response == 0:
                print(" ")
                print(Fore.LIGHTRED_EX + hostname, 'is up!')
            else:
                print(" ")
                print(Fore.LIGHTRED_EX + hostname, 'is down!')

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
        continue

#help_echo cmd
    elif usr_input == ("help echo"):
        print(f" {Fore.WHITE}{Style.DIM}echo command is used to repeat what you have typed. \n if the user type 'echo' they'll get message that 'input to echo:' \n The message gets prints which is typed after that ")
        continue

#help_cd cmd
    elif usr_input == ("help cd"):
        print(f" {Fore.WHITE}{Style.DIM}Cd command is used to change directory \n if the user type cd 'path' \n The cwd(current working directory) changes to the path mentonied \n example:\n 'cd Downloads' \n The cwd changes to Downloads")
        continue

#help_mkdir cmd
    elif usr_input == ("help mkdir"):
        print(f" {Fore.WHITE}{Style.DIM}mk dir command is to make a directory(folder) \n if the user types 'mkdir'name''\n it creates a direcotry(folder) of the name given \n example: \n 'mkdir Test' \n It created a directory(Folder) Test'")
        continue

#help_rmdir cmd
    elif usr_input == ("help rmdir"):
        print("")
        continue
#stop cmd
    elif usr_input == "stop":
        print(f"{Fore.YELLOW}BRAVO SIX GOING {Back.WHITE}{Fore.BLACK}DARK!")
        time.sleep(2)
        break


    else:
        print(f"pyterminal: {usr_input}: commmand not found")
        continue
