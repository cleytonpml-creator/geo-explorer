import sys

from src.certificado import gerar_certificado
from src.desafio import gerar_desafio
from src.trilha import obter_trilha


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python main.py trilha <tecnologia>")
        print("  python main.py desafio <tecnologia> <nivel>")
        print("  python main.py certificado <nome_usuario> <tecnologia>")
        return

    comando = sys.argv[1].lower()

    try:
        if comando == "trilha":
            if len(sys.argv) < 3:
                print("Informe a tecnologia. Ex: python main.py trilha python")
                return

            tecnologia = sys.argv[2]
            resultado = obter_trilha(tecnologia)
            print(f"\n Trilha: {resultado['nome']}")
            print("Módulos:")
            for modulo in resultado["modulos"]:
                print(f"  • {modulo}")

        elif comando == "desafio":
            if len(sys.argv) < 4:
                print(
                    "Informe tecnologia e nível. "
                    "Ex: python main.py desafio python iniciante"
                )
                return

            tecnologia = sys.argv[2]
            nivel = sys.argv[3]
            print(f"\n{gerar_desafio(tecnologia, nivel)}")

        elif comando == "certificado":
            if len(sys.argv) < 4:
                print(
                    "Informe o nome e a tecnologia. "
                    "Ex: python main.py certificado 'Seu Nome' python"
                )
                return

            nome = sys.argv[2]
            tecnologia = sys.argv[3]
            print(f"\n{gerar_certificado(nome, tecnologia)}")

        else:
            print(f"Comando desconhecido: {comando}")
    except Exception as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
