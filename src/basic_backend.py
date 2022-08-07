import os
os.system('color')  # that ANSI escape sequence start working


class Colors:  # define terminal colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HashCheck(Colors):

    def __init__(self, hash1, hash2):
        self.hash1 = hash1.lower()
        self.hash2 = hash2.lower()
        self.max_len = max(len(hash1), len(hash2))

    def check_length(self) -> bool:
        """
        Check length of both hashes.
        :param hash1: Hash 1.
        :param hash2: Hash 2.
        :return: True: have the same length. False: Length differs.
        """
        if len(self.hash1) != len(self.hash2):
            return False
        return True

    def get_diff(self) -> list:
        """
        Find the positions of difference.
        :return: List with position numbers.
        """
        return [i for i in range(self.max_len) if self.hash1[i] != self.hash2[i]]

    def print_hash(self, hash_value: str) -> None:
        """
        Compares each letter/symbol of the two hashes and marks it OK or FAIL.
        :param hash_value: Hash string to check.
        """
        for i, symbol in enumerate(hash_value):
            if i in self.get_diff():
                print(Colors.FAIL + symbol + Colors.ENDC, end='')
            else:
                print(symbol, end='')
        print('')


def check_inputs(h1: str, h2: str) -> bool:
    """
    Check if 2 hashes/files are given.
    :param h1: hash text or file 1.
    :param h2: hash text or file 2.
    :return: True: 2 hashes are given; False: one or none.
    """
    state = False

    if h1 and h2:
        state = True
    return state
