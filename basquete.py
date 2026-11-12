
def validar_equipe(equipe):
    erros = []

    if not equipe.get("nome"):
        erros.append("Nome da equipe ausente")

    if equipe.get("jogos", 0) < 5:
        erros.append("Histórico insuficiente: mínimo de 5 jogos")

    if equipe.get("jogos", 0) > 0:
        if equipe.get("gols_marcados", -1) < 0:
            erros.append("Gols marcados inválidos")

        if equipe.get("gols_sofridos", -1) < 0:
            erros.append("Gols sofridos inválidos")

    return {
        "valido": len(erros) == 0,
        "erros": erros
    }


def validar_partida(casa, visitante):
    resultado_casa = validar_equipe(casa)
    resultado_visitante = validar_equipe(visitante)

    return {
        "aprovado": (
            resultado_casa["valido"]
            and resultado_visitante["valido"]
        ),
        "mandante": resultado_casa,
        "visitante": resultado_visitante
    }
