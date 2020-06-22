def header(function):
    def wrapper(*args, **kwrags):
        print('### Bem vindo ao meu site ###')
        function(*args, **kwrags)
    return wrapper


def footer(funcion):
    def wrapper(*args, **kwargs):
        funcion(*args, **kwargs)
        print('### Coprigth ###')
        print('\n\n\n\n')
    return wrapper


@footer
@header
def produto(nome):
    print(f'Produto: {nome}')
    

produto('pão')

def pao(f):
    def wrapper(*args, **kwargs):
        print("(fatia superior do pao)")
        f(*args, **kwargs)
        print("(fatia inferior do pao)")
    return wrapper

@pao
def lanche(recheio):
    print(f'{recheio}')


lanche('cheese burguer')