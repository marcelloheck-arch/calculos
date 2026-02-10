"""Script de demonstração não interativo da calculadora de juros.

Este script roda exemplos automáticos e imprime os resultados formatados.
"""
from calculadora_juros import juros_simples, juros_compostos, format_currency


def demo():
    examples = [
        ("Juros Simples (exemplo)", juros_simples, 1000.0, 5.0, 2.0),
        ("Juros Compostos (exemplo)", juros_compostos, 1000.0, 5.0, 2.0),
        ("Juros Simples — outro exemplo", juros_simples, 2500.0, 3.5, 4.0),
        ("Juros Compostos — outro exemplo", juros_compostos, 2500.0, 3.5, 4.0),
    ]

    for title, func, capital, taxa, periodo in examples:
        juros, montante = func(capital, taxa, periodo)
        print("-------------------------------------------")
        print(title)
        print(f"Capital inicial: {format_currency(capital)}")
        print(f"Taxa: {taxa}% — Período(s): {int(periodo) if periodo.is_integer() else periodo}")
        print(f"Juros calculados: {format_currency(juros)}")
        print(f"Montante final:   {format_currency(montante)}")
        print()


if __name__ == "__main__":
    print("Demonstração da Calculadora de Juros — exemplos automáticos\n")
    demo()
