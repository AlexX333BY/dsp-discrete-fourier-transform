from fourier_transform import DirectFourierTransformer, InverseFourierTransformer, FastFourierTransformer
import math
import random
from filter import Spectrum, filter_spectrum
from graphs import GraphDrawer, Graph
import argparse


def generate_harmonic_sequence(length):
    return [10 * math.cos(2 * math.pi * i / length) for i in range(length)]


def generate_polyharmonic_sequence(length):
    polyharmonics_count = 30
    amplitudes = [1, 3, 5, 8, 10, 12, 16]
    phases = [math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, 3 * math.pi / 4, math.pi]
    chosen_amplitudes = [random.choice(amplitudes) for _ in range(polyharmonics_count)]
    chosen_phases = [random.choice(phases) for _ in range(polyharmonics_count)]
    return [sum(chosen_amplitudes[j] * math.cos(2 * math.pi * j * i / length - chosen_phases[j])
                for j in range(polyharmonics_count)) for i in range(length)]


def task_2(sequence_length, phase_filtering):
    harmonic_sequence = generate_harmonic_sequence(sequence_length)
    direct_transformer = DirectFourierTransformer(harmonic_sequence)
    amplitude_spectrum = direct_transformer.get_amplitude_spectrum()
    phase_spectrum = [x if amplitude_spectrum[i] > phase_filtering else 0
                      for i, x in enumerate(direct_transformer.get_phase_spectrum())]
    restored_sequence = InverseFourierTransformer(amplitude_spectrum, phase_spectrum).restore_harmonic()

    drawer = GraphDrawer()
    drawer.add_graph(Graph(range(sequence_length), harmonic_sequence, "Original sequence"))
    drawer.add_graph(Graph(range(sequence_length), amplitude_spectrum, "Amplitude spectrum"))
    drawer.add_graph(Graph(range(sequence_length), phase_spectrum, "Phase spectrum"))
    drawer.add_graph(Graph(range(sequence_length), restored_sequence, "Restored sequence"))
    drawer.draw()
    drawer.show()


def task_3(sequence_length, phase_filtering):
    polyharmonic_sequence = generate_polyharmonic_sequence(sequence_length)
    direct_transformer = DirectFourierTransformer(polyharmonic_sequence)
    amplitude_spectrum = direct_transformer.get_amplitude_spectrum()
    phase_spectrum = [x if amplitude_spectrum[i] > phase_filtering else 0
                      for i, x in enumerate(direct_transformer.get_phase_spectrum())]
    restored_sequence = InverseFourierTransformer(amplitude_spectrum, phase_spectrum).restore_polyharmonic(True)
    restored_sequence_without_phases \
        = InverseFourierTransformer(amplitude_spectrum, phase_spectrum).restore_polyharmonic(False)

    drawer = GraphDrawer()
    drawer.add_graph(Graph(range(sequence_length), polyharmonic_sequence, "Original sequence"))
    drawer.add_graph(Graph(range(sequence_length), amplitude_spectrum, "Amplitude spectrum"))
    drawer.add_graph(Graph(range(sequence_length), phase_spectrum, "Phase spectrum"))
    drawer.add_graph(Graph(range(sequence_length), restored_sequence, "Restored sequence"))
    drawer.add_graph(Graph(range(sequence_length), restored_sequence_without_phases,
                           "Restored sequence w/o phase spectrum"))
    drawer.draw()
    drawer.show()


def task_4(sequence_length, phase_filtering):
    polyharmonic_sequence = generate_polyharmonic_sequence(sequence_length)
    fast_transformer = FastFourierTransformer(polyharmonic_sequence)
    amplitude_spectrum = fast_transformer.get_amplitude_spectrum()
    phase_spectrum = [x if amplitude_spectrum[i] > phase_filtering else 0
                      for i, x in enumerate(fast_transformer.get_phase_spectrum())]
    restored_sequence = InverseFourierTransformer(amplitude_spectrum, phase_spectrum).restore_polyharmonic(True)

    drawer = GraphDrawer()
    drawer.add_graph(Graph(range(sequence_length), polyharmonic_sequence, "Original sequence"))
    drawer.add_graph(Graph(range(sequence_length), amplitude_spectrum, "Amplitude spectrum"))
    drawer.add_graph(Graph(range(sequence_length), phase_spectrum, "Phase spectrum"))
    drawer.add_graph(Graph(range(sequence_length), restored_sequence, "Restored sequence"))
    drawer.draw()
    drawer.show()


def task_5(sequence_length, phase_filtering):
    parser = argparse.ArgumentParser()
    parser.add_argument('--low', action='store', required=False, help='lower bound of filtering', dest='low', type=int,
                        default=None)
    parser.add_argument('--high', action='store', required=False, help='higher bound of filtering', dest='high',
                        type=int, default=None)
    args = parser.parse_known_args()[0]

    polyharmonic_sequence = generate_polyharmonic_sequence(sequence_length)
    direct_transformer = DirectFourierTransformer(polyharmonic_sequence)
    amplitude_spectrum = direct_transformer.get_amplitude_spectrum()
    phase_spectrum = [x if amplitude_spectrum[i] > phase_filtering else 0
                      for i, x in enumerate(direct_transformer.get_phase_spectrum())]
    filtered = filter_spectrum(Spectrum(amplitude_spectrum, phase_spectrum), args.low, args.high)
    restored = InverseFourierTransformer(filtered.amplitude, filtered.phase).restore_polyharmonic()

    drawer = GraphDrawer()
    drawer.add_graph(Graph(range(sequence_length), polyharmonic_sequence, "Original sequence"))
    drawer.add_graph(Graph(range(sequence_length), amplitude_spectrum, "Amplitude spectrum"))
    drawer.add_graph(Graph(range(sequence_length), phase_spectrum, "Phase spectrum"))
    drawer.add_graph(Graph(range(sequence_length), filtered.amplitude, "Filtered amplitude"))
    drawer.add_graph(Graph(range(sequence_length), filtered.phase, "Filtered phase"))
    drawer.add_graph(Graph(range(sequence_length), restored, "Restored filtered"))
    drawer.draw()
    drawer.show()


def main():
    tasks_callbacks = {2: task_2, 3: task_3, 4: task_4, 5: task_5}

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', action='store', required=True, help='task number',
                        choices=tasks_callbacks.keys(), dest='task', type=int)
    parser.add_argument('-l', '--length', action='store', required=False, help='sequence length', dest='length',
                        type=int, default=1024)
    parser.add_argument('-f', '--phase-filter', action='store', required=False, help='when to set phase spectrum to 0',
                        dest='filter', type=float, default=0.001)

    args = parser.parse_known_args()[0]
    tasks_callbacks[args.task](args.length, args.filter)


if __name__ == "__main__":
    main()
