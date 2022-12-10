description = "This command shows the pwd (current working directory)"


# must have
def run(args: str, ro_path:str):
    print(ro_path)

# must have
def constructor():
    return {"description": description, "exec": run}
