description = "This command shows the pwd (current working directory)"
usage = ["'pwd'. The Terminal prints the directory your working in."]

# must have
def run(args: str, ro_path:str):
    print(ro_path)

# must have
def constructor():
    return {"description": description,"usage":usage, "exec": run}
