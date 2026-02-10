# Calculadora de Juros — Simples e Compostos

## 1. Introdução

Esta calculadora em Python permite calcular juros simples e juros compostos de forma interativa via linha de comando. É uma ferramenta educativa e prática para simulações financeiras rápidas.

- Juros simples: juros calculados apenas sobre o capital inicial.
- Juros compostos: juros calculados sobre o capital + juros acumulados (capitalização).


## 2. Pré-requisitos

- Python 3.8 ou superior.
- Verifique a versão do Python com:

```bash
python --version
```

Se o Python não estiver instalado, baixe e instale a versão apropriada nos sites oficiais:

- Windows / macOS / Linux: https://www.python.org/downloads/


## 3. Instalação Passo a Passo

1. Clone o repositório:

```bash
git clone <URL_DO_SEU_REPOSITORIO>
```

2. Entre na pasta do projeto:

```bash
cd calculadora
# ou para este projeto específico
cd caminho/para/calculos
```

3. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```


## 4. Guia de Uso Completo

Execute o programa com:

```bash
python calculadora_juros.py
```

Menu principal:

- `1` — Calcular juros simples
- `2` — Calcular juros compostos
- `3` — Sair

Entradas solicitadas:

- Capital inicial (ex: 1500 ou 1500,50)
- Taxa de juros em porcentagem por período (ex: 2.5)
- Período (número de períodos — pode ser anos, meses, etc.)

Exemplo prático — Juros Simples:

1) Escolha `1` no menu.
2) Informe `Capital inicial: R$ 1000`.
3) Informe `Taxa de juros (% ao período): 5`.
4) Informe `Período (quantidade de períodos): 2`.

Resultado esperado:

- Capital inicial: R$ 1.000,00
- Juros calculados: R$ 100,00
- Montante final: R$ 1.100,00

Exemplo prático — Juros Compostos:

1) Escolha `2` no menu.
2) Informe `Capital inicial: R$ 1000`.
3) Informe `Taxa de juros (% por período): 5`.
4) Informe `Período (número de períodos): 2`.

Resultado esperado:

- Capital inicial: R$ 1.000,00
- Juros calculados: R$ 102,50
- Montante final: R$ 1.102,50


## 5. Conceitos Financeiros

- Juros simples: J = C × i × t
  - Exemplo: C=1000, i=5% (0.05), t=2 → J = 1000 × 0.05 × 2 = 100

- Juros compostos: M = C × (1 + i)^t
  - Exemplo: C=1000, i=5% (0.05), t=2 → M = 1000 × (1.05)^2 = 1102.5

- Diferença principal: nos juros compostos, os juros anteriores também rendem.


## 6. Boas Práticas

- Verifique se a taxa está na mesma unidade do período (ex: taxa mensal com período em meses).
- Use números positivos para capital, taxa e período.
- Evite entradas com caracteres inválidos; o programa orienta sobre formatação.


## 7. Solução de Problemas

- Erro de sintaxe / não inicia: verifique a versão do Python.
- Entrada inválida: insira números, utilize vírgula ou ponto para decimais.
- Se o programa travar: pressione `Ctrl+C` para interromper.

Como reportar bugs: abra uma issue no repositório com passos para reproduzir.


## 8. Exemplos de Uso Real

- Cenário 1 — Poupança (juros simples): quando o produto aplica juros fixos sobre capital inicial.
- Cenário 2 — Renda fixa com capitalização (juros compostos): quando juros são reinvestidos.

Tabelas comparativas podem ser feitas exportando os resultados e comparando colunas de montante por período.


## 9. Contribuições

Contribuições são bem-vindas. Siga estas diretrizes:

- Abra uma issue antes de grandes mudanças.
- Use commits pequenos e significativos.
- Siga PEP 8 para formatação do código.


## 10. Licença e Contato

Este projeto está sob a licença MIT (veja o arquivo LICENSE).

Contato: abra uma issue no repositório ou envie e-mail para o mantenedor.

---

### Demonstração (exemplo de execução)

Tela inicial:

```
Calculadora de Juros — Simples e Compostos
Dica: use pontos ou vírgulas para decimais. Ex: 1500.50 ou 1500,50

=== Calculadora de Juros ===
1) Juros Simples
2) Juros Compostos
3) Sair

Escolha uma opção (1-3):
```

Exemplo completo (juros simples):

```
Escolha: 1
Capital inicial: R$ 1000
Taxa de juros (% ao período): 5
Período (quantidade de períodos): 2

Resultado:
Capital inicial: R$ 1.000,00
Juros calculados: R$ 100,00
Montante final:   R$ 1.100,00
```

Exemplo completo (juros compostos):

```
Escolha: 2
Capital inicial: R$ 1000
Taxa de juros (% por período): 5
Período (número de períodos): 2

Resultado:
Capital inicial: R$ 1.000,00
Juros calculados: R$ 102,50
Montante final:   R$ 1.102,50
```
