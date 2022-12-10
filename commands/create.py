description = "This command is used to create files in the selected dir"

# must have
import os
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    if len(cmd) > 1:
        for i in range(1, len(cmd)):
            f = open(cmd[i], "x")
            f.close()
            print("New file created")
    else:
        newfilename = input("What will be the new file's name?: ")
        newfile = os.path.join(ro_path, newfilename)
        f = open(newfile, "x")
        f.close()
        print("New file created")


# must have
def constructor():
    return {"description": description, "exec": run}
