
def analisar_oportunidade(probabilidade, odd):

    if not 0 < probabilidade < 1:
        return {"erro": "Probabilidade invalida"}

    if odd <= 1:
        return {"erro": "Odd invalida"}

    odd_justa = 1 / probabilidade

    ev = (probabilidade * odd - 1) * 100

    if ev >= 10:
        classificacao = "EV+ FORTE"
    elif ev > 0:
        classificacao = "EV+ MODERADO"
    else:
        classificacao = "EV NEGATIVO"

    return {
        "probabilidade": round(probabilidade * 100, 2),
        "odd_oferecida": odd,
        "odd_justa": round(odd_justa, 2),
        "valor_esperado": round(ev, 2),
        "classificacao": classificacao
    }


if __name__ == "__main__":

    probabilidade = 0.70
    odd = 1.60

    resultado = analisar_oportunidade(
        probabilidade,
        odd
    )

    print("ORBE QUANT - ANALISE EV+")
    print(resultado)
