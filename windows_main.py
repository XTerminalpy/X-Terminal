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

sure = False

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


register_help(["echo"], "says what you want")
register_help(["help"], "prints all the commands")
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
    if usr_input.startswith("echo"):
        cmd = usr_input.split(" ")
        if len(cmd) > 1:
           _ = print(" ".join(cmd[1:]))
        else:
            echoinput = input("What do you want to echo?: ")
            print(echoinput)

    elif usr_input == "help":
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
        list = os.listdir(path)
        for files in list:
            print(Fore.CYAN + '-' + files)
        continue

    #f = open('help_cmd.json')
## returns JSON object as 
## a dictionary
    #data = json.load(f)
## Iterating through the json
## list
    #for i in data["Commands"]:
        #print(i)
## Closing file
    #f.close()

    elif usr_input.startswith("mkdir"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            try:
                newdir = cmd[1]
                newdir_path = os.path.join(path, newdir)
                os.mkdir(newdir_path)
                print("Directory '% s' created" % newdir)
            except FileExistsError:
                print("Mention dir name after space")
            continue

        else:
            newdir = input("directory name: ")
            newdir_path = os.path.join(path, newdir)
            os.mkdir(newdir_path)
            print("Directory '% s' created" % newdir)
        continue

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
                print("Make sure you enter filename after the space")
        else:
            file_to_remove = input("file name(include file extension): ")
            rmfile_path = os.path.join(path, file_to_remove)
            os.remove(rmfile_path)
            print("File '% s' removed" % file_to_remove)
        continue

    elif usr_input.startswith("read"):
        cmd = usr_input.split(" ")
        if len(cmd) == 2:
            try:
                filename = cmd[1]
                filedir = os.path.join(path, filename)
                with open(filedir) as f:
                    lines = f.read()
                    print("")
                    print("")
                    print(Fore.YELLOW + lines)
                    print("")
                    print("")

            except FileNotFoundError:
                print("The file you wanted to read is not found")

        else:
            try:
                filename = input("file to read(include file extension): ")
                filedir = os.path.join(path, filename)
                with open(filedir) as f:
                    lines = f.read()
                    print("")
                    print("")
                    print(Fore.YELLOW + lines)
                    print("")
                    print("")
            
            except FileNotFoundError:
                print("The file you wanted to read is not found")
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
        if len(cmd) == 1:
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
        print(os.system("clear"))

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

    elif usr_input == "tday":
        x = datetime.date.today()
        str(x)
        print(x)
        print(Fore.GREEN + x.strftime("%A"))
        continue

    elif usr_input.startswith("help"):
        cmd = usr_input.split(" ")
        cdword = "cd"
        if len(cmd) < 2:
            if search(cdword, cmd):
                print("True")
            else:
                print("False")

    elif usr_input == "stop":
        print(f"{Fore.YELLOW}BRAVO SIX GOING {Back.WHITE}{Fore.BLACK}DARK!")
        #print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Alright then, have a nice day!")
        time.sleep(2)
        break

    elif usr_input == "quit":
        print(f"{Fore.YELLOW}BRAVO SIX GOING {Back.WHITE}{Fore.BLACK}DARK!")
        #print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Alright then, have a nice day!")
        time.sleep(0)
        break
        
    

    else:
        print(f"pyterminal: {usr_input}: commmand not found")
        continue
