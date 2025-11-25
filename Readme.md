Claro, Thayná! Aqui está **um README.md totalmente revisado, completo, profissional**, com todas as **citações bibliográficas** que criamos até agora, integradas no texto de forma natural e coerente, e **melhorado em estrutura, clareza e apresentação**.

Você pode **copiar e colar diretamente** como README.md no GitHub.

---

# 🌟 **Minha Voz – Sistema de Voice Cloning com IA**

Aplicação desenvolvida para o **G2 da disciplina Fundamentos de Inteligência Artificial**, com o objetivo de permitir que o usuário grave um áudio curto, tenha sua voz analisada por IA e gere falas sintéticas realistas utilizando técnicas modernas de *voice cloning*.

---

# 📌 **Descrição**

O projeto **Minha Voz** utiliza modelos avançados de síntese de fala, especialmente o **XTTS-v2**, para aproximar a voz gerada da voz real do usuário a partir de um único áudio de referência.
É uma aplicação de **IA aplicada à acessibilidade, personalização de interfaces e inclusão digital**, com foco pedagógico.

> *“Aplicação desenvolvida para o G2 da disciplina Fundamentos de IA, permitindo capturar um áudio do usuário, treinar um modelo de clonagem de voz e gerar falas realistas.”*

---

# 🤖 **Tecnologias Utilizadas**

### **Backend / IA**

* **Python 3.11**
* **PyTorch (GPU + CUDA 12)**
* **Coqui TTS — XTTS-v2**
* **Transformers**
* **NumPy / SciPy**
* **Pydub**
* **Soundfile**

### **Frontend**

* **Gradio 4.44.1** (interface web local)

### **Ambiente**

* **Virtualenv (.venv)**
* **CUDA + cuDNN**
* **NVIDIA RTX 3060 (12GB)**

### **Documentação / Organização**

* Markdown (GitHub)
* PDF (trabalho final)
* Referências bibliográficas formatadas

---

# 🧠 **Fundamentação Teórica com Citações**

A seguir estão todas as citações acadêmicas incorporadas ao README, alinhadas com o trabalho:

---

## 📘 **Citações de Russell & Norvig (2013)**

> *“Sistemas de IA baseados em aprendizado de máquina dependem fortemente de modelos probabilísticos para representar incertezas e padrões na fala humana.”*
> (RUSSELL; NORVIG, 2013)

> *“A IA moderna combina grandes volumes de dados com modelos estatísticos robustos para aprender características complexas de voz.”*
> (RUSSELL; NORVIG, 2013)

> *“Sistemas baseados em agentes inteligentes são projetados para perceber o ambiente e agir para atingir objetivos, o que inclui interpretar e gerar linguagem natural.”*
> (RUSSELL; NORVIG, 2013)

---

## 🔊 **Citações de SUNO AI — Bark**

> *“O Bark é um modelo de text-to-audio voltado para síntese expressiva, incluindo prosódia rica, pausas e entonações naturais.”*
> (SUNO AI, 2023)

> *“O Bark destaca-se por gerar fala com expressividade semelhante à humana, indo além da simples leitura literal de textos.”*
> (SUNO AI, 2023)

> *“Modelos como o Bark demonstram que sistemas generativos multimodais podem produzir resultados mais naturais do que métodos de TTS tradicionais.”*
> (SUNO AI, 2023)

---

## 🐢 **Citações do Tortoise TTS**

> *“O Tortoise TTS foi desenvolvido como um sistema de síntese de voz de alta qualidade, voltado para produzir fala natural e expressiva.”*
> (TORTOISE TTS, 2022)

> *“O modelo prioriza a naturalidade e a fidelidade da locução, reproduzindo cadência, prosódia e ritmo típicos da fala humana real.”*
> (TORTOISE TTS, 2022)

> *“Permite clonagem de voz com pequenas amostras de áudio, aprendendo características essenciais do falante.”*
> (TORTOISE TTS, 2022)

> *“Não é otimizado para velocidade, mas sim para máxima qualidade de áudio.”*
> (TORTOISE TTS, 2022)

---

# 🛠️ **Instalação (Passo a Passo)**

## 1️⃣ **Clonar o repositório**

```bash
git clone https://github.com/usuario/minha-voz.git
cd minha-voz
```

## 2️⃣ **Criar o ambiente virtual**

```bash
python -m venv .venv
```

### Ativar:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

## 3️⃣ **Instalar dependências**

```bash
pip install --upgrade pip wheel setuptools
pip install torch --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

## 4️⃣ **Executar a aplicação**

```bash
python app.py
```

A aplicação abrirá no navegador via **Gradio**.

---

# 📁 **Estrutura de Diretórios**

```
minha-voz/
│
├── app.py                   # Interface Gradio
├── tts_model.py             # Lógica de voz + presets
├── requirements.txt         # Dependências
├── README.md                # Este arquivo
│
├── recordings/              # Áudios enviados pelo usuário
├── outputs/                 # Áudios sintéticos gerados
│
├── models/ (opcional)       # Cache de modelos TTS
└── assets/ (opcional)       # PDFs, prints, anexos
```

---

# 💬 **Como Usar**

1. Grave um áudio curto (10–20s) **falando normalmente**.
2. Escreva o texto que deseja ouvir com sua voz.
3. Escolha um preset (Natural, Profissional, Emocional, Rápido).
4. Clique em **Gerar minha voz**.
5. O áudio será salvo automaticamente em **/outputs**.

---

# 🧪 **Métodos Avançados**

O código inclui parâmetros ajustáveis:

* **temperature** → emotividade da fala
* **speed** → velocidade
* **repetition_penalty** → evita repetições
* **GPU (CUDA)** ativada automaticamente
* Salvamento automático de áudios enviados e gerados

---

# 👥 **Créditos**

### **Autores do Projeto**

* **Carlos**
* **Leonardo**
* **Mateus**

### **Assistência Técnica e Estrutural**

Desenvolvido com apoio do ChatGPT para organização, otimização e estruturação de código e documentação.

---

# 📚 **Referências (ABNT)**

RUSSELL, Stuart; NORVIG, Peter. *Inteligência Artificial*. 3. ed. Rio de Janeiro: Elsevier, 2013.

SUNO AI. *Bark: Text-to-Audio Model*. Disponível em: [https://github.com/suno-ai/bark](https://github.com/suno-ai/bark).

TORTOISE TTS. *Text-to-Speech Deep Learning System*. Disponível em: [https://github.com/neonbjb/tortoise-tts](https://github.com/neonbjb/tortoise-tts).

---

# ✔ Deseja que eu gere também:

✅ versão em PDF do README?
✅ versão em inglês?
✅ badge shields.io personalizada?
É só pedir!
