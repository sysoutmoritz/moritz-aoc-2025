def solution():
    dial = 50
    count = 0

    with open("input.txt") as file:
        for line in file:

            line = line.strip()
            #print(f"Dial before: {dial}, line is {line}")

            if line.startswith("L"):
                dial -= int(line[1:])
            elif line.startswith("R"):
                dial += int(line[1:])

            dial %= 100
            #print(f"Dial after: {dial}")

            if dial == 0:
                count += 1

    print(f"Answer: {count}")

if __name__ == "__main__":
    solution()