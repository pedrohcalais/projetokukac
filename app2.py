import streamlit as st
import json

# Função para carregar perguntas do arquivo JSON
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["questions"]

# Função para salvar os resultados em um arquivo JSON
def save_results(questions, responses, file_path):
    results = {
        "questions_and_answers": [
            {"question": q["question"], "answer": r} for q, r in zip(questions, responses)
        ],
        "correct_answers_count": calculate_correct_answers(questions, responses)
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    return results

# Função para calcular respostas corretas
def calculate_correct_answers(questions, responses):
    correct_count = 0
    for question, response in zip(questions, responses):
        correct_answers = question.get("correct_answer", [])
        
        # Garantir que `correct_answers` seja uma lista
        if not isinstance(correct_answers, list):
            correct_answers = [correct_answers]
        
        # Verificar se a resposta do usuário está na lista de respostas corretas
        user_answer = response.strip().lower()
        correct_answers = [answer.strip().lower() for answer in correct_answers]
        
        if user_answer in correct_answers:
            correct_count += 1
    return correct_count


# Inicializar o estado da aplicação
if "step" not in st.session_state:
    st.session_state.step = 0
if "messages" not in st.session_state:
    st.session_state.messages = []
if "responses" not in st.session_state:
    st.session_state.responses = []

# Carregar as perguntas do arquivo JSON
questions = load_questions("questions.json")

# Exibir o histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Exibir a pergunta atual com base no passo (step)
if st.session_state.step < len(questions):
    question = questions[st.session_state.step]
    
    # Exibir a pergunta na interface
    with st.chat_message("assistant"):
        st.markdown(question["question"])

    user_response = None

    if question["type"] == "open":
        # Pergunta aberta
        user_response = st.text_input("Sua resposta:")
    elif question["type"] == "multiple_choice":
        # Pergunta de múltipla escolha
        options = question["options"]
        user_response = st.radio("Escolha uma opção:", options)
    elif question["type"] == "true_false":
        # Pergunta de verdadeiro ou falso
        user_response = st.radio("Escolha:", ["Verdadeiro", "Falso"])

    # Processar a resposta apenas ao clicar no botão "Enviar"
    if st.button("Enviar", key=f"send_button_{st.session_state.step}"):
        if user_response:
            st.session_state.messages.append({"role": "user", "content": user_response})
            st.session_state.responses.append(user_response.strip())
            st.session_state.step += 1

# Finalizar o questionário
else:
    correct_answers = calculate_correct_answers(questions, st.session_state.responses)
    st.chat_message("assistant").markdown("Obrigado por responder ao questionário!")
    st.success(f"Você acertou {correct_answers} de {len(questions)} questões!")

    # Salvar resultados em um arquivo JSON
    results_file = "results.json"
    save_results(questions, st.session_state.responses, results_file)

    # Exibir botão para baixar os resultados
    with open(results_file, "rb") as f:
        st.download_button(
            label="Baixar resultados",
            data=f,
            file_name="resultados_questionario.json",
            mime="application/json"
        )
