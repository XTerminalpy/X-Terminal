description = "This command searches for an existing file in the cwd(current working directory)"
usage = [
        "search 'name(with ext)'. Here it shows the path of the searched file",
        "'search file.txt'. Here it shows the path of the file 'file.txt'"
        ]


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
    return {"description": description,"usage":usage, "exec": run}
