description = "This command clears the entire screen"


# must have
import os
def run(args: str, ro_path:str):
   _ = os.system("clear")


# must have
def constructor():
    return {"description": description, "exec": run}
