def soma(parcela1:float, parcela2:float)->float:
    if valida_float(parcela1) and valida_float(parcela2):
        soma = parcela1 + parcela2
        return soma


def subtracao(minuendo:float, subtraendo:float)->float:
    if valida_float(minuendo) and valida_float(subtraendo):
        diferenca = minuendo - subtraendo
        return diferenca


def multiplicacao(fator1:float, fator2:float)->float:
    if valida_float(fator1) and valida_float(fator2):
        produto = fator1 * fator2
        return produto


def divisao(dividendo:float, divisor:float)->float:
    try:
        if valida_float(dividendo) and valida_float(divisor):
            quociente = dividendo / divisor
            return quociente
    except ZeroDivisionError:
        raise ZeroDivisionError('Não é possível dividir por 0!')



def valida_float(numero:float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f'Valor informado {numero} não é float')
