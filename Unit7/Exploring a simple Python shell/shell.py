"""a simple python CLI"""

def psh_help():
    print("""Commands:
          add: Input integers with spaces in between to receive sum.
          help: You are here.
          exit: Exits the application.""")

def add(string):
    total = 0
    for num in string.split(" "):
        try:
            num = int(num)
        except:
            "Not a valid number."
            break
        finally:
            total += num
    print(total)
            

def main():
    while True:
        inp = input("$ ")
        if inp == "exit":
            break
        elif inp == "help":
            psh_help()
        elif inp[:4] == "add ":
            add(inp.removeprefix("add "))
        else:
            print("Unknown command")


if '__main__' == __name__:
    main()