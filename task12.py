import functools

def named(f):
    @functools.wraps(f)
    def bar(*args, **kwargs):
        print("Type: ", args[0]._name, " data: ", args[0]._data)
        return f(*args, **kwargs)
    return bar