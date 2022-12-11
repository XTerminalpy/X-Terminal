description = "This command remove the selected file in the cwd(current working directory)"
usage = [
        "rm 'name(withext)'. Here it will delete this file",
        "'rm file.txt'. Here it will delete this file.txt"
        ]

import os
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    file_to_remove = ""
    if len(cmd) == 2:
        file_to_remove = cmd[1]
    else:
        file_to_remove = input("filename (include file extension): ")

    rmfile_path = os.path.join(ro_path, file_to_remove)

    if not os.path.exists(rmfile_path):
        print(f"{file_to_remove}: no such file")
        return

    if os.path.isdir(rmfile_path):
        print(f"{file_to_remove}: is a directory, please us rmdir instead")
        return

    os.remove(rmfile_path)
    print("File '% s' removed" % file_to_remove)
    return


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
