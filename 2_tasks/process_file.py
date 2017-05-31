import sys
import time
import numpy as np
from pathlib import Path

filename = Path(sys.argv[1])
print("Processing {}".format(filename))

output_filename = filename.parent / "output" / ("out_" + filename.name)

sleep_minutes = 1
time.sleep(sleep_minutes * 60)

print("Writing output file {}".format(output_filename))

output_filename.parent.mkdir(exist_ok=True)
output_file = open(output_filename, "w")
output_file.close()
