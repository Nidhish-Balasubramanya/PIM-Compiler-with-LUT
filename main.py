import streamlit as st
import os
import subprocess
import numpy as np
from backend.translate import read_llvm_ir, write_output

# -----------------------------
# ✅ Setup file directories
# -----------------------------
UPLOAD_DIR = "uploads"
BACKEND_DIR = "backend"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -----------------------------
# ✅ Output file paths
# -----------------------------
ISA_OUTPUT_FILE = os.path.join(BACKEND_DIR, "pim_isa_output.txt")
BINARY_OUTPUT_FILE = os.path.join(BACKEND_DIR, "output_pPIM.isa")
LUT_OUTPUT_FILE = os.path.join(BACKEND_DIR, "lut_output.txt")
LLVM_FILE = os.path.join(BACKEND_DIR, "matrix.ll")
MATRIX_FILE = os.path.join(BACKEND_DIR, "matrix_input.txt")

# -----------------------------
# ✅ Streamlit UI Layout
# -----------------------------
st.title("🔧 PIM Compiler with LUT")
st.write("Upload a .cpp file and input matrices, then download the ISA instructions, PIM binary, and LUT output.")

# Upload C++ file
cpp_file = st.file_uploader("Upload your C++ Matrix Multiplication Program", type=["cpp"])

# Matrix dimensions
rows = st.number_input("Matrix Rows", min_value=2, max_value=10, value=2)
cols = st.number_input("Matrix Columns", min_value=2, max_value=10, value=2)

# Matrix Input Fields
def create_matrix_input(name, rows, cols):
    st.subheader(name)
    matrix = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        cols_values = st.columns(cols)
        for j in range(cols):
            matrix[i][j] = cols_values[j].number_input(f"{name}[{i}][{j}]", value=0, key=f"{name}_{i}_{j}")
    return matrix

matrix_a = create_matrix_input("Matrix A", rows, cols)
matrix_b = create_matrix_input("Matrix B", rows, cols)

# -----------------------------
# ✅ Compilation and File Generation State
# -----------------------------
if "compiled" not in st.session_state:
    st.session_state.compiled = False

if cpp_file and st.button("Compile and Generate ISA"):
    cpp_path = os.path.join(UPLOAD_DIR, cpp_file.name)
    with open(cpp_path, "wb") as f:
        f.write(cpp_file.getvalue())
    
    with open(MATRIX_FILE, "w") as f:
        f.write("# Matrix A\n")
        np.savetxt(f, matrix_a, fmt='%d')
        f.write("\n# Matrix B\n")
        np.savetxt(f, matrix_b, fmt='%d')

    st.success("✅ Matrix Input File Generated!")

    compile_command = f"clang++ -S -emit-llvm {cpp_path} -o {LLVM_FILE}"

    try:
        subprocess.run(compile_command, shell=True, check=True)
        st.success("✅ LLVM IR Generated!")

        st.write("🔁 Translating LLVM IR to pPIM ISA...")
        llvm_ir = read_llvm_ir()
        write_output()
        
        st.session_state.compiled = True
    except subprocess.CalledProcessError as e:
        st.error(f"❌ Compilation failed: {e}")
    except Exception as e:
        st.error(f"❌ Error during translation: {e}")

# -----------------------------
# ✅ Persist Download Buttons
# -----------------------------
if st.session_state.compiled:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.download_button("📥 Download LLVM IR", open(LLVM_FILE, "rb").read(), "matrix.ll")
    with col2:
        st.download_button("📥 Download ISA Instructions", open(ISA_OUTPUT_FILE, "rb").read(), "pim_isa_output.txt")
    with col3:
        st.download_button("📥 Download Binary PIM", open(BINARY_OUTPUT_FILE, "rb").read(), "output_pPIM.isa")
    with col4:
        st.download_button("📥 Download LUT Output", open(LUT_OUTPUT_FILE, "rb").read(), "lut_output.txt")
