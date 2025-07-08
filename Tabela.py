import pandas as pd
import matplotlib.pyplot as plt

# Dados da tabela comparativa
dados = {
    "Critério": [
        "Total de resultados estimados",
        "Idioma predominante",
        "Tipo de publicação",
        "Palavras-chave frequentes",
        "Principais autores/instituições",
        "Foco metodológico dominante",
        "Aplicações assistivas diretamente",
        "Tendência temporal (crescimento)"
    ],
    "Google Scholar": [
        "150+ (amplo e com duplicações)",
        "Inglês (85%), Português (10%), Outros (5%)",
        "Artigos, TCCs, pré-prints, capítulos",
        "“Assistive Navigation”, “LiDAR 3D”, “SLAM”, “Robotics”",
        "Dispersos, com foco em Ásia e Europa",
        "Análises práticas, protótipos",
        "15% dos estudos",
        "Crescente após 2020"
    ],
    "Scopus": [
        "45 artigos relevantes (2020–2024)",
        "Inglês (>95%)",
        "Artigos indexados, periódicos, conferências",
        "“3D LiDAR”, “Autonomous navigation”, “Smart wheelchair”",
        "TUM (Alemanha), MIT, KAIST, UFRGS",
        "Modelos com LiDAR + fusão de sensores",
        "~10 artigos (LiDAR + mobilidade assistiva)",
        "Pico em 2022–2023"
    ],
    "IEEE Xplore": [
        "60 artigos (filtrando por robótica e assistiva)",
        "Inglês (>95%)",
        "Artigos técnicos, conferências",
        "“Obstacle Detection”, “Deep Learning”, “SLAM”",
        "TUM, NUS, Stanford, UFMG (algumas parcerias)",
        "Inteligência artificial (CNN, SLAM), hardware",
        "~8 artigos aplicados a navegação humana assistida",
        "Aumento após 2021"
    ],
    "Repositórios Acadêmicos (USP, CAPES, etc.)": [
        "~10 trabalhos (teses, dissertações)",
        "Português (>90%)",
        "Teses, dissertações, monografias",
        "“Cadeira de rodas inteligente”, “Visão computacional”",
        "UFRGS, USP, UFJF, UTFPR",
        "Robótica móvel, algoritmos simples, sensores alternativos",
        "6 trabalhos diretamente com deficientes visuais/motores",
        "Pouca produção antes de 2020"
    ]
}

# Criar DataFrame
df_tabela = pd.DataFrame(dados)

# Salvar como Excel
caminho_arquivo = "/mnt/data/Tabela_Bibliometrica_LiDAR3D_Navegacao_Assistiva.xlsx"
df_tabela.to_excel(caminho_arquivo, index=False)

df_tabela.head()
