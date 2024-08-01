# Usage:

1. Install dependencies:
   ```bash
   pip install mido
   pip install python-rtmidi
   ```
   **Note:** `mido` is dependent on `python-rtmidi`, not to be mistaken for `rtmidi`. You MUST NOT install `rtmidi`; otherwise, the .venv will need to be recreated.

2. Run the script.

3. If "No Ports are Visible", open "Audio MIDI Setup" on macOS:
   - Press `Command + 2` to open "MIDI Studio".
   - Locate the "IAC Driver" and double-click it.
   - Ensure the "Device is Online" checkbox is enabled.

## Purpose:
This script measures the CPU usage of a specific application while sending MIDI notes to a DAW. This tool is not intended to objectively measure the performance of a plugin but rather to compare different settings and observe the differences in performance between various VSTs, presets, or DAW settings such as sample rate, audio interface, and buffer size.