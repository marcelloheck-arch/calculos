# Calculadora de Juros — Simples e Compostos

## 1. Introdução

Esta calculadora em Python permite calcular juros simples e juros compostos de forma interativa via linha de comando. É uma ferramenta educativa e prática para simulações financeiras rápidas, com validação de entradas e formatação monetária em Real (R$).

- **Juros simples**: juros calculados apenas sobre o capital inicial.
- **Juros compostos**: juros calculados sobre o capital mais juros acumulados (capitalização).


## 2. Pré-requisitos

- Python 3.8 ou superior.
- Verifique a versão do Python com:

```powershell
python --version
```

Se o Python não estiver instalado, baixe e instale a versão apropriada nos sites oficiais:

- Windows / macOS / Linux: https://www.python.org/downloads/

```bash
python --version
```

Se o Python não estiver instalado, baixe e instale a versão apropriada nos sites oficiais:

- Windows / macOS / Linux: https://www.python.org/downloads/


## 3. Instalação Passo a Passo


1. Clone o repositório (substitua pela URL do seu fork se necessário):

```powershell
git clone https://github.com/marcelloheck-arch/calculos.git
```

2. Entre na pasta do projeto:

```powershell
cd C:\Users\marcelo.heck\Desktop\AUTORIZACOES\calculos
```

3. (Opcional) Crie e ative um ambiente virtual (recomendado):

```powershell
python -m venv venv
venv\Scripts\activate
```


## 4. Guia de Uso Completo


### Execução

Execute o programa com:

```powershell
python calculadora_juros.py
```

Menu principal:

- `1` — Calcular juros simples
- `2` — Calcular juros compostos
- `3` — Sair

Entradas solicitadas:

- Capital inicial (ex: `1500` ou `1500,50`)
- Taxa de juros em porcentagem por período (ex: `2.5`)
- Período (número de períodos — pode ser anos, meses, etc.)

Exemplo prático — Juros Simples (passo a passo):

1) Escolha `1` no menu.
2) Informe `Capital inicial: R$ 1000`.
3) Informe `Taxa de juros (% ao período): 5`.
4) Informe `Período (quantidade de períodos): 2`.

Resultado esperado:

- Capital inicial: R$ 1.000,00
- Juros calculados: R$ 100,00
- Montante final: R$ 1.100,00

Exemplo prático — Juros Compostos (passo a passo):

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


## 9. Changelog (versão inicial)

- **v1.0.0** — 2026-02-10
  - Adicionado `calculadora_juros.py` com funcionalidades de juros simples e compostos.
  - Adicionado `README.md`, `LICENSE`, `.gitignore`.


## 10. Como contribuir

1. Crie um fork ou clone este repositório.
2. Abra uma branch para sua alteração:

```powershell
git checkout -b feature/minha-melhoria
```

3. Faça commits claros e pequenos:

```powershell
git add .
git commit -m "Descrição da mudança"
git push origin feature/minha-melhoria
```

4. Abra um Pull Request no GitHub descrevendo a mudança.


## 11. Comandos úteis (commit, tag, push)

Exemplo de commit e push (já executado neste repositório):

```powershell
git init
git add .
git commit -m "Add calculadora de juros, README, .gitignore, LICENSE"
git branch -M main
git remote add origin https://github.com/marcelloheck-arch/calculos.git
git push -u origin main
```

Criar tag anotada e enviar para o remoto (executado):

```powershell
git tag -a v1.0.0 -m "v1.0.0 — calculadora de juros"
git push origin v1.0.0
```


## 12. Licença

Este projeto está sob a licença MIT — veja o arquivo `LICENSE`.


Se precisar, posso também gerar um arquivo `CHANGELOG.md` com histórico mais detalhado ou criar o Release no GitHub (requer token ou `gh`).

## Manual passo a passo (para pessoas leigas)

Este manual foi escrito para alguém que nunca usou o terminal ou Python. Siga cada passo com calma.

1) Abra o Explorador de Arquivos e navegue até a pasta do projeto:

```powershell
C:\Users\marcelo.heck\Desktop\AUTORIZACOES\calculos
```

## Versão Web (deploy estático)

Adicionei uma versão web estática na pasta `web/` com uma interface amigável em `index.html` que pode ser implantada em serviços de hospedagem estática (Vercel, Netlify, GitHub Pages, etc.).

Arquivos principais:

- `web/index.html` — interface da calculadora
- `web/style.css` — estilos
- `web/app.js` — lógica do front-end (valida entradas, calcula juros e formata resultados)

Como implantar no Vercel (passos rápidos):

1. Acesse https://vercel.com e faça login com sua conta GitHub.
2. Clique em "New Project" → "Import Git Repository" → escolha `marcelloheck-arch/calculos`.
3. Nas configurações do projeto, defina o campo "Root Directory" como `web`.
4. Clique em "Deploy". O Vercel irá gerar um link público (ex: https://seu-projeto.vercel.app) onde a calculadora estará acessível.

Observação: também é possível usar Netlify (arrastar a pasta `web`) ou GitHub Pages (configurar branch e pasta `web`).

Se quiser, posso criar um `vercel.json` com configurações padrão e preparar o repositório para deploy automático.

2) Verifique se o Python está instalado:

```powershell
python --version
```

Se aparecer algo como `Python 3.x.x`, continue. Se você receber um erro, instale o Python em https://www.python.org/downloads/ e marque a opção "Add Python to PATH" durante a instalação.

3) Abrir o terminal (PowerShell):

- Clique com o botão direito na pasta `calculos` e escolha "Abrir no Terminal" ou "Abrir janela do PowerShell aqui".

4) Rodar a demonstração automática (sem perguntas):

```powershell
python demo_test.py
```

Você verá várias linhas mostrando o capital inicial, taxa, juros calculados e montante final. Exemplo de saída:

```
Demonstração da Calculadora de Juros — exemplos automáticos
-------------------------------------------
Juros Simples (exemplo)
Capital inicial: R$ 1.000,00
Taxa: 5.0% — Período(s): 2
Juros calculados: R$ 100,00
Montante final:   R$ 1.100,00
```

5) Rodar o programa interativo (se quiser inserir seus próprios valores):

```powershell
python calculadora_juros.py
```

Passo a passo dentro do programa interativo:

- O programa mostrará um menu com as opções `1`, `2` ou `3`.
- Digite `1` para juros simples, `2` para juros compostos ou `3` para sair, e pressione Enter.
- Quando solicitado "Capital inicial: R$", digite o valor (ex: `1000` ou `1500,50`) e pressione Enter.
- Quando solicitado "Taxa de juros (%):", digite a taxa em porcentagem (ex: `5` para 5%).
- Quando solicitado "Período:", digite o número de períodos (por exemplo, anos ou meses) e pressione Enter.

6) Interpretação dos resultados (explicação simples):

- `Capital inicial`: quanto você está investindo ou emprestando agora.
- `Juros calculados`: quanto o dinheiro rendeu a mais durante o período.
- `Montante final`: capital inicial + juros — é o total que você terá no fim.

7) Problemas comuns e soluções rápidas:

- Se o terminal não aceita vírgula, tente usar ponto (ex: `1500.50`).
- Se aparecer erro de sintaxe ao rodar `python`, talvez o Python não esteja instalado ou não esteja no PATH.
- Para cancelar o programa interativo a qualquer momento, pressione `Ctrl+C`.

8) Passos seguintes recomendados para iniciantes:

- Faça várias simulações com valores diferentes para entender a diferença entre juros simples e compostos.
- Anote os resultados em um bloco de notas para comparar montantes por período.

Se quiser, eu posso gerar um PDF com este manual formatado para impressão.

---

## Alterações realizadas agora

- Adicionado `demo_test.py` — script que executa exemplos automáticos e imprime resultados formatados.
- Atualizado `README.md` com o manual passo a passo para iniciantes.

Para enviar estas alterações ao repositório remoto:

```powershell
git add demo_test.py README.md
git commit -m "Add demo_test.py and improve README with manual passo a passo"
git push
```
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
