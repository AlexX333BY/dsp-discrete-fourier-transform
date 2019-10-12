import math


class DirectFourierTransformer:
    def __init__(self, sequence):
        self.__sequence = sequence

    def get_cosine_component_amplitude(self, harmonic_number):
        sequence_length = len(self.__sequence)
        trigonometric_const_part = 2 * math.pi * harmonic_number / sequence_length
        return 2 * sum(x * math.cos(trigonometric_const_part * i) for i, x in enumerate(self.__sequence)) \
               / sequence_length

    def get_sinus_component_amplitude(self, harmonic_number):
        sequence_length = len(self.__sequence)
        trigonometric_const_part = 2 * math.pi * harmonic_number / sequence_length
        return 2 * sum(x * math.sin(trigonometric_const_part * i) for i, x in enumerate(self.__sequence)) \
               / sequence_length

    def get_amplitude(self, harmonic_number):
        return math.hypot(self.get_cosine_component_amplitude(harmonic_number),
                          self.get_sinus_component_amplitude(harmonic_number))

    def get_initial_phase(self, harmonic_number):
        return math.atan2(self.get_sinus_component_amplitude(harmonic_number),
                          self.get_cosine_component_amplitude(harmonic_number))

    def get_amplitude_spectrum(self):
        sequence_length = len(self.__sequence)
        return [self.get_amplitude(j) for j in range(sequence_length)]

    def get_phase_spectrum(self):
        sequence_length = len(self.__sequence)
        return [self.get_initial_phase(j) for j in range(sequence_length)]


class InverseFourierTransformer:
    def __init__(self, amplitude_spectrum, phase_spectrum):
        self.__spectrum_length = min(len(amplitude_spectrum), len(phase_spectrum))
        self.__amplitude_spectrum = amplitude_spectrum[:self.__spectrum_length]
        self.__phase_spectrum = phase_spectrum[:self.__spectrum_length]

    def restore_harmonic(self):
        terms_count_range = range(self.__spectrum_length // 2)
        trigonometric_const_part = 2 * math.pi / self.__spectrum_length
        return [sum(self.__amplitude_spectrum[j] * math.cos(trigonometric_const_part * j * i - self.__phase_spectrum[j])
                    for j in terms_count_range)
                for i in range(self.__spectrum_length)]

    def restore_polyharmonic(self, consider_phase_spectrum=True):
        phases = self.__phase_spectrum if consider_phase_spectrum else [0] * self.__spectrum_length
        terms_count_range = range(1, self.__spectrum_length // 2)
        trigonometric_const_part = 2 * math.pi / self.__spectrum_length
        return [self.__amplitude_spectrum[0] / 2
                + sum(self.__amplitude_spectrum[j] * math.cos(trigonometric_const_part * j * i - phases[j])
                      for j in terms_count_range)
                for i in range(self.__spectrum_length)]
