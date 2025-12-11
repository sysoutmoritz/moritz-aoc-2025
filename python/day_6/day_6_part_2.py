import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0
    inputs = []
    
    with open(os.path.join('python', 'day_6', 'input.txt'), 'r') as file:
        for line in file:
            line = list(line)
            if '\n' in line:
                line.remove('\n')
            inputs.append(line)

    operations = inputs[-1]
    for i in range(len(operations)):

        # Find sign and length of next interval
        if operations[i] == '+':
            total = 0
            interval = find_interval(operations, i)
        elif operations[i] == '*':
            total = 1
            interval = find_interval(operations, i)
        else:
            continue

        # Build the numbers and sum/multiply them up
        for j in range(i, i + interval):
            for k in range(len(inputs)-1):
                pass

        sum += total

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")

# Helper function to find the interval of current problem
def find_interval(line, start):
    interval = 1
    for char in line[start+1:]:
        if char == ' ':
            interval += 1
        else:
            break
    return interval
if __name__ == "__main__":
    solution()