import functools

def counted(foo):
    counted._count = {}
    @functools.wraps(foo)
    def bar(*args, **kwargs):
        counted._count[bar.__name__] = counted._count.get(bar.__name__, 0) + 1
        print(bar.__name__, "called", counted._count[bar.__name__], "times")
        return foo(*args, **kwargs)
    return bar