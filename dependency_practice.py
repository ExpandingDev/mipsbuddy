from content_generation import generate_random_example_sequence
import dependencies as deps
import mips_instructions as mi

import sys
import random
import time

# Probabilities of each instruction type in our sequences
r_mix = 0.5
i_arith_mix = 0.15
load_mix = 0.18
store_mix = 0.12
branch_mix = 0.049
j_mix = 0.001

INSTRUCTION_MIX = [r_mix, i_arith_mix, load_mix, store_mix, branch_mix, j_mix]

# Default values for args
sequence_count = 1
sequence_size = 6
register_count = 8



def generate_deps_report(seq, rf):
    deps = DependencyReport()
    history = []
    for r in rf:
        history.append(RegisterAccessHistory(r))

    return deps

# Parse user input args
if len(sys.argv) > 1:
    sequence_count = int(sys.argv[1])

if len(sys.argv) > 2:
    sequence_size = int(sys.argv[2])

if len(sys.argv) > 3:
    register_count = int(sys.argv[3])

print("Generating " + str(sequence_count) + " sequences of " + str(sequence_size) + " instructions long")

for i in range(0, sequence_count):
    seq = generate_random_example_sequence(INSTRUCTION_MIX, sequence_size, register_count)
    print(seq)
    i += 1
