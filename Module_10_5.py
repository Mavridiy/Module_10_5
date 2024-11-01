import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open (name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    start = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time()
    
    print(f"{linear_duration} (линейный)")

# Многопроцессный
    start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start

    print(f"{multiprocessing_duration} (многопроцессный)")


