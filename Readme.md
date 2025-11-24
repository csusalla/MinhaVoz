Perfeito, Thayná!
Aqui está o **README.md completo, profissional, organizado e pronto para subir no GitHub**, já formatado em Markdown e contendo tudo o que você pediu: descrição, tecnologias, passos de instalação, execução, árvore de diretórios e créditos.

Você só precisa **copiar e colar em um arquivo chamado `README.md`** dentro do seu projeto.

---

# 📘 **README.md — Projeto *Minha Voz***

````markdown
# 🎙️ Minha Voz  
Aplicação desenvolvida para o G2 da disciplina **Fundamentos de Inteligência Artificial**, permitindo capturar um áudio do usuário, utilizar modelos avançados de IA para *clonagem de voz* e gerar falas sintéticas altamente realistas.

---

## 🚀 Objetivo
O projeto **Minha Voz** foi criado para demonstrar, na prática, como modelos modernos de *Text-to-Speech* (TTS) e *voice cloning* podem reproduzir o timbre, melodia e estilo vocal de um usuário a partir de um pequeno áudio de referência.

---

## 🧠 Tecnologias Utilizadas

### **Linguagem & Ambiente**
- Python 3.11  
- Virtualenv  
- VSCode  

### **IA e Deep Learning**
- **PyTorch** (com suporte CUDA para RTX 3060)
- **Coqui TTS – XTTS v2** (modelo multilingual de clonagem de voz)
- Transformers (HuggingFace)
- NumPy  
- SciPy  

### **Interface**
- Gradio — interface interativa via navegador

### **Áudio & Utilitários**
- Soundfile  
- Pydub  
- Librosa  
- FFmpeg (dependência para manipulação de áudio)

---

## 🖥️ Funcionalidades Principais

✔ Gravação ou upload de áudio de referência  
✔ Extração do timbre do usuário  
✔ Geração de fala sintética utilizando XTTS-v2  
✔ Interface amigável e acessível pelo navegador  
✔ Salvamento automático dos áudios de entrada e saída  
✔ Parâmetros avançados: `temperature`, `speed`, `repetition_penalty`, presets de naturalidade  

---

## 📂 Estrutura de Diretórios

```plaintext
MinhaVoz/
│
├── app.py                 # Interface Gradio
├── tts_model.py           # Funções de IA e clonagem de voz
├── requirements.txt       # Dependências do projeto
│
├── recordings/            # Áudios enviados/gravações do usuário
│     └── ref_*.wav
│
├── outputs/               # Áudios gerados pela IA
│     └── minha_voz_*.wav
│
└── README.md              # Documentação do projeto
````

---

## ⚙️ Instalação — Passo a Passo

### **1. Clone o repositório**

```bash
git clone https://github.com/SEU_USUARIO/minha-voz.git
cd minha-voz
```

### **2. Crie o ambiente virtual**

```bash
python -m venv .venv
```

### **3. Ative o ambiente virtual**

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### **4. Instale as dependências**

```bash
pip install -r requirements.txt
```

### **5. Confirme se o PyTorch está usando sua GPU**

```python
python -c "import torch; print(torch.cuda.is_available())"
```

Se retornar `True`, tudo certo!

---

## ▶️ Como Executar a Aplicação

No ambiente virtual ativo, execute:

```bash
python app.py
```

O Gradio iniciará um servidor local:

```
Running on http://127.0.0.1:7860
```

Abra esse endereço no navegador.

---

## 🎚️ Presets de Naturalidade

O projeto inclui três presets ajustando temperatura, velocidade e entonação:

* **Natural**
* **Expressivo**
* **Rápido e Objetivo**

Eles podem ser selecionados diretamente na interface.

---

## 👥 Créditos

Projeto desenvolvido por:

* **Carlos Reis**
* **Leonardo Aguirre**
* **Mateus Ferrarini**
* **Professora: Aline**

Curso: **Fundamentos de Inteligência Artificial – G2**

---

## 📝 Licença

Uso acadêmico. Modificações e melhorias são permitidas.

---

## ⭐ Como contribuir

Sinta-se livre para abrir *issues* ou *pull requests* no GitHub.

```

---

# 🔥 Tudo pronto para subir direto no GitHub!

Se quiser, posso também:

✅ gerar badges (Python version, CUDA, Coqui TTS, etc.)  
✅ criar a licença escolhida (MIT, Apache, etc.)  
✅ gerar o `.gitignore` ideal para este projeto  
✅ gerar um banner gráfico para o topo do README  
✅ preparar um release “v1.0” para você subir

Só pedir!
```
