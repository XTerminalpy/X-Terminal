description = "This command show to information typed inside a file"

import os
from colorama import Fore
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    filename = ""
    if len(cmd) == 2:
        filename = cmd[1]
    else:
        filename = input("file to read(include file extension): ")

    filedir = os.path.join(ro_path, filename)

    if not os.path.exists(filedir):
        print(f"{filename}: no such file ")
        return

    with open(filedir, "r") as f:
        print("\n\n" + Fore.YELLOW + f.read() + "\n\n")



# must have
def constructor():
    return {"description": description, "exec": run}
