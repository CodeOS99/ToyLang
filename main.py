from runner import Runner

print("Welcome to REPL of simplelang\n")

runner = Runner()

while True:
    prog = input(">> ")
    if prog == "exit":
        print("Exiting")
        break
    if prog == "":
        continue

    runner.run(prog)

print("Exiting successful")
