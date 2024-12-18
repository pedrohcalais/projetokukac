# 📋 Aplicação de Questionário Interativo com Streamlit

Esta aplicação é um **questionário interativo** desenvolvido em **Python** utilizando o **Streamlit**. Ela permite que os usuários respondam a perguntas de diferentes tipos (abertas, múltipla escolha e verdadeiro/falso) e, ao final, exibe o número de respostas corretas.

---

## 🚀 **Funcionalidades**

- Carrega perguntas de um arquivo JSON.
- Suporta **3 tipos de perguntas**:
   - Aberta (resposta livre)
   - Múltipla escolha
   - Verdadeiro ou falso
- Calcula o total de respostas corretas.
- Gera um arquivo `JSON` com os resultados.
- Permite baixar os resultados ao final do questionário.

---

## 🛠️ **Pré-requisitos**

Para executar a aplicação localmente, você precisará ter instalado:

1. **Python** (versão 3.8 ou superior)
   - Baixe o Python em [python.org](https://www.python.org/).
2. **Streamlit**
   - Instale o Streamlit com o comando:
     ```bash
     pip install streamlit
     ```

---

##  **Organização do Projeto**

```plaintext
.
├── app2.py                # Código principal da aplicação
├── questions.json         # Arquivo com as perguntas
├── results.json           # Arquivo gerado com os resultados
└── README.md              # Documentação do projeto
