import time

def log(fn):
    def wrapped(*args):
        start = time.time()
        value = fn(*args)
        end = time.time()
        print('{:s}: {} - took {:.3f} ms'.format(fn.__name__, value, (end - start) * 1000.0))

        return value
    return wrapped