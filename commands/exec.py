description = "This command executes the command typed after it divided by a space"

import os
# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    if len(cmd) < 2:
        print("Missing argument SYSTEM_COMMAND")
        return

    _ = os.system(" ".join(cmd[1:]))


# must have
def constructor():
    return {"description": description, "exec": run}
