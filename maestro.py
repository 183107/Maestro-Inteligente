import numpy as np

print("--- [STARK/M3GAN] INICIALIZANDO MAESTRO INTELIGENTE ---")

# 1. Parâmetros de Áudio Digital (Padrão de estúdio)
TAXA_AMOSTRAGEM = 44100  # 44.1 kHz
DURACAO = 1.0            # 1 segundo de simulação analítica
FREQUENCIA_ALVO = 440.0  # Frequência da nota Lá 4 (A4) do teclado

# 2. Gerando uma onda senoidal matemática (Simulando uma tecla pressionada)
t = np.linspace(0, DURACAO, int(TAXA_AMOSTRAGEM * DURACAO), endpoint=False)
onda_sonora = np.sin(2 * np.pi * FREQUENCIA_ALVO * t)

# 3. Processamento de Sinais: Aplicando a Transformada Rápida de Fourier (FFT)
frequencias = np.fft.fftfreq(len(onda_sonora), 1 / TAXA_AMOSTRAGEM)
valores_fft = np.abs(np.fft.fft(onda_sonora))

# 4. Cérebro Algorítmico: Encontrando o pico de energia mecânica
indice_maximo = np.argmax(valores_fft[:len(valores_fft)//2])
frequencia_detectada = abs(frequencias[indice_maximo])

print(f"Frequência gerada pelo simulador: {FREQUENCIA_ALVO} Hz")
print(f"Frequência calculada pela FFT: {frequencia_detectada:.1f} Hz")

if round(frequencia_detectada) == 440:
    print("🚀 SUCESSO: O cérebro do Maestro identificou com precisão a nota Lá 4 (A4)!")
else:
    print("❌ Falha no cálculo matemático do algoritmo.")
