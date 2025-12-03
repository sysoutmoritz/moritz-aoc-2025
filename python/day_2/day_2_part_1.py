import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0

    with open(os.path.join('python', 'day_2', 'input.txt'), 'r') as file:

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

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")             

if __name__ == "__main__":
    solution()
    