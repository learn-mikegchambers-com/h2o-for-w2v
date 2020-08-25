import numpy as np

class helper():

    def nearest_word(vector, words):
        return_word = ''
        current_distance = 10000
        for w in words:
            distance = np.linalg.norm(vector-words[w])
            if distance < current_distance:
                return_word = w
                current_distance = distance
        return return_word