import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# =========================================================
# CONFIGURAÇÃO
# =========================================================

load_dotenv()

MODEL = "meta/llama-3.1-8b-instruct"

SYSTEM_PROMPT = """
Você é um assistente de inteligência artificial geral.

Seu objetivo é ajudar o usuário com qualquer tipo de dúvida,
fornecendo respostas claras, úteis e bem estruturadas.

Regras:
- Responda em português quando o usuário escrever em português.
- Seja objetivo e claro.
- Não invente informações.
- Caso não saiba algo, informe a limitação.
"""

# =========================================================
# CLIENTE NVIDIA
# =========================================================

@st.cache_resource
def get_client():
    api_key = os.getenv("NVIDIA_API_KEY")

    if not api_key:
        raise Exception("NVIDIA_API_KEY não configurada no .env")

    return OpenAI(
        api_key=api_key,
        base_url="https://integrate.api.nvidia.com/v1"
    )

client = get_client()

# =========================================================
# CHAMADA AO MODELO (STREAMING SEGURO)
# =========================================================

def ask_model(messages):
    try:
        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            stream=True
        )

        response_text = ""
        placeholder = st.empty()

        for chunk in stream:

            if (
                not chunk
                or not hasattr(chunk, "choices")
                or len(chunk.choices) == 0
            ):
                continue

            delta = chunk.choices[0].delta

            if hasattr(delta, "content") and delta.content:
                response_text += delta.content
                placeholder.markdown(response_text)

        return response_text

    except Exception as e:
        return f"Erro: {str(e)}"

# =========================================================
# STREAMLIT CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Chatbot Inteligente")

# =========================================================
# SIDEBAR (RESTAURADA)
# =========================================================

with st.sidebar:
    st.header("Configuração")

    st.write(f"Modelo atual: `{MODEL}`")

    st.divider()

    if st.button("🗑️ Nova conversa"):

        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "Olá! Como posso ajudar você?"}
        ]

        st.rerun()

# =========================================================
# MEMÓRIA DA SESSÃO
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Olá! Como posso ajudar você?"}
    ]

# =========================================================
# EXIBIR HISTÓRICO
# =========================================================

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================================================
# INPUT
# =========================================================

user_input = st.chat_input("Digite sua mensagem...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        answer = ask_model(st.session_state.messages)
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )