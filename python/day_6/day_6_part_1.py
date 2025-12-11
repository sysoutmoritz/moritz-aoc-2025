import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0
    inputs = []
    
    with open(os.path.join('python', 'day_6', 'input.txt'), 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            line = [n for n in line if n.strip()] # Remove empty strings
            inputs.append(line)

    # Iterate over every problem
    for i in range(len(inputs[0])):
        sign = inputs[-1][i]
        if sign == '+':
            total = 0
        else:
            total = 1
        # Iterate over every number in problem
        for j in range(len(inputs)-1):
            if sign == '+':
                total += int(inputs[j][i])
            else:
                total *= int(inputs[j][i])
        sum += total 

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")
    
if __name__ == "__main__":
    solution()