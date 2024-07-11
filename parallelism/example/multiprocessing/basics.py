import multiprocessing


def print_numbers():
    for i in range(5):
        print(i)


if __name__ == '__main__':
    # Create two processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_numbers)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for the processes to complete
    process1.join()
    process2.join()
