description = "This command clears the entire screen"
usage = ["'clear'. If we type this command the terminal clears everything on the screen"]

# must have
import os
def run(args: str, ro_path:str):
   _ = os.system("clear")


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
