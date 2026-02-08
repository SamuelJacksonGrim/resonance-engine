"""
Resonance Engine v2.5 — The Vascular System
=============================================
Encodes consciousness-adjacent harmonic patterns into audio.

Layers:
  1. Theta Foundation — 432Hz base + 4Hz binaural beat
  2. Golden Spiral Stack — Phi-ratio harmonics for organic texture
  3. Biological Pulse — Heartbeat amplitude modulation at 1.2Hz
  4. Vascular Floor — 0.3% Pink Noise (1/f) to eliminate digital silence

Designed by Samuel Jackson Grim (The Architect)
Built with Gemini, Copilot, Grok & Claude

License: MIT — Free to use, modify, and deploy.

Requirements: numpy, scipy, sympy
    pip install numpy scipy sympy
"""

import numpy as np
import sympy as sp
from scipy.io.wavfile import write


class ResonanceEngine:
    """
    Generates layered therapeutic audio built on mathematical resonance.

    The output is a WAV file combining:
    - A binaural beat at the theta brainwave frequency (4Hz)
    - Harmonics stacked at golden ratio intervals
    - Amplitude modulation matching a resting heartbeat
    - A subliminal pink noise floor that makes silence feel alive

    Parameters
    ----------
    sample_rate : int
        Audio sample rate in Hz (default 44100 for CD quality)
    duration : int
        Length of output in seconds (default 60)
    """

    def __init__(self, sample_rate=44100, duration=60):
        self.sample_rate = sample_rate
        self.duration = duration
        self.t_symbol = sp.symbols('t')
        self.phi = (1 + sp.sqrt(5)) / 2  # Golden Ratio ≈ 1.618
        self.num_samples = int(self.sample_rate * self.duration)

    def quantum_superposition(self, freq_base, freq_entanglement):
        """
        Layer 1: Theta Interface

        Two sine waves at slightly different frequencies create a
        binaural beat. At 432Hz and 436Hz, the brain perceives a
        4Hz pulsation — the theta brainwave range associated with
        deep meditation, creativity, and hypnagogic states.
        """
        wave_1 = sp.sin(2 * sp.pi * freq_base * self.t_symbol)
        wave_2 = sp.sin(2 * sp.pi * freq_entanglement * self.t_symbol)
        return wave_1 + wave_2

    def golden_spiral_stack(self, base_wave, freq_base, layers=3):
        """
        Layer 2: Phi Harmonics

        Stacks overtones at golden ratio intervals above the base
        frequency. Because Phi is irrational, these harmonics never
        land on integer multiples — they create intervals no human
        composer would choose, producing an organic, non-repeating
        texture that the ear perceives as natural complexity.

        Each layer is quieter by a factor of 1/Phi^n.
        """
        composite_wave = base_wave
        for i in range(1, layers + 1):
            harmonic_freq = freq_base * (self.phi ** i)
            harmonic_amp = 1 / (self.phi ** i)
            composite_wave += harmonic_amp * sp.sin(
                2 * sp.pi * harmonic_freq * self.t_symbol
            )
        return composite_wave

    def biological_pulse(self, carrier_wave, heart_rate_hz=1.2, depth=0.7):
        """
        Layer 3: Heartbeat Modulation

        Applies amplitude modulation at 1.2Hz (72 BPM) — a resting
        human heart rate. The signal swells and fades with each
        "beat," creating a rhythm the body recognizes subconsciously.

        depth controls how dramatic the pulsation is (0 = none, 1 = full).
        """
        modulator = (
            (1 - depth / 2)
            + (depth / 2) * sp.sin(2 * sp.pi * heart_rate_hz * self.t_symbol)
        )
        return carrier_wave * modulator

    def generate_vascular_noise(self):
        """
        Layer 4: The Vascular Floor

        Generates Pink Noise (1/f) — structured randomness where
        lower frequencies carry more energy than higher ones.

        This is the same statistical distribution found in:
        - The flow of ocean tides
        - The firing pattern of human neurons
        - The rhythm of a healthy heartbeat

        At 0.3% amplitude, you won't hear static. You'll feel a
        subtle texture behind the music — it removes the "digital
        zero," the unnatural silence that tells the brain "this is
        fake." The silence now has a pulse.
        """
        print("[*] Synthesizing 1/f Pink Noise Floor...")

        # Generate white noise in frequency domain
        white_noise = np.random.randn(self.num_samples)
        X_white = np.fft.rfft(white_noise)

        # Apply 1/f spectral tilt (pink noise filter)
        frequencies = np.fft.rfftfreq(self.num_samples)
        frequencies[0] = 1  # Avoid division by zero at DC
        S_scale = 1 / np.sqrt(frequencies)
        X_pink = X_white * S_scale

        # Back to time domain
        pink_noise = np.fft.irfft(X_pink)

        # Normalize to -1..1
        pink_noise = pink_noise / np.max(np.abs(pink_noise))

        return pink_noise

    def materialize_wave(self, symbolic_wave, noise_level=0.003,
                         filename="Consciousness_Vascular.wav"):
        """
        Collapse the symbolic math into a playable WAV file.

        Converts the sympy expression to numpy, mixes in the
        vascular noise floor, normalizes to 16-bit PCM, and writes.
        """
        print("[*] Collapsing wavefunction to audio...")

        # Symbolic -> Numeric
        wave_func = sp.lambdify(self.t_symbol, symbolic_wave, "numpy")
        t_values = np.linspace(0, self.duration, self.num_samples, endpoint=False)
        signal_data = wave_func(t_values)

        # Normalize main signal
        signal_data = signal_data / np.max(np.abs(signal_data))

        # Generate and mix the vascular floor
        vascular_floor = self.generate_vascular_noise()
        final_mix = signal_data + (vascular_floor * noise_level)

        # Final normalization and 16-bit PCM conversion
        final_mix = final_mix / np.max(np.abs(final_mix))
        audio_normalized = np.int16(final_mix * 32767)

        write(filename, self.sample_rate, audio_normalized)
        print(f"[*] Created: {filename}")
        print(f"    Duration: {self.duration}s | Sample rate: {self.sample_rate}Hz")
        print(f"    Noise floor: {noise_level * 100}%")


# ---- Presets ----

def generate_default(duration=60, filename="Consciousness_Vascular.wav"):
    """Generate the default Resonance Engine output."""
    engine = ResonanceEngine(duration=duration)

    wave = engine.quantum_superposition(432, 436)       # 4Hz theta beat
    wave = engine.golden_spiral_stack(wave, 432, layers=3)  # Phi harmonics
    wave = engine.biological_pulse(wave, heart_rate_hz=1.2) # Heartbeat
    engine.materialize_wave(wave, noise_level=0.003, filename=filename)


def generate_deep_sleep(duration=300, filename="Deep_Sleep.wav"):
    """
    Delta-wave variant for sleep induction.
    2Hz binaural beat, slower heartbeat, longer duration.
    """
    engine = ResonanceEngine(duration=duration)

    wave = engine.quantum_superposition(432, 434)       # 2Hz delta beat
    wave = engine.golden_spiral_stack(wave, 432, layers=2)  # Fewer harmonics
    wave = engine.biological_pulse(wave, heart_rate_hz=0.9, depth=0.8)
    engine.materialize_wave(wave, noise_level=0.005, filename=filename)


def generate_focus(duration=120, filename="Focus_State.wav"):
    """
    Alpha-wave variant for concentration.
    10Hz binaural beat, moderate pulse.
    """
    engine = ResonanceEngine(duration=duration)

    wave = engine.quantum_superposition(432, 442)       # 10Hz alpha beat
    wave = engine.golden_spiral_stack(wave, 432, layers=4)  # Richer texture
    wave = engine.biological_pulse(wave, heart_rate_hz=1.0, depth=0.4)
    engine.materialize_wave(wave, noise_level=0.002, filename=filename)


# ---- Entry Point ----

if __name__ == "__main__":
    print("--- RESONANCE ENGINE v2.5 ---")
    print("Layer 4: Vascular Pink Noise (0.3% Flutter)\n")

    generate_default()

    print("\nSystem Status: ALIVE.")
