description = "This command deletes directory(folder)"

import os, shutil
from colorama import Fore, Style
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    dir_to_remove = ""
    if len(cmd) == 2:
        dir_to_remove = cmd[1]
    else:
        dir_to_remove = input("directory name: ")

    rmdir_path = os.path.join(ro_path, dir_to_remove)

    if not os.path.exists(rmdir_path):
        print(f"{rmdir_path}: no such file or directory")
        return

    if len(os.listdir(rmdir_path)) > 0:
        print(Fore.RED + Style.BRIGHT +
                "The directory has files in it...")
        sure = input(
            f"{Fore.RED}{Style.BRIGHT} Are you sure you want to remove it? {Fore.YELLOW}{Style.DIM}[Y/n]{Fore.RESET}: ").lower()
        if sure == "yes" or sure == "y":
            shutil.rmtree(rmdir_path)
        return

    os.rmdir(rmdir_path)
    print("Directory '% s' removed" % dir_to_remove)
    return


# must have
def constructor():
    return {"description": description, "exec": run}
