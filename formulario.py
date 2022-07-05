import sympy as sym

class Formulario:
    """twertew"""

    eletromag = 'Eletromagnetismo é uma área que estuda (de modo mais fundamental) os fenômenos decorrentes da emissão, troca e absorção de particulas elétricas.'
    motivacao = 'Como seria a vida humana sem eletricidade? Praticamente tudo que fazemos hoje está relacionado com aparelhos eletrônicos, e para que esses aparelhos possam funcionar corretamente, foi necessário desenvolver um estudo em cima do tema "eletricidade" e realmente entender como ela se comporta para que todos os apralhos que usamos hoje pudessem ser contruídos. Essa é uma das motivações para o engenheiro e os fisicos estudarem tanto o tema, mas ainda, se pararmos para perceber, tudo a nossa volta é constituído de átomos. Os átmos são contituidos de prótons, neutrôns e elétrons, que é literalmente a energia elétrica, ou seja, tudo a nossa volta é feito de um amontoado de cargas elétricas, também sendo uma grande motivação de estudo desse tema, onde nós não apenas iremos entender como os aparelhos elétricos funcionam, mas também como tudo a nossa volta.'

    def __init__(self, carga_elementar=1.6*(10**(-19))):
        self.carga_proton = carga_elementar
        self.carga_eletron = carga_elementar*(-1)

    def quant_particula(self, carga_total, proton_ou_eletron = 'eletron'):
        if proton_ou_eletron == 'eletron':
            return carga_total/self.carga_eletron
        elif proton_ou_eletron == 'proton':
            return carga_total/self.carga_proton
        else:
            return print('Parâmetro de partícula inválido')