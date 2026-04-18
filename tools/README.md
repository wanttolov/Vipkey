# Vipkey Tools

## benchmark_ime.ps1

End-to-end IME benchmark. Compares Vipkey vs UniKey (or any IME) by injecting keystrokes into Notepad and measuring latency.

**Requirements:** Windows PowerShell 5.1+ (built-in). No extra dependencies.

### Quick Start

```powershell
# 1. Switch to Vipkey, run benchmark
powershell -ExecutionPolicy Bypass -File .\benchmark_ime.ps1 -IME "Vipkey"

# 2. Switch to UniKey, run again
powershell -ExecutionPolicy Bypass -File .\benchmark_ime.ps1 -IME "UniKey"

# 3. Compare results
powershell -ExecutionPolicy Bypass -File .\benchmark_ime.ps1 -Compare
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-IME` | (prompt) | Name of the active IME |
| `-Rounds` | 5 | Number of rounds per test |
| `-DelayMs` | 80 | Delay between words (ms), simulates typing speed |
| `-Compare` | | Compare the 2 most recent result files |
| `-NoEnglish` | | Skip the English typing test |

### What it measures

- Opens Notepad automatically
- Types 20 Vietnamese words (Telex) x N rounds via `SendInput`
- Types 20 English words x N rounds
- Reports per-key latency (us), per-round total (ms), avg/min/max
- Saves results to `benchmark_<ime>_<timestamp>.json`

### Example output

```
============================================================
  Vietnamese Telex - Vipkey
============================================================
  Round 1:    45.23 ms  (  34.2 us/key, 132 keys)
  Round 2:    43.87 ms  (  33.2 us/key, 132 keys)
  --------------------------------------------------------
  Average:    44.55 ms  (  33.7 us/key)
  Best:       43.87 ms
  Worst:      45.23 ms

=================================================================
  IME COMPARISON
=================================================================
                          Vipkey         UniKey
                      ────────────    ────────────
Vietnamese (avg/key)       33.7 us         35.2 us
English (avg/key)          28.1 us         29.5 us

  Vietnamese: Vipkey is 4.3% faster
```

## build_lite.ps1 / build_app.ps1

Build & run scripts for the two Vipkey variants.

| Script | What it builds | Output |
|--------|---------------|--------|
| `build_lite.ps1` | Classic Win32 UI (no Sciter) | `build-lite\Debug\VipkeyClassic.exe` |
| `build_app.ps1` | Full Sciter UI | `build\Debug\Vipkey.exe` |

```powershell
# Build + run Classic (Lite)
.\tools\build_lite.ps1 -Run

# Build + run Sciter (App)
.\tools\build_app.ps1 -Run

# Clean rebuild
.\tools\build_lite.ps1 -Clean -Run

# Release build
.\tools\build_lite.ps1 -Release

# Debug both side by side
.\tools\build_app.ps1 -Run; .\tools\build_lite.ps1 -Run
```

Auto-kills existing instance before launching. Auto-configures CMake if no cache exists.

## release_tag.sh

Create a git tag for release.

## update_sciter.sh

Update Sciter SDK to latest version from GitLab. Copies includes + binaries to `extern/sciter/`.

```bash
bash tools/update_sciter.sh
```
