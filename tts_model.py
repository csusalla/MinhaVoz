# tts_model.py
import os
import torch
from datetime import datetime
from shutil import copy2
from typing import Dict

from TTS.api import TTS

# -----------------------------------------------------------
# CONFIGURAÇÕES DO MODELO
# -----------------------------------------------------------

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"

# Detecta automaticamente GPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[TTS] Dispositivo selecionado: {DEVICE}")
print(f"[TTS] Carregando modelo: {MODEL_NAME}")

# Inicializa o modelo
tts = TTS(MODEL_NAME).to(DEVICE)

# -----------------------------------------------------------
# MAPEAMENTO DE IDIOMAS
# -----------------------------------------------------------

LANGUAGE_MAP: Dict[str, str] = {
    "Português (Brasil)": "pt",
    "Inglês": "en",
    "Francês": "fr",
}

# -----------------------------------------------------------
# GARANTIR PASTAS
# -----------------------------------------------------------

def _ensure_dirs() -> None:
    os.makedirs("recordings", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

# -----------------------------------------------------------
# SALVA CÓPIA DO ÁUDIO DE REFERÊNCIA
# -----------------------------------------------------------

def save_reference_copy(original_path: str) -> str:
    _ensure_dirs()
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = os.path.splitext(original_path)[1] or ".wav"
        dest_path = os.path.join("recordings", f"ref_{timestamp}{ext}")
        copy2(original_path, dest_path)
        print(f"[TTS] Áudio de referência salvo em: {dest_path}")
        return dest_path
    except Exception as e:
        print(f"[TTS] Aviso: não foi possível salvar cópia do áudio de referência: {e}")
        return original_path

# -----------------------------------------------------------
# FUNÇÃO PRINCIPAL DE GERAÇÃO — COM PARÂMETROS AVANÇADOS
# -----------------------------------------------------------

def synthesize_speech(
    text: str,
    language: str,
    reference_audio_path: str,
    output_path: str,
    # ---- PARÂMETROS AVANÇADOS PARA AJUSTAR NATURALIDADE ----
    temperature: float = 0.7,        # 0.4–1.0 (0.7 recomendado)
    speed: float = 1.0,              # 0.8–1.2
    repetition_penalty: float = 2.0, # 1.0–3.0
):
    """
    Gera fala com XTTS-v2 usando áudio de referência.

    PARÂMETROS:
    - temperature: controla naturalidade/emotividade
    - speed: controla velocidade da fala
    - repetition_penalty: evita repetições indesejadas
    """

    _ensure_dirs()

    # Salvar cópia do áudio de referência
    saved_ref_path = save_reference_copy(reference_audio_path)

    # Nome único do arquivo gerado
    base_dir = os.path.dirname(output_path) or "outputs"
    os.makedirs(base_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = os.path.splitext(output_path)[1] or ".wav"
    final_output_path = os.path.join(base_dir, f"minha_voz_{timestamp}{ext}")

    print(f"[TTS] Gerando áudio em: {final_output_path}")
    print(f"[TTS] Idioma: {language} | Ref: {saved_ref_path}")

    # -------------- CHAMADA DO MODELO COM AJUSTES --------------
    
    print(f"[TTS] Usando parâmetros: temperature={temperature}, speed={speed}, repetition_penalty={repetition_penalty},")
    tts.tts_to_file(
        text=text,
        file_path=final_output_path,
        speaker_wav=saved_ref_path,
        language=language,
        # Parâmetros que ajustam naturalidade:
        temperature=temperature,
        speed=speed,
        repetition_penalty=repetition_penalty,
    )

    return final_output_path
