description = "This command prints the date and the day"

import datetime
from colorama import Fore
# must have
def run(args: str, ro_path:str):
    x = datetime.date.today()
    print(x)
    print(Fore.GREEN + x.strftime("%A"))
    return


# must have
def constructor():
    return {"description": description, "exec": run}
