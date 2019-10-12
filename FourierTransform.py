import math


class FourierTransformer:
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
        return math.atan(self.get_sinus_component_amplitude(harmonic_number)
                         / self.get_cosine_component_amplitude(harmonic_number))

    def get_amplitude_spectrum(self):
        sequence_length = len(self.__sequence)
        return [self.get_amplitude(j) for j in range(sequence_length)]

    def get_phase_spectrum(self):
        sequence_length = len(self.__sequence)
        return [self.get_initial_phase(j) for j in range(sequence_length)]
