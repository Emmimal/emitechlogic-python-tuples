import os

print("Running all tuple examples...\n")
for file in sorted(os.listdir("examples")):
    if file.endswith(".py"):
        print(f"--- {file} ---")
        os.system(f"python examples/{file}")
        print()
