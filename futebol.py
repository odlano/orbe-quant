
import math


def poisson(media, gols):
    if media < 0:
        return 0

    return (
        math.exp(-media) *
        media ** gols /
        math.factorial(gols)
    )


def analisar_futebol(media_casa, media_fora):
    if media_casa <= 0 or media_fora <= 0:
        return {"erro": "Medias invalidas"}

    limite = 10

    p_casa = [poisson(media_casa, i) for i in range(limite)]
    p_fora = [poisson(media_fora, i) for i in range(limite)]

    casa = empate = fora = 0
    btts = over15 = over25 = 0

    for g1 in range(limite):
        for g2 in range(limite):
            p = p_casa[g1] * p_fora[g2]

            if g1 > g2:
                casa += p
            elif g1 == g2:
                empate += p
            else:
                fora += p

            if g1 > 0 and g2 > 0:
                btts += p

            if g1 + g2 >= 2:
                over15 += p

            if g1 + g2 >= 3:
                over25 += p

    def percentual(x):
        return round(x * 100, 2)

    return {
        "casa": percentual(casa),
        "empate": percentual(empate),
        "fora": percentual(fora),
        "btts_sim": percentual(btts),
        "over_1_5": percentual(over15),
        "over_2_5": percentual(over25),
        "under_2_5": percentual(1 - over25)
    }


if __name__ == "__main__":
    resultado = analisar_futebol(1.5, 1.2)
    print("ORBE QUANT - FUTEBOL")
    print(resultado)
