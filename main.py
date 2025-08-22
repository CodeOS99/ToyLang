from runner import Runner

print("Welcome to REPL of simplelang\n")
print("exit to exit")
print("run *filename.sl* to run a file")
print("or write code to be executed here directly!")
print("try it with run demo.tl!")

runner = Runner(repl=True)

while True:
    prog = input(">> ").strip()
    if prog == "exit":
        print("Exiting")
        break
    if prog == "":
        continue

    if prog.startswith("run "):
        filename = prog[4:].strip()
        try:
            with open(filename, "r") as f:
                code = f.read()
            runner.run(code, is_file=True)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error running {filename}: {e}")
        continue

    runner.run(prog)

print("Exiting successful")
