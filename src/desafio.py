from src.trilha import obter_trilha


def gerar_desafio(tecnologia: str, nivel: str) -> str:
	info = obter_trilha(tecnologia)
	nivel_formatado = nivel.lower().strip()
	desafios = info.get("desafios", {})

	if nivel_formatado in desafios:
		return (
			f"[{info['nome']} - Nível {nivel_formatado.capitalize()}]\n"
			f"Desafio: {desafios[nivel_formatado]}"
		)

	raise ValueError(
		f"Nível '{nivel}' não encontrado. "
		f"Opções: {list(desafios.keys())}"
	)
