import time, os

def solution():
    start_time = time.perf_counter()
    sum = 0
    padding_field = []

    with open(os.path.join('python', 'day_4', 'input.txt'), 'r') as file:
        file = file.read().strip().split('\n')

        # Fill a padding field with dots around the original field
        padding_field.append(['.'] * (len(file[0]) + 2))  # Top padding
        for line in file:
            padding_field.append(['.'] + list(line) + ['.'])  # Side paddings
        padding_field.append(['.'] * (len(file[0]) + 2))  # Bottom padding

    for i in range(1, len(padding_field) - 1):
        for j in range(1, len(padding_field[0]) - 1):
           
            # Exit instantly if cell is not paper
            if padding_field[i][j] != '@':
                continue

            count = 0
            still_possible = True

            # Check all adjacent cells
            for x in range(-1, 2):   
                # Exit early if more than 3 neighbors are found
                if not still_possible:
                   break
                
                for y in range(-1, 2):
                    if not (x == 0 and y==0) and padding_field[i + x][j + y] == '@':
                        count += 1
                        if count > 3:
                            still_possible = False
                            break

            if count <= 3:
                sum += 1

    end_time = time.perf_counter()
    print(f"Answer: {sum}")
    print(f"Time taken: {end_time - start_time:.9f} seconds")
if __name__ == "__main__":
    solution()