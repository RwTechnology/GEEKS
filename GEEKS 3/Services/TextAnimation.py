import sys
import time
from time import sleep


class TextAnimation:

    @staticmethod
    def animation_text(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)
