# 🤖 AI Chat com NVIDIA NIM + Streamlit (Deploy na Oracle Cloud)

## 📌 Introdução

### 🎯 Objetivo da atividade
O objetivo deste projeto é desenvolver e implantar um chatbot genérico utilizando modelos de linguagem da NVIDIA NIM, integrados a uma aplicação web interativa construída com Streamlit.

### 🌐 Visão geral da solução
A solução consiste em um chat inteligente capaz de interagir com diferentes modelos de linguagem de forma dinâmica, permitindo ao usuário escolher o modelo desejado. O sistema foi implantado em uma máquina virtual na Oracle Cloud Infrastructure (OCI), tornando a aplicação acessível via navegador.

---

## 🖥️ Infraestrutura

### ⚙️ Configuração da máquina virtual
A aplicação foi executada em uma instância na Oracle Cloud Infrastructure (OCI).

### 💻 Sistema operacional utilizado
- Ubuntu Server 22.04 LTS

### 📊 Recursos computacionais
- CPU: 1–2 OCPUs  
- RAM: 1GB a 4GB  
- Armazenamento: padrão OCI (boot volume)  
- Acesso via SSH com chave privada

---

## 🧠 Modelo Escolhido

### 🏷️ Nome do modelo
- meta/llama-3.1-8b-instruct

### 📌 Justificativa da escolha
O modelo Llama 3.1 8B foi escolhido por oferecer um equilíbrio entre desempenho, custo computacional e qualidade das respostas, sendo ideal para execução via API em ambientes cloud.

### ⚡ Principais características
- Modelo otimizado para instruções (instruction-tuned)
- Boa capacidade de generalização
- Baixa latência via NVIDIA NIM API
- Compatível com SDK OpenAI

---

## 🛠️ Desenvolvimento

### 🏗️ Arquitetura da aplicação

Usuário → Streamlit UI → Backend Python → NVIDIA NIM API → LLM → Resposta → UI

### 📦 Bibliotecas utilizadas

streamlit
openai
python-dotenv

## 🔐 Estratégia de gerenciamento de credenciais

As credenciais são armazenadas em um arquivo `.env`:

NVIDIA_API_KEY=sua_chave_aqui

Carregamento seguro:

from dotenv import load_dotenv
load_dotenv()

---

## 🚀 Implantação

### ☁️ Processo de publicação na Oracle Cloud

1. Acesso à VM  
ssh -i ssh-key-2026-03-07.key ubuntu@IP_DA_VM  

2. Envio do projeto  
scp -i ssh-key-2026-03-07.key -r /mnt/c/Users/Gamer/Documents/chatbot_curso ubuntu@IP_DA_VM:/home/ubuntu/chatbot/  

3. Configuração do ambiente  
sudo apt update && sudo apt upgrade -y  
sudo apt install python3 python3-pip python3-venv -y  

4. Criação do ambiente virtual  
python3 -m venv chat  
source chat/bin/activate  

5. Instalação das dependências  
pip install -r requirements.txt  

6. Configuração do .env  
nano .env  
NVIDIA_API_KEY=sua_chave_aqui  

7. Execução da aplicação  
streamlit run app.py --server.address 0.0.0.0 --server.port 8501  

---

## ⚠️ Principais desafios encontrados

- Configuração inicial da VM na Oracle Cloud  
- Ajuste de permissões SSH e autenticação por chave  
- Integração do SDK OpenAI com NVIDIA NIM  
- Exposição da aplicação para acesso externo  
- Transferência de arquivos via SCP/WSL  

---

## 📊 Discussão

### 📖 Lições aprendidas
- Deploy em cloud exige atenção a rede e segurança  
- Streamlit facilita criação rápida de interfaces de IA  
- O uso de .env é essencial para segurança  
- APIs de LLM permitem arquitetura flexível  

### 🚀 Possíveis melhorias futuras
- RAG com documentos  
- Banco de dados para histórico  
- Autenticação de usuários  
- Dockerização  
- CI/CD com GitHub Actions  
- Interface mais avançada  

---

## 📌 Conclusão

Projeto demonstra integração de LLMs via NVIDIA NIM com Streamlit em infraestrutura cloud Oracle, servindo como base para sistemas mais avançados de IA.
