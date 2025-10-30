#orientação a objetos: paradigma de programação
#python é uma linguagem multiparadigma
#estudei paradigma estuturado e funcional

#classe e objetos


#class Veiculo - modelos abstratos que representam itens do mundo real
#objetos - são ocorrências destas classes.


'''
É um paradigma de programação, ou seja, uma forma de organizar e estruturar o código.
Na POO, em vez de apenas escrever funções soltas e variáveis, você modela o problema em objetos, que representam coisas do mundo real ou conceitos abstratos.

Exemplo:

Em um sistema bancário → "Conta Bancária" pode ser um objeto.

Em um jogo → "Jogador" e "Inimigo" podem ser objetos.

Cada objeto tem:

Atributos → características (ex: nome, saldo, idade).
Métodos → ações ou comportamentos (ex: depositar(), sacar(), correr()).

Classe

Uma classe é como um molde ou planta baixa que descreve como os objetos daquele tipo serão.
Ela não é o objeto em si, mas a definição dele.

função dentro de um class é chamado de método

agora um atributo guarda um valor dentro do class começando com self. - 
atributo interno que guarda o valor da classe

não tem objeto dentro de uma classe, o bjeto é criado no sistema principal.

'''

class Veiculo:
    def movimentar(self): #método
        print(f'sou um carro')

    def __init__(self, modelo, ano): #atributo
        self.modelo = modelo #atributo
        self.__ano = ano  #atributo - em todos estes exemplos são atributos públicos, 
        # ou seja, qualquer um pode acessar, para deixar privado utilziamos o 
        # método de encapsulamento, que funciona com o - __ antes do nome do objeto  
        self.cor = None #atributo


    #setter - serve para atribuir um valor a um atributo
    def set_cor(self, cor):
        self.cor = cor

    #getter de encapsulados
    def get_ano(self):
        print(self.__ano)
    def get_cor(self):
        return self.cor

#heranças reaproveita o que já foi codificado em uma classe para outra, por exemplo

class Carro(Veiculo):
    #init herdado do Veiculo
    def movimentar(self):
        print(f'me movimento sobre 4 rodas')



if __name__ == '__main__':
    meu_veiculo = Veiculo('Fiat','2016')  #objeto
    meu_veiculo.movimentar() #invocar o método
    print(meu_veiculo.modelo) #chama o atributo - com os traços e o atributo encapusaldo
    # não é possivel chamar o valor do atributo
    meu_veiculo.get_ano()
    meu_veiculo.set_cor('vermelho')
    print(f'cor: {meu_veiculo.get_cor()}')
    
    carro = Carro('ferrari', 2023)
    carro.movimentar()
    carro.get_ano()
    print(carro.modelo)

  


'''
para pegar qualquer informação encapsulada é preciso criar um função(def) getter 

'''



