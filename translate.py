import os
import random

# ✅ Define consistent output file paths
ISA_OUTPUT_FILE = "backend/pim_isa_output.txt"
BINARY_OUTPUT_FILE = "backend/output_pPIM.isa"
LUT_OUTPUT_FILE = "backend/lut_output.txt"


def read_llvm_ir():
    """Reads the LLVM IR file and returns it as a string."""
    llvm_file = "backend/matrix.ll"
    with open(llvm_file, "r") as f:
        return f.read()


def generate_isa(llvm_ir):
    """Generates ISA instructions from LLVM IR."""
    isa_instructions = []

    for line in llvm_ir.splitlines():
        if "load" in line:
            isa_instructions.append("LOAD R0, A[i][k]")
        elif "mul" in line:
            isa_instructions.append("LUT_MUL R2, R0, R1")
        elif "store" in line:
            isa_instructions.append("STORE R2, C[i][j]")
        elif "add" in line:
            isa_instructions.append("ADD R3, R1, R2")

    return isa_instructions


def write_binary(isa_instructions):
    """Generates binary representation from ISA instructions."""
    binary_output = []

    for instruction in isa_instructions:
        parts = instruction.split()
        opcode = parts[0]

        # Simulate basic binary encoding
        if opcode == "LOAD":
            binary_output.append("01 000010 0000000000000000")
        elif opcode == "LUT_MUL":
            binary_output.append("01 000011 0000000000000000")
        elif opcode == "STORE":
            binary_output.append("01 000100 0000000000000000")
        elif opcode == "ADD":
            binary_output.append("01 000101 0000000000000000")
        else:
            binary_output.append("01 111111 0000000000000000")

    return binary_output


def generate_lut(isa_instructions):
    """Generates LUT output data."""
    lut_output = []

    for _ in isa_instructions:
        # Simulate LUT output with random values
        lut_output.append(f"LUT {random.randint(0, 255)} {random.randint(0, 255)} {random.randint(0, 65535)}")

    return lut_output


def write_output():
    """Generates and writes PIM ISA, Binary, and LUT outputs to files."""

    # ✅ Ensure the backend folder exists
    os.makedirs("backend", exist_ok=True)

    # ✅ Read LLVM IR
    llvm_ir = read_llvm_ir()

    # ✅ Generate ISA, Binary, and LUT outputs
    isa_instructions = generate_isa(llvm_ir)

    # ✅ Write ISA to file
    with open(ISA_OUTPUT_FILE, "w") as f:
        f.write("\n".join(isa_instructions))

    # ✅ Write Binary output to file
    binary_data = write_binary(isa_instructions)
    with open(BINARY_OUTPUT_FILE, "w") as f:
        f.write("\n".join(binary_data))

    # ✅ Write LUT output to file
    lut_data = generate_lut(isa_instructions)
    with open(LUT_OUTPUT_FILE, "w") as f:
        f.write("\n".join(lut_data))

    print("✅ Output files generated:")
    print(f" - ISA Instructions → {ISA_OUTPUT_FILE}")
    print(f" - Binary ISA → {BINARY_OUTPUT_FILE}")
    print(f" - LUT Output → {LUT_OUTPUT_FILE}")