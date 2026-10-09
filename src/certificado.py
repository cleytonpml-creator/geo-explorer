import hashlib
from datetime import datetime

from src.trilha import obter_trilha


def gerar_certificado(nome_usuario: str, tecnologia: str) -> str:
    info = obter_trilha(tecnologia)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    chave = f"{nome_usuario.strip()}:{tecnologia.strip().lower()}"
    codigo = hashlib.sha256(chave.encode("utf-8")).hexdigest()[:8]

    linhas = [
        "============================================================",
        "                    CERTIFICADO DE CONCLUSÃO",
        "============================================================",
        f"Certificamos que {nome_usuario.strip().upper()} concluiu com êxito a trilha:",
        "",
        f">>> {info['nome']} <<<",
        "",
        "Módulos Concluídos:",
        *(f"- {modulo}" for modulo in info.get("modulos", [])),
        "",
        f"Data de Emissão: {data_atual}",
        f"Código de Autenticação: GEO-{codigo}",
        "============================================================",
    ]

    return "\n".join(linhas)
