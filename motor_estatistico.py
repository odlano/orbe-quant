
import math

def probabilidade_implicita(odd):
    if odd <= 1:
        return 0
    return 1 / odd

def odd_justa(probabilidade):
    if probabilidade <= 0 or probabilidade > 1:
        return None
    return 1 / probabilidade

def valor_esperado(probabilidade, odd):
    if odd <= 1 or not 0 <= probabilidade <= 1:
        return None
    return (probabilidade * odd - 1) * 100

def poisson(media, gols):
    if media < 0 or gols < 0:
        return 0
    return (
        math.exp(-media) *
        (media ** gols) /
        math.factorial(gols)
    )

def classificar_ev(ev):
    if ev is None:
        return "DADOS INVALIDOS"
    if ev > 0:
        return "EV POSITIVO"
    if ev < 0:
        return "EV NEGATIVO"
    return "EV NEUTRO"


if __name__ == "__main__":
    prob = 0.70
    odd = 1.60

    ev = valor_esperado(prob, odd)

    print("ORBE QUANT")
    print("Probabilidade:", prob * 100, "%")
    print("Odd justa:", odd_justa(prob))
    print("EV:", round(ev, 2), "%")
    print("Classificação:", classificar_ev(ev))
