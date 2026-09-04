# 💡 Calculadora de Consumo de Energia

Programa que calcula o consumo mensal de um aparelho elétrico.

---

🛠️ Tecnologias: 
Python 3.14.3
VS Code
Git

---

## 📋 Descrição

Este programa em Python ajuda você a:
- Calcular o **consumo mensal em kWh** de um aparelho
- Estimar o **custo em reais** com base no preço do kWh (consulte o preço(kWh) na concessionária local)
- Planejar a redução de gastos na conta de luz

---

## ⚡ Funcionalidades

- ✅ Cálculo do consumo mensal (kWh)
- ✅ Cálculo do custo estimado (R$)

---

## Como usar

1. Execute o programa: `python app.py`
2. Digite o nome do aparelho
3. Digite a potência em watts*
4. Digite as horas de uso por dia

*Para consultar a potência dos aparelhos, consulte o link: 
[Cooperluz - Tabela de Consumo](https://www.cooperluz.com.br/tabela-de-consumo/)

---

## Exemplo

Constantes utilizadas:

30 → Dias no mês
1000 → Conversão de Watts para kWh
valor_kwh → R$ 0,79 (preço ENEL - concessionária local)

**Entrada:**

Qual o nome do aparelho: Geladeira
Qual a potência do aparelho: 150
Qual o tempo médio de uso: 8

**Processamento**

O programa calcula o consumo mensal usando a fórmula:

consumo_mensal = (150 * 8 * 30) / 1000  # 36.0 kWh/mês
custo_estimado = 36.0 * 0.79             # R$ 28.44

**Saída:**

Aparelho: Geladeira
Potência: 150 W
Uso diário: 8.0 horas
Consumo estimado: 36.0 kWh/mês
Custo estimado: R$ 28.44/mês

--- 

## 👤 Autor

**Raul Barbosa**

- GitHub: [@oraulbarbosa](https://github.com/oraulbarbosa)

---

## 📄 Licença

Este projeto está sob a licença MIT.