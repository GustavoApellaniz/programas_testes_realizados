class Pessoa:
    def mult(self, ano):
        print(f'sua idade é {ano}, logo o dobro é {ano*2}')
    def __init__(self, nome, nascimento, prof):
        self.nome = nome
        self.nascimento = nascimento
        self.prof = prof
    

if __name__ == '__main__':
    x = Pessoa('Ricardo', '2001', 'engenheiro')
    print(x.nome)


