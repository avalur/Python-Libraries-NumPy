import numpy as np


def read_data(file):
    text = np.loadtxt(file, delimiter='.', dtype=np.bytes_)[:, 0]
    decoded_text = np.char.decode(text)
    upper_text = np.char.upper(decoded_text)
    return upper_text


def get_line_lengths(array):
    return np.char.str_len(array)


if __name__ == '__main__':
    uppercase_text = read_data('text.txt')
    line_lengths = get_line_lengths(uppercase_text)
    print(uppercase_text)
    print(line_lengths)