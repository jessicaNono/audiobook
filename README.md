# Audio Sampling Visualization

Visualize the process of audio sampling with this Python script. The script loads an audio track, plots its waveform continuously over a 10-second interval, and superimposes the sampled points, providing a visual representation of how audio is digitized.

## Prerequisites

- Python 3.x
- Pip (Python Package Installer)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/jessicaNono/audiobook.git
    cd audiobook
    ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:

    On macOS and Linux:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

    On Windows:
    ```bash
    py -m venv env
    .\env\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the audio file you want to visualize in the root directory or provide the path to it.

2. Run the script:

    ```bash
    python sampling.py
    ```

3. The output will be saved as `output_image.gif` in the root directory.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details (if you have a license file, otherwise you can remove this line).

---

