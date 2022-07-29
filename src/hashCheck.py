# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Script to (manually) check two hash values. """

import os
from argparse import ArgumentParser
os.system('color')  # that ANSI escape sequence start working

__version__ = "1.0"
__author__ = "klaus-moser"


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
        self.check_length(hash1=hash1, hash2=hash2)
        self.hash1 = hash1.lower()
        self.hash2 = hash2.lower()
        self.max_len = max(len(hash1), len(hash2))

    @staticmethod
    def check_length(hash1, hash2) -> None:
        """
        Check length of both hashes.
        """
        if len(hash1) != len(hash2):
            exit("Hashes differ in length!")

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


if __name__ == "__main__":
    parser = ArgumentParser()  # setup parser
    parser.add_argument("hash1", type=str, help="First hash value.")
    parser.add_argument("hash2", type=str, help="Second hash value.")
    args = parser.parse_args()  # parse arguments

    hash_1 = args.hash1
    hash_2 = args.hash2

    h = HashCheck(hash_1, hash_2)

    print('Hash1:\t', end='')
    h.print_hash(hash_value=hash_1)

    print('Hash2:\t', end='')
    h.print_hash(hash_value=hash_2)

    if hash_1 == hash_2:
        print(Colors.OKGREEN + 'IDENTICAL!' + Colors.ENDC)
    else:
        print(Colors.FAIL + 'NOT IDENTICAL!' + Colors.ENDC)
