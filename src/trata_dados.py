import re
import pandas as pd

# Padronizar nomes de clubes
CLUBES = {
    # Brasileiros
    "Botafogo": "Botafogo FR",
    "Botafogo FR": "Botafogo FR",

    "Corinthians": "SC Corinthians",
    "SC Corinthians": "SC Corinthians",

    "Flamengo": "CR Flamengo",
    "CR Flamengo": "CR Flamengo",

    "Bahia": "EC Bahia",
    "EC Bahia": "EC Bahia",

    "Cruzeiro": "Cruzeiro EC",
    "Cruzeiro EC": "Cruzeiro EC",

    "Fortaleza": "Fortaleza EC",
    "Fortaleza EC": "Fortaleza EC",

    "Fluminense": "Fluminense FC",
    "Fluminense FC": "Fluminense FC",

    "Grêmio": "Grêmio FBPA",
    "Grêmio FBPA": "Grêmio FBPA",

    "Internacional": "SC Internacional",
    "SC Internacional": "SC Internacional",

    "Ceará": "Ceará SC",
    "Ceará SC": "Ceará SC",

    "Atlético-MG": "Atlético Mineiro",
    "Atlético Mineiro": "Atlético Mineiro",

    "Bragantino": "RB Bragantino",
    "RB Bragantino": "RB Bragantino",

    "Athletico-PR": "Athletico Paranaense",
    "Athletico Paranaense": "Athletico Paranaense",

    "Palmeiras": "SE Palmeiras",
    "SE Palmeiras": "SE Palmeiras",

    "Santos": "Santos FC",
    "Santos FC": "Santos FC",

    "São Paulo": "São Paulo FC",
    "São Paulo FC": "São Paulo FC",

    "Vasco da Gama": "CR Vasco da Gama",
    "CR Vasco da Gama": "CR Vasco da Gama",

    "Vitória": "EC Vitória",
    "EC Vitória": "EC Vitória",
}


def normalizar(nome):
    nome = nome.strip()
    return CLUBES.get(nome, nome)


# Ler o arquivo de transferências gerado pelo coleta_dados.py
arquivo = "data/raw/transferencias.txt"

dados = []

padrao = re.compile(
    r"Nome:\s*(.*?)\s*-\s*Clube Destino:\s*(.*?)\s*-\s*Clube Origem:\s*(.*)"
)

with open(arquivo, encoding="utf-8") as f:

    for linha in f:

        linha = linha.strip()

        if not linha.startswith("Nome:"):
            continue

        m = padrao.match(linha)

        if not m:
            continue

        jogador = m.group(1).strip()
        destino = normalizar(m.group(2))
        origem = normalizar(m.group(3))

        dados.append({
            "Jogador": jogador,
            "Clube Origem": origem,
            "Clube Destino": destino
        })

# Criar um DataFrame a partir dos dados coletados
df = pd.DataFrame(dados)

df = df.sort_values(
    by=["Jogador", "Clube Origem", "Clube Destino"]
).reset_index(drop=True)

# Salvar os dados organizados em arquivos CSV e Excel
df.to_csv(
    "data/processed/transferencias_organizadas.csv",
    index=False,
    encoding="utf-8-sig"
)

with pd.ExcelWriter(
    "data/processed/transferencias_organizadas.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        index=False,
        sheet_name="Transferências"
    )
# Printar as primeiras linhas do DataFrame e informações sobre o total de transferências e arquivos gerados
print()
print(df.head())

print(f"\nTotal de transferências: {len(df)}")
print("Arquivos gerados:")
print("- transferencias_organizadas.csv")
print("- transferencias_organizadas.xlsx")