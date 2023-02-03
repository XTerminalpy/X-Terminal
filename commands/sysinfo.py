description = "This command details your system and few of it specs(specifics)"
usage = []

from colorama import Fore, Style
import os
import platform

def run(args: str, ro_path:str):
    print(platform.machine)
    print(platform.node)
    print(platform.platform)
    print(platform.processor)
    print(platform.release)
    return

def constructor():
    return {"description": description,"usage":usage, "exec": run}
