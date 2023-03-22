
import time

def timingDecorator(function):
    def wrapper():
        time_start = time.time()
        function()
        print(f'\nThe execution time was: {round(time.time() - time_start, 2)}')
    return wrapper
