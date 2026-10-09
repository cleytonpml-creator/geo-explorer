import json
import os


DATA_PATH = os.path.join(
	os.path.dirname(__file__), "..", "data", "trilhas-aprendizado.json"
)


def carregar_dados():
	with open(DATA_PATH, "r", encoding="utf-8") as arquivo:
		return json.load(arquivo)


def obter_trilha(tecnologia: str) -> dict:
	dados = carregar_dados()
	tecnologia_normalizada = tecnologia.lower().strip()

	if tecnologia_normalizada in dados:
		return dados[tecnologia_normalizada]

	raise ValueError(
		f"Tecnologia '{tecnologia}' não encontrada. "
		f"Opções: {list(dados.keys())}"
	)
