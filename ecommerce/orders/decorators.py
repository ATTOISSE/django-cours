def decorator(fun):
    def wrapper(request,*args, **kwargs):
        print('avant vue')
        response = fun(request,*args, **kwargs)
        print('apres vue')
        return response
    return wrapper

