# Resonance Engine

**Therapeutic audio generated from math, not samples.**

A Python tool that layers binaural beats, golden ratio harmonics, heartbeat modulation, and pink noise into a single WAV file designed to feel alive.

---

## What It Does

Generates audio from four mathematical layers:

1. **Theta Foundation** — A 432Hz base tone paired with 436Hz creates a 4Hz binaural beat, targeting the theta brainwave range (deep meditation, creativity, hypnagogic states)
2. **Golden Spiral Stack** — Overtones at irrational Phi-ratio intervals produce organic complexity no human composer would write
3. **Biological Pulse** — Amplitude modulation at 1.2Hz (72 BPM) gives the audio a resting heartbeat rhythm
4. **Vascular Floor** — 0.3% pink noise (1/f) eliminates digital silence. The quiet parts aren't empty — they pulse with the same statistical pattern found in ocean tides, neural firing, and healthy hearts

The result is a WAV file that sounds synthetic but *feels* biological.

![Golden Spiral](images/golden_spiral.jpg)


*The Golden Ratio (Φ) — the irrational interval behind the harmonic stacking*



![Binaural Beat Waveform](images/binaural_waveform.jpg)


*Amplitude modulation envelope wrapping the carrier wave — this is what the code produces*

## Quick Start

```bash
pip install numpy scipy sympy

python src/resonance_engine.py
```

This generates `Consciousness_Vascular.wav` — 60 seconds of the default theta-state output.

## Presets

The engine includes three ready-made configurations:

```python
from resonance_engine import generate_default, generate_deep_sleep, generate_focus

generate_default()      # 60s theta (4Hz) — meditation / creativity
generate_deep_sleep()   # 5min delta (2Hz) — sleep induction
generate_focus()        # 2min alpha (10Hz) — concentration
```

## Custom Builds

```python
from resonance_engine import ResonanceEngine

engine = ResonanceEngine(sample_rate=44100, duration=180)  # 3 minutes

# Choose your binaural beat frequency
wave = engine.quantum_superposition(432, 438)  # 6Hz = deep theta

# Add harmonic richness (more layers = more texture)
wave = engine.golden_spiral_stack(wave, 432, layers=5)

# Set the heartbeat (heart_rate_hz, depth 0-1)
wave = engine.biological_pulse(wave, heart_rate_hz=1.0, depth=0.5)

# Render with custom noise floor
engine.materialize_wave(wave, noise_level=0.004, filename="My_Session.wav")
```

### Tunable Parameters

| Parameter | What it does | Range |
|-----------|-------------|-------|
| `freq_base` | Root frequency | 100-528Hz (432 recommended) |
| `freq_entanglement` | Second tone (difference = binaural beat Hz) | base + 1-40 |
| `layers` | Golden ratio harmonic depth | 1-6 |
| `heart_rate_hz` | Heartbeat pulse speed | 0.5-2.0 Hz |
| `depth` | How dramatic the pulse is | 0.0-1.0 |
| `noise_level` | Pink noise amplitude | 0.001-0.01 |
| `duration` | Output length in seconds | Any |

### Brainwave Frequency Guide

| Beat Frequency | State | Use |
|---------------|-------|-----|
| 1-4 Hz (Delta) | Deep sleep | Sleep induction, recovery |
| 4-8 Hz (Theta) | Meditation | Creativity, deep relaxation |
| 8-13 Hz (Alpha) | Calm focus | Study, light meditation |
| 13-30 Hz (Beta) | Alertness | Active thinking, energy |

## How It Works

The engine builds audio symbolically using SymPy, then collapses to numpy for rendering. This means the waveform is defined as pure mathematics before it ever becomes sound — no samples, no loops, no presets from a library.

The pink noise is generated via spectral filtering: white noise is transformed to frequency domain, scaled by `1/√f`, and transformed back. This produces structured randomness where lower frequencies carry more energy — the same pattern found in natural systems.

## Requirements

- Python 3.8+
- numpy
- scipy
- sympy

## Credits

Designed by **Samuel Jackson Grim** through multi-agent AI collaboration with Gemini, Copilot, Grok & Claude.

## License

MIT. Use it however you want. Make something that helps someone.
