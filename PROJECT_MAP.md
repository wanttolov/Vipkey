# NexusKey — Project Map

> Vietnamese IME for Windows. Hybrid TSF + Hook, C++20, Sciter.JS UI.

## Build Targets

| Target | Type | Links | Description |
|---|---|---|---|
| `NextKeyEngine` | Static lib | — | Pure C++ engines, no platform deps |
| `NextKeyCore` | Static lib | NextKeyEngine | Platform layer: SharedState, Config |
| `NextKeyTSF` | Shared lib (DLL) | NextKeyCore | TSF Text Input Processor |
| `NextKeyApp` | Executable | NextKeyCore | Main GUI app (Sciter UI + tray) |
| `NextKeyLite` | Executable | NextKeyCore | Classic Win32 native UI (no Sciter). Build: `-DNEXUSKEY_LITE_MODE=ON` |
| `NextKeyTests` | Executable | NextKeyCore, GTest | Google Test suite |

---

## Directory Map

```
NexusKey/
├── src/
│   ├── core/                          # ← NextKeyEngine + NextKeyCore
│   │   ├── engine/                    # Pure C++ input engines
│   │   │   ├── IInputEngine.h         # Interface: ProcessKey, GetResult, Reset
│   │   │   ├── TelexEngine.cpp/h      # Telex typing method (34K cpp)
│   │   │   ├── VniEngine.cpp/h        # VNI typing method (18K cpp)
│   │   │   ├── SpellChecker.cpp/h     # Vietnamese spell checking (26K cpp)
│   │   │   ├── CodeTableConverter.cpp/h  # Charset conversion TCVN3/VNI/Unicode (30K cpp)
│   │   │   ├── EngineFactory.cpp/h    # Creates engine by TypingMethod enum
│   │   │   ├── EngineHelpers.h        # Shared helper utilities
│   │   │   └── VietnameseTables.h     # Static data: vowels, consonants, tones
│   │   ├── config/                    # Configuration management
│   │   │   ├── TypingConfig.h         # Config struct: method, spellCheck, macros etc.
│   │   │   ├── ConfigManager.cpp/h    # TOML load/save (Win32-only, 24K cpp)
│   │   │   ├── ConfigEvent.cpp/h      # Named-event sync (Win32-only)
│   │   │   └── SettingMetadata.h      # Setting definitions: keys, types, defaults, UI labels
│   │   ├── ipc/                       # EXE ↔ DLL communication
│   │   │   ├── SharedState.h          # Memory-mapped struct: flags, config snapshot
│   │   │   ├── SharedConstants.h      # Shared memory names, sizes
│   │   │   └── SharedStateManager.cpp/h  # CreateFileMapping/MapViewOfFile (Win32)
│   │   ├── SmartSwitchManager.cpp/h   # Auto V/E switch by context
│   │   ├── SmartSwitchState.h         # State tracking for smart switch
│   │   ├── Strings.cpp/h             # Localized string dictionary (S() lookup)
│   │   ├── WinStrings.h              # Wstring ↔ UTF8 conversion (Win32-only)
│   │   ├── Debug.h                    # Debug logging macros
│   │   ├── SystemConfig.h            # System-level constants
│   │   ├── UIConfig.h                # UI-related constants
│   │   └── Version.h                 # Version string
│   │
│   ├── tsf/                           # ← NextKeyTSF (DLL)
│   │   ├── TextService.cpp/h          # ITfTextInputProcessorEx — TSF entry point
│   │   ├── KeyEventSink.cpp/h         # ITfKeyEventSink — keystroke handling
│   │   ├── EngineController.cpp/h     # Owns IInputEngine, orchestrates typing (17K cpp)
│   │   ├── CompositionManager.cpp/h   # ITfComposition management
│   │   ├── LanguageBarButton.cpp/h    # V/E toggle on language bar (11K cpp)
│   │   ├── EditSession.h             # ITfEditSession base wrapper
│   │   ├── CompositionEditSession.h   # Edit session for composition text
│   │   ├── InputScopeChecker.h        # Detect password/URL fields
│   │   ├── DisplayAttribute.h         # Underline style for composition
│   │   ├── Register.cpp              # DLL (un)registration in registry
│   │   ├── dllmain.cpp               # DLL entry point
│   │   ├── Globals.cpp/h             # DLL-wide globals (CLSID, refcount)
│   │   ├── ComUtils.h               # COM helper macros
│   │   ├── Define.h                  # TSF-specific constants
│   │   └── stdafx.h                  # Precompiled header
│   │
│   └── app/                           # ← NextKeyApp (EXE)
│       ├── main.cpp                   # WinMain, message loop, init (23K)
│       ├── dialogs/                   # Sciter-based dialog windows
│       │   ├── SettingsDialog.cpp/h   # Main settings (45K cpp — largest file)
│       │   ├── SciterSubDialog.cpp/h  # Base class for subprocess dialogs
│       │   ├── SubDialogConfig.h      # Config struct for subdialogs
│       │   ├── ExcludedAppsDialog.cpp/h  # App exclusion list
│       │   ├── TsfAppsDialog.cpp/h    # TSF-enabled apps list
│       │   ├── MacroTableDialog.cpp/h # Macro editor
│       │   ├── ConvertToolDialog.cpp/h  # Charset converter UI (18K cpp)
│       │   └── AboutDialog.cpp/h      # About box
│       ├── system/                    # System-level services
│       │   ├── HookEngine.cpp/h       # Keyboard hook fallback (63K cpp — largest!)
│       │   ├── TrayIcon.cpp/h         # System tray icon + menu (18K cpp)
│       │   ├── QuickConvert.cpp/h     # Quick consonant shortcuts (15K cpp)
│       │   ├── FloatingIcon.cpp/h     # Floating V/E indicator overlay
│       │   ├── DarkModeHelper.cpp/h   # Win32 dark mode detection + DWM attributes
│       │   ├── HotkeyManager.cpp/h    # Global hotkey registration
│       │   ├── UpdateChecker.cpp/h    # GitHub release checker
│       │   ├── UpdateInstaller.cpp/h  # Auto-update installer
│       │   ├── UpdateSecurity.cpp/h   # Update signature verification
│       │   ├── TsfRegistration.cpp/h  # Register/unregister TSF DLL
│       │   ├── ToastPopup.cpp/h       # Toast notification popup
│       │   ├── SubprocessRunners.cpp/h  # Launch subdialogs as child processes
│       │   ├── SubprocessHelper.h     # Subprocess utilities
│       │   └── StartupHelper.h        # Windows startup registration
│       ├── sciter/                    # Sciter integration layer
│       │   ├── SciterHelper.cpp/h     # Init Sciter, load HTML, callbacks
│       │   ├── SciterArchive.cpp/h    # Embedded resource archive
│       │   └── ScaleHelper.h          # DPI scaling helpers
│       ├── classic/                    # ← NextKeyLite (Classic Win32 UI, no Sciter)
│       │   ├── ClassicSettingsDialog.cpp/h  # Settings dialog (Win32 native controls)
│       │   ├── ClassicTheme.cpp/h     # Dark/light theme for Win32 controls
│       │   ├── NexusKeyLite.rc        # Win32 resource file
│       │   ├── NexusKeyLite.exe.manifest  # DPI + visual styles manifest
│       │   └── resource.h             # Resource IDs
│       ├── main_lite.cpp              # WinMain for Lite/Classic build
│       ├── helpers/
│       │   └── AppHelpers.h           # App-level utility functions
│       ├── ui/                        # HTML/CSS/JS for Sciter dialogs
│       │   ├── settings/              # settings.html/css/js
│       │   ├── excludedapps/          # excludedapps.html/css/js
│       │   ├── tsfapps/              # tsfapps.html/css/js
│       │   ├── macro/                # macro.html/css/js
│       │   ├── appoverrides/         # appoverrides.html/css/js
│       │   ├── convert-tool/         # convert-tool.html/css/js
│       │   ├── about/                # about.html/css
│       │   └── shared/               # Shared UI resources
│       │       ├── theme.css          # Design tokens, colors (10K)
│       │       ├── utils.js           # DOM helpers, event binding (11K)
│       │       ├── strings.js         # i18n string tables (6K)
│       │       ├── i18n.js            # Localization engine
│       │       ├── subdialog.css      # Common subdialog styles
│       │       ├── dropdown.css       # Custom dropdown component
│       │       ├── toggle.css         # Toggle switch component
│       │       └── base.css           # Reset/base styles
│       ├── resources.cpp              # Auto-generated packed UI (538K)
│       └── resources/                 # Icons (ico files)
│
├── tests/                             # Google Test
│   ├── TelexEngineTest.cpp            # ★ 72K — most comprehensive
│   ├── FeatureOptionsTest.cpp         # 29K — feature flag combos
│   ├── SpellCheckerTest.cpp           # 22K
│   ├── CodeTableConverterTest.cpp     # 20K
│   ├── ConfigManagerTest.cpp          # 10K — Win32 only
│   ├── VniEngineTest.cpp              # 8K
│   ├── EngineFactoryTest.cpp          # 8K
│   ├── SharedStateTest.cpp            # 6K
│   ├── ConfigEventTest.cpp            # 2K — Win32 only
│   └── TestHelper.h                   # Shared test utilities
│
├── docs/                              # Documentation (see docs/index.md)
│   ├── Architecture/                  # System architecture (sharded, 12 files)
│   ├── CODING_RULES/                  # Coding standards (sharded, 10 files)
│   ├── telex-test-specification/      # Telex test cases (sharded, 21 files)
│   ├── vietnamese-phonology-spec-distillate.md  # Typing rules (distilled)
│   ├── SECURITY_FIXES-distillate.md   # Security fixes (distilled)
│   ├── tray-icon-sync-analysis-v2-distillate.md # Tray icon sync (distilled)
│   ├── Planning.md                    # Feature roadmap (24K)
│   ├── tsf-hook-coordination.md       # TSF/Hook interplay (4K)
│   ├── subdialog-checklist.md         # Subdialog creation guide (4K)
│   ├── plans/                         # Implementation plans
│   └── diagrams/                      # Visual diagrams
│
├── extern/                            # Vendored dependencies
│   ├── googletest/                    # Google Test v1.14.0
│   ├── tomlplusplus/                  # TOML parser
│   └── sciter/                        # Sciter SDK (JS engine + UI)
│       └── bin/packfolder.exe         # Pack UI → resources.cpp
│
├── CMakeLists.txt                     # Build system (single file)
├── CLAUDE.md                          # AI assistant context
├── BUILD.md                           # Build instructions
└── README.md                          # Project overview
```

---

## Quick Reference: Where To Look

| Task | Go to |
|---|---|
| Fix typing/diacritics bug | `src/core/engine/TelexEngine.cpp` or `VniEngine.cpp` |
| Fix spell checking | `src/core/engine/SpellChecker.cpp` |
| Change encoding conversion | `src/core/engine/CodeTableConverter.cpp` |
| Add/change config option | `src/core/config/TypingConfig.h` → `ConfigManager.cpp` |
| Fix EXE↔DLL sync | `src/core/ipc/SharedState.h` → `SharedStateManager.cpp` |
| Fix TSF composition | `src/tsf/EngineController.cpp` → `CompositionManager.cpp` |
| Fix TSF key handling | `src/tsf/KeyEventSink.cpp` |
| Fix language bar icon | `src/tsf/LanguageBarButton.cpp` |
| Fix hook-based input | `src/app/system/HookEngine.cpp` |
| Change settings UI | `src/app/dialogs/SettingsDialog.cpp` + `src/app/ui/settings/` |
| Add new subdialog | See `docs/subdialog-checklist.md` |
| Fix tray icon/menu | `src/app/system/TrayIcon.cpp` |
| Fix quick consonant | `src/app/system/QuickConvert.cpp` |
| Change Classic/Lite UI | `src/app/classic/ClassicSettingsDialog.cpp` + `ClassicTheme.cpp` |
| Change themes/colors | `src/app/ui/shared/theme.css` (Sciter) or `ClassicTheme.cpp` (Classic) |
| Add/change i18n strings | `src/app/ui/shared/strings.js` + `i18n.js` |
| Fix auto-update | `src/app/system/UpdateChecker.cpp` → `UpdateInstaller.cpp` |
| Fix hotkey handling | `src/app/system/HotkeyManager.cpp` |
| Add tests | `tests/` — follow existing `*Test.cpp` pattern |

---

## Data Flow

```
┌──────────────────── NextKeyApp (EXE) ────────────────────┐
│  main.cpp → TrayIcon → SettingsDialog → ConfigManager    │
│                ↕              ↕                           │
│         HookEngine    SciterSubDialogs                   │
│         (fallback)    (subprocess UI)                    │
└────────────┬─────────────────────────────────────────────┘
             │  SharedState (memory-mapped file)
             │  ConfigEvent (named event)
┌────────────┴─────────────────────────────────────────────┐
│  NextKeyTSF (DLL) — loaded per-process by Windows        │
│  TextService → KeyEventSink → EngineController           │
│     ↕              ↕               ↕                     │
│  Register   CompositionManager  TelexEngine/VniEngine    │
│             LanguageBarButton   SpellChecker             │
└──────────────────────────────────────────────────────────┘
```

---

## TelexEngine Internal Architecture

> Read this section before debugging any diacritics/tone bug in `TelexEngine.cpp`.

### PushChar() Processing Pipeline

```
PushChar(c)
  ├─ 0a. Quick start consonant (f→ph, j→gi, w→qu) — word start only
  ├─ 0b. Quick consonant (cc→ch, gg→gi, nn→ng, ...) — after consonant
  ├─ 1a. 'z' key → clear existing tone
  ├─ 1b. Tone keys (s,f,r,x,j) → ProcessTone() → FindToneTarget()
  ├─ 2a. Modifier keys → ProcessModifier()
  │       ├─ Brackets: [ → ơ, ] → ư
  │       ├─ 'w' → ProcessWModifier() (horn/breve, 8 priority levels)
  │       ├─ Double vowel → circumflex (aa→â, ee→ê, oo→ô)
  │       │       ├─ Direct: last char matches (e.g., "a" + 'a' → "â")
  │       │       └─ Free marking: backward scan across intervening chars
  │       │               (e.g., "tieng" + 'e' → "tiêng")
  │       │               Crosses consonants freely; crosses vowels only
  │       │               when spell check validates the result
  │       └─ dd → đ (ProcessDModifier)
  ├─ 2b. Quick end consonant (g→ng, h→nh, k→ch) — after vowel
  └─ 3.  Regular character → ProcessChar()
  Then: ApplyAutoUO() + UpdateSpellState()
```

### Tone Placement Priority (FindToneTargetImpl)

```
FindToneTarget()
  ├─ P1: Horn vowel (ư, ơ) — last one wins (for ươ pair)
  ├─ P2: Modified vowel (â, ê, ô, ă) — first one found
  ├─ P3: Diphthong/triphthong table lookup
  │       ├─ Triphthong (modern only): tone on MIDDLE vowel (oai, uyu, ...)
  │       └─ Diphthong: kDiphthongClassic/Modern in VietnameseTables.h
  │           rule=1 → first vowel
  │           rule=2 → second vowel
  │           rule=3 → coda-aware (SECOND if coda exists, ELSE FIRST)
  └─ P4: Default → rightmost vowel
  Special: "gi" cluster ('i' skipped), "qu" cluster ('u' skipped)
```

### Modifier Application Priority (ProcessWModifier)

```
ProcessWModifier()
  P1: "ua" → horn on 'u' (mưa)     P5: standalone 'u' → horn
  P2: "uo" → horn on 'o' (ươ)      P6: standalone 'o' → horn
  P3: "oa" → breve on 'a' (hoặc)   P7: standalone 'a' → breve
  P4: Escape (clear horn/breve)     P8: no target → insert 'ư'
```

### Key Interactions Between Subsystems

| Action | Triggers | Why it matters |
|---|---|---|
| Circumflex applied | → `RelocateToneToTarget()` | Tone may need to move to newly-modified vowel |
| Regular char added | → `RelocateToneToTarget()` | Tone relocates when a new vowel forms a diphthong/coda (e.g. hofa -> hoà) |
| Horn applied | → `RelocateToneToHornVowel()` | Horn vowels have highest tone priority |
| Any char after ơ | → `ApplyAutoUO()` | Auto-horns preceding 'u' (u+ơ → ư+ơ) |
| Every PushChar/Backspace | → `UpdateSpellState()` | Sets `spellCheckDisabled_` if invalid syllable |
| `spellCheckDisabled_` = true | Tone keys become literal chars | Free marking blocked, tone blocked |
| Free marking crosses vowels | → `SpellCheck::Validate()` | Tentative apply + validate, undo if invalid |

### State Model (CharState)

Each character in the buffer is a `CharState` with: `base` (lowercase letter), `mod` (None/Circumflex/Breve/Horn), `tone` (None/Acute/Grave/Hook/Tilde/Dot), `isUpper`, `rawIdx`, `toneRawIdx`. Composition (`Compose()`) combines base+mod+tone into a single Unicode character via flat array lookups in `VietnameseTables.h`.

---

## Largest Files (by code complexity)

| File | Size | Notes |
|---|---|---|
| `HookEngine.cpp` | 63K | Keyboard hook fallback — most complex |
| `SettingsDialog.cpp` | 45K | Main settings UI logic |
| `TelexEngine.cpp` | 34K | Core Telex algorithm |
| `CodeTableConverter.cpp` | 30K | Charset conversion tables |
| `SpellChecker.cpp` | 26K | Vietnamese spell validation |
| `ConfigManager.cpp` | 24K | TOML config load/save |
| `main.cpp` | 23K | App initialization |
| `VniEngine.cpp` | 18K | VNI typing method |
| `EngineController.cpp` | 17K | TSF engine orchestrator |
| `QuickConvert.cpp` | 15K | Quick consonant shortcuts |
