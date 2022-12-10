description = "This command searches for an existing file in the cwd(current working directory)"

import fnmatch, os
from colorama import Fore
# must have
def run(args: str, ro_path:str):
    searchinput = input("What would you like to search for?: ")

    def find(pattern, a):
        result = []
        for root, dirs, files in os.walk(a):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    files = find(searchinput, ro_path)
    for i in files:
        print(Fore.CYAN + '-' + i)
    return


# must have
def constructor():
    return {"description": description, "exec": run}
