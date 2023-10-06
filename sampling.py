import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os


def generate_gif_from_audio(audio_file, output_gif, duration=10, interval=0.1):
    # Load audio file
    y, sr = librosa.load(audio_file, sr=None, duration=duration)

    # Create a list to hold frames
    frames = []

    # Generate images for the GIF
    for end_time in np.arange(interval, duration + interval, interval):
        start_sample = 0
        end_sample = int(end_time * sr)

        num_samples = end_sample - start_sample
        sample_every = num_samples // 100  # for roughly 100 sample points

        times = librosa.samples_to_time(np.arange(start_sample, end_sample), sr=sr)

        plt.figure(figsize=(10, 6))
        plt.plot(times, y[start_sample:end_sample], color='b', label='Continuous Signal')
        plt.plot(times[::sample_every], y[start_sample:end_sample:sample_every], 'ro', label='Sampled Signal')
        plt.title(f"Sampling Representation: {end_time:.1f} seconds")
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)

        # Add signature to the bottom of the plot
        plt.figtext(0.15, 0.02, "Jessica Nono 2023", ha="center", fontsize=10,
                    bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})

        # Save the current frame to a file and append to frames
        frame_path = f"frame_{end_time:.1f}.png"
        plt.savefig(frame_path)
        frames.append(imageio.imread(frame_path))
        plt.close()
        os.remove(frame_path)

    # Convert frames to GIF
    imageio.mimsave(output_gif, frames, duration=interval)


generate_gif_from_audio('/Users/jessicakamdem/Desktop/testsong.mp3', 'output_image.gif')
