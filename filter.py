from collections import namedtuple

Spectrum = namedtuple('Spectrum', ['amplitude', 'phase'])


def filter_spectrum(spectrum, low_bound=None, high_bound=None):
    spectrum_length = min(len(spectrum.amplitude), len(spectrum.phase))

    low = min(low_bound if low_bound is not None else 0, spectrum_length // 2)
    high = min(high_bound if high_bound is not None else spectrum_length // 2, spectrum_length // 2)
    filtered_amplitude = []
    filtered_phase = []

    def get_symmetric_index(index):
        return index if index < spectrum_length // 2 else spectrum_length - index

    for i in range(spectrum_length):
        symmetric_i = get_symmetric_index(i)
        filtered_amplitude.append(spectrum.amplitude[i] if low < symmetric_i < high else 0.0)
        filtered_phase.append(spectrum.phase[i] if low < symmetric_i < high else 0.0)

    return Spectrum(filtered_amplitude, filtered_phase)
