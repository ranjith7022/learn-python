def args_logger(*args, **kwargs):
    [print(f" {i+1}. {j}") for i,j in enumerate(args)]
    [print(f" * {i}: {j}") for i,j in kwargs.items()]