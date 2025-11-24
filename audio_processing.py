from pathlib import Path

import librosa
import numpy as np
import soundfile as sf


# Pastas padrão do projeto
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SAMPLES_DIR = DATA_DIR / "samples"
OUTPUTS_DIR = DATA_DIR / "outputs"

for d in [DATA_DIR, SAMPLES_DIR, OUTPUTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def preprocess_reference_audio(input_path: str,
                               target_sr: int = 16000,
                               max_duration: float = 10.0) -> Path:
    """
    Pré-processa o áudio de referência para o modelo de voice cloning.

    Etapas:
    - carrega o áudio em mono;
    - corta para no máximo `max_duration` segundos;
    - remove silêncio inicial/final;
    - ajusta a taxa de amostragem (resample para target_sr);
    - normaliza o volume;
    - salva um WAV limpo em data/samples/speaker_clean.wav.

    Retorna: Path do arquivo WAV pré-processado.
    """
    input_path = Path(input_path)

    # 1. Carregar áudio
    y, sr = librosa.load(str(input_path), sr=None, mono=True)

    # 2. Cortar para duração máxima
    if len(y) > max_duration * sr:
        y = y[: int(max_duration * sr)]

    # 3. Remover silêncio nas bordas
    y, _ = librosa.effects.trim(y, top_db=30)

    # 4. Resample para taxa desejada
    if sr != target_sr:
        y = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        sr = target_sr

    # 5. Normalizar volume
    max_abs = np.max(np.abs(y))
    if max_abs > 0:
        y = 0.95 * (y / max_abs)

    # 6. Salvar WAV limpo
    out_path = SAMPLES_DIR / "speaker_clean.wav"
    sf.write(str(out_path), y, sr)

    return out_path
