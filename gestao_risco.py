
def calcular_entrada(
    banca,
    probabilidade,
    odd,
    percentual_risco=1.0
):
    if banca <= 0:
        return {"erro": "Banca invalida"}

    if not 0 < probabilidade < 1:
        return {"erro": "Probabilidade invalida"}

    if odd <= 1:
        return {"erro": "Odd invalida"}

    if not 0 < percentual_risco <= 1:
        return {"erro": "Risco deve ser entre 0 e 1%"}

    ev = (probabilidade * odd - 1)

    if ev <= 0:
        return {
            "classificacao": "NAO ENTRAR",
            "motivo": "Valor esperado nao positivo",
            "entrada": 0
        }

    # Kelly fracionado: utiliza 25% do Kelly integral
    kelly = (probabilidade * odd - 1) / (odd - 1)

    kelly_conservador = max(0, kelly * 0.25)

    limite = banca * percentual_risco / 100

    entrada = min(
        banca * kelly_conservador,
        limite
    )

    return {
        "banca": round(banca, 2),
        "probabilidade": round(probabilidade * 100, 2),
        "odd": odd,
        "ev_percentual": round(ev * 100, 2),
        "entrada_sugerida": round(entrada, 2),
        "risco_percentual": percentual_risco
    }


if __name__ == "__main__":

    resultado = calcular_entrada(
        banca=1000,
        probabilidade=0.65,
        odd=1.80,
        percentual_risco=1.0
    )

    print("ORBE QUANT - GESTAO DE RISCO")
    print(resultado)
