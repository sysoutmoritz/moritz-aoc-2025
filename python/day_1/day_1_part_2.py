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

            # Count depending on how many times we've wrapped around
            if dial >= 100:
                count += int(dial/100)
            if dial <= 0:
                count += abs(int((dial-100)/100))

                 # If you started at 0 and went left, don't double count
                if dial + int(line[1:]) == 0:
                    count -= 1

            # Make sure dial is within 0-99
            dial %= 100

    print(f"Answer: {count}")

if __name__ == "__main__":
    solution()
    