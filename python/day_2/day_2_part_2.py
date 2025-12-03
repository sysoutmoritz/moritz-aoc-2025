import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0

    with open(os.path.join('python', 'day_2', 'input.txt'), 'r') as file:

        # Get all ID ranges as a list
        file = file.read().strip().split(',')
        for idrange in file:
            interval = idrange.split('-')

            # Get all IDs of a range to test them
            for id in range(int(interval[0]), int(interval[1]) + 1):
                id = str(id)

                #Find all possible substring lengths that can divide the id evenly
                possible_substring_lengths = [i for i in range(1, int(len(id)/2) + 1) if len(id) % i == 0]
                
                # Test each possible substring length
                for substring_length in possible_substring_lengths:
                    if id[:substring_length]*int(len(id)/substring_length) == id:
                        sum += int(id)
                        break

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")                       

if __name__ == "__main__":
    solution()
