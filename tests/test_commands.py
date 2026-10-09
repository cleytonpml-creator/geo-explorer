import pytest

from src.certificado import gerar_certificado
from src.desafio import gerar_desafio
from src.trilha import obter_trilha


def test_obter_trilha_sucesso():
    trilha = obter_trilha("python")

    assert "nome" in trilha
    assert len(trilha["modulos"]) > 0


def test_obter_trilha_invalida():
    with pytest.raises(ValueError):
        obter_trilha("tecnologia_inexistente")


def test_gerar_desafio_sucesso():
    mensagem = gerar_desafio("python", "iniciante")

    assert "Desafio:" in mensagem


def test_gerar_certificado():
    certificado = gerar_certificado("Aluno Teste", "cybersecurity")

    assert "ALUNO TESTE" in certificado
    assert "CERTIFICADO DE CONCLUSÃO" in certificado
