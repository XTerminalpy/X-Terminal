description = "This command prints the 'user_id' in which the user is logged in"
import os
def run(args: str, ro_path:str):
    try:
        print(os.getlogin())
    except OSError:
        print("This device has no user")


# must have
def constructor():
    return {"description": description, "exec": run}
