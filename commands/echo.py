description = "This command will repeat the user input"

# must have
def run(args: str, ro_path:str):
    cmd = args.split(" ")
    toEcho = ""
    if len(cmd) > 1:
        toEcho = " ".join(cmd[1:])
    else:
        toEcho = input("What do you want to echo?: ")

    print(toEcho)


# must have
def constructor():
    return {"description": description, "exec": run}
