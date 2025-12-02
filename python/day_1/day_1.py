def solution():
    dial = 50
    count = 0

    with open("input.txt") as file:
        for line in file:
            line = line.strip()

            # Adjust dial based on instruction
            if line.startswith("L"):
                dial -= int(line[1:])
            elif line.startswith("R"):
                dial += int(line[1:])

            # Make sure dial is within 0-99
            dial %= 100

            # Count if dial is at 0
            if dial == 0:
                count += 1

    print(f"Answer: {count}")

if __name__ == "__main__":
    solution()