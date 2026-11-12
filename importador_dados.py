
import csv
from pathlib import Path


def importar_csv(caminho, esporte):
    esporte = esporte.lower()

    if esporte not in ["futebol", "basquete"]:
        return {"erro": "Esporte não suportado"}

    caminho = Path(caminho)

    if not caminho.exists():
        return {"erro": "Arquivo não encontrado"}

    campos = (
        ["equipe", "data", "pontos_feitos", "pontos_sofridos"]
        if esporte == "basquete"
        else ["equipe", "data", "gols_marcados", "gols_sofridos"]
    )

    registros = []
    erros = []

    try:
        with open(caminho, "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo)

            if not leitor.fieldnames or not all(
                campo in leitor.fieldnames for campo in campos
            ):
                return {"erro": "Colunas obrigatórias ausentes"}

            for numero, linha in enumerate(leitor, start=2):
                try:
                    equipe = linha["equipe"].strip()
                    data = linha["data"].strip()

                    if not equipe or not data:
                        raise ValueError("Equipe ou data ausente")

                    feitos = int(linha[campos[2]])
                    sofridos = int(linha[campos[3]])

                    if feitos < 0 or sofridos < 0:
                        raise ValueError("Estatística negativa")

                    registros.append({
                        "equipe": equipe,
                        "data": data,
                        campos[2]: feitos,
                        campos[3]: sofridos
                    })

                except (ValueError, TypeError):
                    erros.append({
                        "linha": numero,
                        "motivo": "Dados inválidos"
                    })

    except OSError:
        return {"erro": "Não foi possível ler o arquivo"}

    return {
        "esporte": esporte,
        "registros_importados": len(registros),
        "erros": erros,
        "dados": registros
    }


if __name__ == "__main__":
    print("ORBE QUANT - IMPORTADOR")
    print("Módulo pronto para receber arquivos CSV.")
