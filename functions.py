
import time

def timingDecorator(function):
    def wrapper():
        time_start = time.time()
        function()
        print(f'\nВремя выполнения составило: {round(time.time() - time_start, 2)}')
    return wrapper
