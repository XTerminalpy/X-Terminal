description = "This command is used to check the ping of the the website mentioned"
usage = [
        "ping 'website'. It shows the ping of the website mentioned",
        "'ping google.com'. It shows the ping of google"
        ]

# must have
import os
from colorama import Fore
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    hostname = ""
    if len(cmd) == 2:
        hostname = cmd[1]
    else:
        hostname = input("address: ")

    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        print(" ")
        print(Fore.LIGHTGREEN_EX + hostname, 'is up!')
    else:
        print(" ")
        print(Fore.LIGHTRED_EX + hostname, 'is down!')


# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
