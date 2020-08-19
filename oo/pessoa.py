class Pessoa:
    def __init__(self):
        self.nome = None
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(Pessoa.cumprimentar(p))
    print(p.nome)
    p.nome = 'Abimael'
    print(p.nome)