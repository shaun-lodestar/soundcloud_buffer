import os
from pydub import AudioSegment

def add_silence_to_wav(file_path, output_dir, silence_duration_ms=750):
    audio = AudioSegment.from_wav(file_path)
    silence = AudioSegment.silent(duration=silence_duration_ms)
    final_audio = silence + audio

    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    new_name = f"{name}_SCbuffer{ext}"
    output_path = os.path.join(output_dir, new_name)

    final_audio.export(output_path, format="wav")
    print(f"Saved: {output_path}")

def process_all_wavs_in_current_folder():
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "soundcloud_buffer")
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(current_dir):
        if file.lower().endswith('.wav') and '_SCbuffer' not in file:
            full_path = os.path.join(current_dir, file)
            add_silence_to_wav(full_path, output_dir)

if __name__ == "__main__":
    process_all_wavs_in_current_folder()