from mcp.server.fastmcp import FastMCP

from src.certificado import gerar_certificado as get_certificado
from src.desafio import gerar_desafio as get_desafio
from src.trilha import obter_trilha as get_trilha

mcp = FastMCP("Geo-Explorer")


@mcp.tool()
def trilha(tecnologia: str) -> str:
    """Retorna o plano de estudos/trilha para uma tecnologia."""
    resultado = get_trilha(tecnologia)
    modulos = "\n- ".join(resultado["modulos"])
    return f"Trilha {resultado['nome']}:\n- {modulos}"


@mcp.tool()
def desafio(tecnologia: str, nivel: str) -> str:
    """Gera um desafio de código conforme a tecnologia e nível (iniciante, intermediario, avancado)."""
    return get_desafio(tecnologia, nivel)


@mcp.tool()
def certificado(nome_usuario: str, tecnologia: str) -> str:
    """Gera um certificado fictício de conclusão de trilha."""
    return get_certificado(nome_usuario, tecnologia)


if __name__ == "__main__":
    mcp.run()
