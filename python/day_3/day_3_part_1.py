import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0

    with open(os.path.join('python', 'day_3', 'input.txt'), 'r') as file:

        # Get all banks
        file = file.read().strip().split('\n')

        # Turn banks into lists
        for line in file:
            line = list(line)
        
            # Find first appearance of max element and its index in list without last element
            maximum = max(line[:-1])
            index = line.index(maximum)

            # Find second maximum in list after the first maximum
            second_maximum = max(line[index + 1:])

            # Add jolt to sum
            sum += int(maximum + second_maximum)

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")

if __name__ == "__main__":
    solution()