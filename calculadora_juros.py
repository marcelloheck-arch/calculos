"""Calculadora de Juros (Simples e Compostos)

Arquivo principal com interface CLI interativa.
"""
from __future__ import annotations

from typing import Tuple


def format_currency(value: float) -> str:
    """Formata valor numérico para formato monetário brasileiro.

    Exemplo: 1234.5 -> 'R$ 1.234,50'
    """
    # Formata com separador de milhares e vírgula decimal
    s = f"{value:,.2f}"
    # Troca separadores para o padrão BR
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def juros_simples(capital: float, taxa_percent: float, periodo: float) -> Tuple[float, float]:
    """Calcula juros simples.

    Fórmula: J = C × i × t

    Retorna uma tupla (juros, montante).
    """
    if capital < 0:
        raise ValueError("Capital não pode ser negativo")
    if taxa_percent < 0:
        raise ValueError("Taxa não pode ser negativa")
    if periodo < 0:
        raise ValueError("Período não pode ser negativo")

    i = taxa_percent / 100.0
    juros = capital * i * periodo
    montante = capital + juros
    return juros, montante


def juros_compostos(capital: float, taxa_percent: float, periodo: float) -> Tuple[float, float]:
    """Calcula juros compostos.

    Fórmula: M = C × (1 + i)^t

    Retorna uma tupla (juros, montante).
    """
    if capital < 0:
        raise ValueError("Capital não pode ser negativo")
    if taxa_percent < 0:
        raise ValueError("Taxa não pode ser negativa")
    if periodo < 0:
        raise ValueError("Período não pode ser negativo")

    i = taxa_percent / 100.0
    montante = capital * ((1 + i) ** periodo)
    juros = montante - capital
    return juros, montante


def parse_positive_number(prompt: str, allow_zero: bool = True) -> float:
    """Lê um número do usuário validando positivo (ou zero se permitido).

    Lança ValueError se entrada inválida repetidas vezes.
    """
    while True:
        s = input(prompt).strip().replace(" ", "")
        try:
            value = float(s.replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número válido (ex: 1000, 5.5)")
            continue

        if value < 0 or (not allow_zero and value == 0):
            print("Por favor, informe um valor positivo.")
            continue
        return value


def mostrar_resultado(capital: float, juros: float, montante: float) -> None:
    """Exibe resultado formatado na tela."""
    print("\nResultado:")
    print(f"Capital inicial: {format_currency(capital)}")
    print(f"Juros calculados: {format_currency(juros)}")
    print(f"Montante final:   {format_currency(montante)}\n")


def menu() -> None:
    """Menu principal da calculadora."""
    while True:
        print("\n=== Calculadora de Juros ===")
        print("1) Juros Simples")
        print("2) Juros Compostos")
        print("3) Sair")

        opc = input("Escolha uma opção (1-3): ").strip()
        if opc == "1":
            print("\n--- Juros Simples ---")
            capital = parse_positive_number("Capital inicial: R$ ")
            taxa = parse_positive_number("Taxa de juros (% ao período): ")
            periodo = parse_positive_number("Período (quantidade de períodos): ", allow_zero=False)
            try:
                juros, montante = juros_simples(capital, taxa, periodo)
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            mostrar_resultado(capital, juros, montante)

        elif opc == "2":
            print("\n--- Juros Compostos ---")
            capital = parse_positive_number("Capital inicial: R$ ")
            taxa = parse_positive_number("Taxa de juros (% por período): ")
            periodo = parse_positive_number("Período (número de períodos): ", allow_zero=False)
            try:
                juros, montante = juros_compostos(capital, taxa, periodo)
            except ValueError as e:
                print(f"Erro: {e}")
                continue
            mostrar_resultado(capital, juros, montante)

        elif opc == "3" or opc.lower() in ("s", "q"):
            print("Saindo. Obrigado por usar a calculadora.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    print("Calculadora de Juros — Simples e Compostos")
    print("Dica: use pontos ou vírgulas para decimais. Ex: 1500.50 ou 1500,50")
    try:
        menu()
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário. Até logo!")
