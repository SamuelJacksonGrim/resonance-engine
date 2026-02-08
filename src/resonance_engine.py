"""
Resonance Engine v3.2 — The Hemispheric Bridge (Final Ship Cut)
================================================================
Encodes consciousness-adjacent harmonic patterns into TRUE STEREO audio.

Layers:
  1. True Binaural Separation — Base Freq (Left) / Entangled Freq (Right)
  2. Orbital Phi Harmonics — Golden Spiral overtones rotate around the head
  3. Fibonacci HRV — Heartbeat drifts naturally using FM synthesis + soft-knee
  4. Vascular Floor — Decorrelated pink/brown noise (β tunable per preset)
  5. Breath Envelope — Cosine fade-in/fade-out for clean edges

Designed by Samuel Jackson Grim (The Architect)
Refined by Gemini, Copilot, Grok, Claude
Final polish: Grok v3.2 (phase rand + HRV knee + β-palette)

License: MIT — Free to use, modify, and deploy.

Requirements: numpy, scipy, sympy
    pip install numpy scipy sympy
"""

import numpy as np
import sympy as sp
from scipy.io.wavfile import write
import random


class ResonanceEngine:
    """
    Generates layered therapeutic audio built on mathematical resonance.
    All output is TRUE STEREO — headphones required for binaural effect.
    """

    def __init__(self, sample_rate=44100, duration=60):
        self.sample_rate = sample_rate
        self.duration = duration
        self.t_symbol = sp.symbols('t')
        self.phi = (1 + sp.sqrt(5)) / 2  # Golden Ratio ≈ 1.618
        self.num_samples = int(self.sample_rate * self.duration)

        # Global phase randomization — different every run
        self.global_phase_offset = random.uniform(0, 2 * np.pi)

    def quantum_superposition_stereo(self, freq_base, freq_entanglement):
        """
        Layer 1: True Binaural Interface (Stereo Split)

        Sends base frequency to Left ear, entangled frequency to Right ear.
        The 'beat' is created inside the listener's brainstem as the
        corpus callosum reconciles the frequency difference.

        This only works with headphones.
        """
        t = self.t_symbol + self.global_phase_offset / (2 * np.pi * freq_base)
        left_wave = sp.sin(2 * sp.pi * freq_base * t)
        right_wave = sp.sin(2 * sp.pi * freq_entanglement * t)
        return left_wave, right_wave

    def golden_spiral_stack(self, base_waves, freq_base, layers=3):
        """
        Layer 2: Orbital Phi Harmonics

        Stacks overtones at golden ratio intervals. Each harmonic layer
        slowly pans between ears at a different Phi-divided speed,
        creating a spatial halo that never repeats predictably.
        """
        left_composite, right_composite = base_waves

        for i in range(1, layers + 1):
            harmonic_freq = freq_base * (self.phi ** i)
            harmonic_amp = 1 / (self.phi ** i)

            t_shifted = self.t_symbol + self.global_phase_offset / (2 * np.pi * harmonic_freq)
            tone = sp.sin(2 * sp.pi * harmonic_freq * t_shifted)

            # Orbital panning — different layers rotate at different speeds
            pan_speed = 0.1 / i
            pan_phase = self.global_phase_offset * (i + 1)  # stagger layers
            pan_left = sp.cos(2 * sp.pi * pan_speed * self.t_symbol + pan_phase)
            pan_right = sp.sin(2 * sp.pi * pan_speed * self.t_symbol + pan_phase)

            left_composite += (harmonic_amp * tone * pan_left)
            right_composite += (harmonic_amp * tone * pan_right)

        return left_composite, right_composite

    def generate_fibonacci_hrv(self, base_rate=1.2, drift_range=0.4,
                               breath_cycle=0.1, min_knee=0.40):
        """
        Layer 3: Fibonacci HRV (Heart Rate Variability)

        A healthy heart doesn't beat like a metronome — it varies.
        This generates the pulse envelope numerically using FM synthesis
        so the beat frequency itself drifts over time.

        The soft-knee (min_knee) prevents the envelope from ever fully
        muting — keeps the pulse feeling alive even in deep drift.

        Parameters
        ----------
        base_rate : float
            Center heartbeat frequency in Hz (1.2 = 72 BPM)
        drift_range : float
            How much the rate varies (0.4 = swings ±0.4Hz)
        breath_cycle : float
            How fast the drift oscillates in Hz (0.1 = 10 second cycle)
        min_knee : float
            Minimum envelope value to prevent dead air (0.0-1.0)
        """
        t = np.linspace(0, self.duration, self.num_samples, endpoint=False)
        instant_freq = base_rate + drift_range * np.sin(2 * np.pi * breath_cycle * t)
        phase = 2 * np.pi * np.cumsum(instant_freq) / self.sample_rate + self.global_phase_offset
        depth = 0.6
        envelope = (1 - depth / 2) + (depth / 2) * np.sin(phase)
        envelope = np.clip(envelope, min_knee, 1.0)
        return envelope

    def generate_vascular_noise(self, beta=1.0, seed=None):
        """
        Layer 4: Tunable Vascular Noise Floor

        Generates 1/f^β noise. When called with different seeds,
        produces decorrelated noise for true stereo separation.

        β controls the noise color:
          β < 1.0 — bluer (crisper, more high-frequency energy)
          β = 1.0 — classic pink (equal energy per octave)
          β > 1.0 — redder (warmer, more low-frequency rumble)
        """
        rng = np.random.default_rng(seed)
        white = rng.standard_normal(self.num_samples)
        X_white = np.fft.rfft(white)
        freqs = np.fft.rfftfreq(self.num_samples)
        freqs[0] = 1  # guard against division by zero
        shaping = 1 / (freqs ** (beta / 2))
        X_colored = X_white * shaping
        colored = np.fft.irfft(X_colored)
        return colored / np.max(np.abs(colored))

    def generate_breath_envelope(self, fade_seconds=4.0):
        """
        Layer 5: Fade In / Fade Out

        Cosine ramp at both ends prevents speaker pops and creates
        a gentle emergence from and return to silence. Essential for
        audio that people listen to with their eyes closed.
        """
        fade_samples = int(fade_seconds * self.sample_rate)
        envelope = np.ones(self.num_samples)
        if fade_samples > 0 and fade_samples * 2 < self.num_samples:
            fade_in = 0.5 * (1 - np.cos(np.pi * np.arange(fade_samples) / fade_samples))
            fade_out = fade_in[::-1]
            envelope[:fade_samples] = fade_in
            envelope[-fade_samples:] = fade_out
        return envelope

    def materialize_stereo(self, stereo_waves, noise_beta=1.0,
                           noise_level=0.003, fade_seconds=4.0,
                           hrv_base_rate=1.2, hrv_drift=0.4, hrv_breath=0.1,
                           filename="Resonance_v3.2_Stereo.wav"):
        """
        Collapse symbolic math into a playable stereo WAV file.

        Applies all numeric layers (HRV, noise, fade) during
        materialization since they require numpy, not sympy.
        """
        print("[*] Collapsing wavefunction to STEREO (v3.2)...")
        left_sym, right_sym = stereo_waves

        func_L = sp.lambdify(self.t_symbol, left_sym, "numpy")
        func_R = sp.lambdify(self.t_symbol, right_sym, "numpy")

        t_val = np.linspace(0, self.duration, self.num_samples, endpoint=False)

        print("    -> Rendering hemispheres...")
        audio_L = func_L(t_val).astype(np.float64)
        audio_R = func_R(t_val).astype(np.float64)

        # Normalize BOTH channels together to preserve spatial image
        print("    -> Normalizing stereo field...")
        shared_max = max(np.max(np.abs(audio_L)), np.max(np.abs(audio_R)))
        if shared_max > 0:
            audio_L /= shared_max
            audio_R /= shared_max

        # Apply Fibonacci HRV pulse (numeric, not symbolic)
        print("    -> Applying Fibonacci HRV (with knee)...")
        hrv_envelope = self.generate_fibonacci_hrv(
            base_rate=hrv_base_rate, drift_range=hrv_drift,
            breath_cycle=hrv_breath, min_knee=0.40
        )
        audio_L *= hrv_envelope
        audio_R *= hrv_envelope

        # Decorrelated noise — independent per channel
        print(f"    -> Synthesizing vascular noise (\u03b2={noise_beta})...")
        noise_L = self.generate_vascular_noise(beta=noise_beta, seed=42)
        noise_R = self.generate_vascular_noise(beta=noise_beta, seed=137)
        audio_L += noise_L * noise_level
        audio_R += noise_R * noise_level

        # Breath envelope (fade in/out)
        print("    -> Applying breath envelope...")
        breath = self.generate_breath_envelope(fade_seconds=fade_seconds)
        audio_L *= breath
        audio_R *= breath

        # Final normalization and 16-bit PCM conversion
        final_max = max(np.max(np.abs(audio_L)), np.max(np.abs(audio_R)))
        if final_max > 0:
            audio_L = np.int16((audio_L / final_max) * 32767)
            audio_R = np.int16((audio_R / final_max) * 32767)

        # Interleave for stereo WAV
        stereo_data = np.column_stack((audio_L, audio_R))
        write(filename, self.sample_rate, stereo_data)

        print(f"[*] Created: {filename} (v3.2)")
        print(f"    Duration: {self.duration}s | \u03b2={noise_beta} | HRV knee @ 0.40")
        print(f"    Phase randomized | Channels: True Stereo")


# ---- Presets (tuned β per state) ----

def generate_true_theta(duration=60, filename="Resonance_Theta_Stereo.wav"):
    """
    Default: 4Hz theta binaural beat for meditation and creativity.
    Headphones required.
    """
    engine = ResonanceEngine(duration=duration)
    waves = engine.quantum_superposition_stereo(432, 436)
    waves = engine.golden_spiral_stack(waves, 432, layers=3)
    engine.materialize_stereo(
        waves,
        noise_beta=1.1,
        filename=filename
    )


def generate_deep_sleep(duration=300, filename="Deep_Sleep_Stereo.wav"):
    """
    Delta-wave variant for sleep induction.
    2Hz binaural beat, slower heartbeat, deeper pulse, longer duration.
    Headphones required.
    """
    engine = ResonanceEngine(duration=duration)
    waves = engine.quantum_superposition_stereo(432, 434)
    waves = engine.golden_spiral_stack(waves, 432, layers=2)
    engine.materialize_stereo(
        waves,
        noise_beta=1.3,
        hrv_base_rate=0.9,
        hrv_drift=0.2,
        hrv_breath=0.067,
        noise_level=0.005,
        fade_seconds=8.0,
        filename=filename
    )


def generate_focus(duration=120, filename="Focus_State_Stereo.wav"):
    """
    Alpha-wave variant for concentration.
    10Hz binaural beat, moderate pulse, richer harmonics.
    Headphones required.
    """
    engine = ResonanceEngine(duration=duration)
    waves = engine.quantum_superposition_stereo(432, 442)
    waves = engine.golden_spiral_stack(waves, 432, layers=4)
    engine.materialize_stereo(
        waves,
        noise_beta=0.95,
        hrv_base_rate=1.1,
        hrv_drift=0.3,
        hrv_breath=0.1,
        noise_level=0.002,
        fade_seconds=3.0,
        filename=filename
    )


def generate_gamma_flow(duration=90, filename="Gamma_Flow_Stereo.wav"):
    """
    Gamma-wave variant for peak performance and insight.
    40Hz binaural beat — associated with heightened awareness
    and cross-cortical binding.
    Headphones required.
    """
    engine = ResonanceEngine(duration=duration)
    waves = engine.quantum_superposition_stereo(432, 472)
    waves = engine.golden_spiral_stack(waves, 432, layers=5)
    engine.materialize_stereo(
        waves,
        noise_beta=0.85,
        hrv_base_rate=1.3,
        hrv_drift=0.5,
        hrv_breath=0.133,
        noise_level=0.001,
        fade_seconds=3.0,
        filename=filename
    )


# ---- Entry Point ----

if __name__ == "__main__":
    print("=== RESONANCE ENGINE v3.2 \u2014 FINAL SHIP CUT ===")
    print("Phase-randomized | HRV soft-knee | Tunable noise \u03b2 | Ready for GitHub\n")

    print("--- Generating Theta (Meditation) ---")
    generate_true_theta()

    print("\n--- Generating Deep Sleep (Delta) ---")
    generate_deep_sleep()

    print("\n--- Generating Focus (Alpha) ---")
    generate_focus()

    print("\n--- Generating Gamma Flow (Peak Performance) ---")
    generate_gamma_flow()

    print("\n=== ALL PRESETS GENERATED ===")
    print("System Status: ALIVE. Ship it, Architect.")
                                 
