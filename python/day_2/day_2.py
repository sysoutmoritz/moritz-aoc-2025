def solution():
    sum = 0

    with open('input.txt', 'r') as file:

        # Get all ID ranges as a list
        file = file.read().strip().split(',')
        for idrange in file:
            interval = idrange.split('-')

            # Get all IDs of a range that can be equally divided in two halves to test them
            for id in [i for i in range(int(interval[0]), int(interval[1]) + 1) if len(str(i)) % 2 == 0]:
                id = str(id)

                # Check if the ID is made of two repeating halves
                if id[:len(id)//2]*2 == id:
                    sum += int(id)

    print(f"Answer: {sum}")             

if __name__ == "__main__":
    solution()
    