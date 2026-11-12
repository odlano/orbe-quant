
from classificador_ev import analisar_oportunidade
from gestao_risco import calcular_entrada


def gerar_relatorio(probabilidades, odds, banca):

    oportunidades = []

    for mercado, percentual in probabilidades.items():

        odd = odds.get(mercado)

        if odd is None:
            continue

        if not 0 < percentual < 100:
            continue

        probabilidade = percentual / 100

        analise = analisar_oportunidade(
            probabilidade,
            odd
        )

        risco = calcular_entrada(
            banca,
            probabilidade,
            odd,
            percentual_risco=1.0
        )

        oportunidades.append({
            "mercado": mercado,
            "odd": odd,
            "analise": analise,
            "risco": risco
        })

    oportunidades.sort(
        key=lambda x: x["analise"]["valor_esperado"],
        reverse=True
    )

    return oportunidades


if __name__ == "__main__":

    probabilidades = {
        "Over 1.5": 78,
        "BTTS": 65,
        "Over 2.5": 55
    }

    odds = {
        "Over 1.5": 1.50,
        "BTTS": 1.80,
        "Over 2.5": 2.00
    }

    relatorio = gerar_relatorio(
        probabilidades,
        odds,
        banca=1000
    )

    print("ORBE QUANT")
    print("RELATORIO DE OPORTUNIDADES")

    for item in relatorio:
        print("----------------------")
        print("Mercado:", item["mercado"])
        print("Odd:", item["odd"])
        print("Analise:", item["analise"])
        print("Gestao:", item["risco"])
