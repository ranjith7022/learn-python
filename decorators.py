def configure_plugin_decorator(func):
    def wrapper(*args):
        kwags = dict(args)
        return func(**kwags)
        
    return wrapper


