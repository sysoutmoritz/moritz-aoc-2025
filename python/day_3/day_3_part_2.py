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
        
            count = 0 # Digit count that keeps track of how many digits have been processed
            pointer = 0 # Pointer that moves to the right after another maximum has been found
            jolt = '' # String to build the jolt number by number

            # Find next best jolt number by taking the maximum of the remaining list to the right of the pointer, making sure that you always leave enough digits at the end to form a 12-digit number
            while count < 12:
                available_list = line[pointer:-11 + count] if count != 11 else line[pointer:] # Part of the list where we can choose a maximum from without breaking any conventions by skipping behind or not leaving enough digits at the end
                maximum = max(available_list)
                jolt += maximum
                pointer += available_list.index(maximum) + 1
                count += 1

            # Add jolt to sum
            sum += int(jolt)

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")

if __name__ == "__main__":
    solution()