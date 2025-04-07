class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel 

    def exibir_detalhes(self):
        barra = '█' * (self.__vida // 10)
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()} [{barra}]\nNível: {self.get_nivel()}'
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!')


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}'


class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}'


class Jogo:
    def __init__(self):
        self.heroi = Heroi(nome='Questão', vida=120, nivel=9, habilidade='Super inteligência')
        self.vilao = Vilao(nome='Sistema', vida=95, nivel=4, tipo='Mongo Loide')

    def iniciar_batalha(self):
        print('⚔️ Iniciando Batalha ⚔️')
        rodada = 1
        while self.heroi.get_vida() > 0 and self.vilao.get_vida() > 0:
            print(f'\n🌀 Rodada {rodada}')
            print('\n👤 Detalhes dos personagens:')
            print(self.heroi.exibir_detalhes())
            print(self.vilao.exibir_detalhes())

            input('\nPressione Enter para atacar...')
            escolha = input('Escolha: (1 - Ataque Normal, 2 - Ataque Especial): ')

            if escolha == '1':
                self.heroi.atacar(self.vilao)
            elif escolha == '2':
                dano_especial = self.heroi.get_nivel() * 4
                self.vilao.receber_ataque(dano_especial)
                print(f'{self.heroi.get_nome()} usou um ATAQUE ESPECIAL e causou {dano_especial} de dano!')
            else:
                print('❌ Escolha inválida! Tente novamente.')
                continue  # pula o ataque do vilão

            if self.vilao.get_vida() > 0:
                self.vilao.atacar(self.heroi)
            
            rodada += 1

        print('\n🏁 Fim da batalha!')
        if self.heroi.get_vida() > 0:
            print('🎉 O herói venceu!')
        else:
            print('💀 O vilão venceu!')


# Executar o jogo
jogo = Jogo()
jogo.iniciar_batalha()
