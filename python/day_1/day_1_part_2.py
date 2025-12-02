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

            if dial >= 100:
                #print(f"Dial exceeded 100: {dial}, so adding to count {int(dial/100)}")
                count += int(dial/100)
            if dial <= 0:
                count += abs(int((dial-100)/100))
                #print(f"Dial below 0: {dial}, so adding to count {abs(int((dial-100)/100))}")

                if dial + int(line[1:]) == 0: # if you started at 0 and went left, don't double count
                    count -= 1
                    #print(f"Correcting for double count, new count is {count}")

                

            dial %= 100
            #print(f"Dial after: {dial}, Count is {count}")

    print(f"Answer: {count}")

if __name__ == "__main__":
    solution()