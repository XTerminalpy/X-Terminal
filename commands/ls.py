description = "This commands shows the list of files in cwd(current working directory)"
usage = ["'ls'. It shows all the files and folders in the cwd(current workinf directory)"]

from colorama import Fore
import os
# must have
def run(args: str, ro_path):
    path = ro_path
    if len(args.split(" ")) > 1:
        path = " ".join(args.split(" ")[1:])

    for files in os.listdir(path):
        print(Fore.CYAN + '-' + files)


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
