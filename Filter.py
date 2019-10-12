from collections import namedtuple

Spectrum = namedtuple('Spectrum', ['amplitude', 'phase'])


def filter_spectrum(spectrum, low_bound=None, high_bound=None):
    spectrum_length = min(len(spectrum.amplitude), len(spectrum.phase))

    low = low_bound if low_bound is not None else 0
    high = high_bound if high_bound is not None else spectrum_length
    filtered_amplitude = [0.0] * low
    filtered_phase = [0.0] * low

    for i in range(low, high):
        filtered_amplitude.append(spectrum.amplitude[i])
        filtered_phase.append(spectrum.phase[i])

    filtered_amplitude += [0.0] * (spectrum_length - high)
    filtered_phase += [0.0] * (spectrum_length - high)
    return Spectrum(filtered_amplitude, filtered_phase)
