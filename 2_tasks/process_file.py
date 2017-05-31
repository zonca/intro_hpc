import time
import numpy as np
from pathlib import Path

def analyze(input_filename):
    filename = Path(input_filename)
    print("Processing {}".format(filename))

    output_filename = filename.parent / "output" / ("out_" + filename.name)

    sleep_minutes = 1
    time.sleep(sleep_minutes * 60)

    print("Writing output file {}".format(output_filename))

    output_filename.parent.mkdir(exist_ok=True)
    output_file = open(output_filename, "w")
    output_file.close()

if __name__ == "__main__":
    import sys
    analyze(sys.argv[1])
