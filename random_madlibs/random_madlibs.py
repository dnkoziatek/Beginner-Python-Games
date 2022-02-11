#Call differing madlib files

from sample_madlibs import george
import random

if __name__ == "__main__":
    m = random.choice([george])
    m.madlib()
