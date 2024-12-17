from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf_8') as file:
        while True:
            line = file.readline()
            if line:
                all_data.append(line.strip())
            else:
                break


if __name__ == '__main__':
    filenames = [f'files/file {number}.txt' for number in range(1, 5)]
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    print(datetime.now() - start_time)
    start_time = datetime.now()
    with Pool(len(filenames)) as pool:  # processes=multiprocessing.cpu_count() создает количество процессов равное
        pool.map(read_info, filenames)  # колиечству ядер компьютера, использовать вметс len
    print(datetime.now() - start_time)
