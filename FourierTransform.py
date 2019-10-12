import math


class FourierTransformer:
    def __init__(self, sequence):
        self.__sequence = sequence

    def get_cosine_component_amplitude(self, harmonic_number):
        sequence_length = len(self.__sequence)
        trigonometric_const_part = 2 * math.pi * harmonic_number / sequence_length
        cosine_component = 0
        for i in range(sequence_length):
            cosine_component += self.__sequence[i] * math.cos(trigonometric_const_part * i)
        return 2 * cosine_component / sequence_length

    def get_sinus_component_amplitude(self, harmonic_number):
        sequence_length = len(self.__sequence)
        trigonometric_const_part = 2 * math.pi * harmonic_number / sequence_length
        sinus_component = 0
        for i in range(sequence_length):
            sinus_component += self.__sequence[i] * math.sin(trigonometric_const_part * i)
        return 2 * sinus_component / sequence_length

    def get_amplitude(self, harmonic_number):
        return math.sqrt(self.get_cosine_component_amplitude(harmonic_number) ** 2
                         + self.get_sinus_component_amplitude(harmonic_number) ** 2)

    def get_initial_phase(self, harmonic_number):
        return math.atan(self.get_sinus_component_amplitude(harmonic_number)
                         / self.get_cosine_component_amplitude(harmonic_number))
