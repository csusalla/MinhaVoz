# app.py
import gradio as gr
import os
from tts_model import synthesize_speech, LANGUAGE_MAP

# -----------------------------------------------------------
# PRESETS DE VOZ
# -----------------------------------------------------------

PRESETS = {
    "Natural": {
        "temperature": 0.7,
        "speed": 1.0,
        "repetition_penalty": 2.0,
    },
    "WhatsApp Real": {
        "temperature": 0.6,
        "speed": 1.1,   # levemente mais rápido
        "repetition_penalty": 1.8,
    },
    "Narrador": {
        "temperature": 0.75,
        "speed": 0.92,  # mais pausado
        "repetition_penalty": 2.2,
    },
    "Emocionado": {
        "temperature": 0.85,
        "speed": 1.0,
        "repetition_penalty": 2.0,
    },
    "Rápido Profissional": {
        "temperature": 0.65,
        "speed": 1.15,
        "repetition_penalty": 2.5,
    },
    "Clareza Máxima": {
        "temperature": 0.55,
        "speed": 1.05,
        "repetition_penalty": 3.0,
    }
}


# -----------------------------------------------------------
# FUNÇÃO PARA A INTERFACE
# -----------------------------------------------------------

def generate_voice(reference_audio, text, language_name, preset_name):
    if reference_audio is None:
        raise gr.Error("Por favor, grave ou envie um áudio de referência primeiro.")

    language = LANGUAGE_MAP.get(language_name)

    if language is None:
        raise gr.Error("Idioma não reconhecido.")

    # Caminho onde o áudio será salvo
    output_path = "outputs/minha_voz.wav"

    # Preset escolhido
    preset = PRESETS[preset_name]

    try:
        final_path = synthesize_speech(
            text=text,
            language=language,
            reference_audio_path=reference_audio,
            output_path=output_path,
            temperature=preset["temperature"],
            speed=preset["speed"],
            repetition_penalty=preset["repetition_penalty"],
        )

        return final_path

    except Exception as e:
        raise gr.Error(f"Erro ao gerar o áudio com a IA: {str(e)}")


# -----------------------------------------------------------
# INTERFACE GRADIO
# -----------------------------------------------------------

with gr.Blocks(title="Minha Voz - Gerador de Voz Personalizada") as demo:
    gr.Markdown("## 🎤 Minha Voz — Crie uma voz sintética a partir da sua própria voz")

    with gr.Row():
        reference_audio = gr.Audio(
            label="Áudio de referência (sua voz)",
            type="filepath",
            waveform_options={"show_controls": True},
            sources=["microphone", "upload"],
        )

        output_audio = gr.Audio(
            label="Resultado (voz gerada)",
            type="filepath"
        )

    text = gr.Textbox(
        label="Texto que será falado",
        placeholder="Digite aqui a frase...",
        lines=3
    )

    language_name = gr.Dropdown(
        list(LANGUAGE_MAP.keys()),
        value="Português (Brasil)",
        label="Idioma da Fala"
    )

    preset_name = gr.Dropdown(
        list(PRESETS.keys()),
        value="Natural",
        label="Estilo de Voz (preset)"
    )

    generate_button = gr.Button("Gerar Voz", variant="primary")

    generate_button.click(
        fn=generate_voice,
        inputs=[reference_audio, text, language_name, preset_name],
        outputs=output_audio
    )

demo.launch(share=True)
