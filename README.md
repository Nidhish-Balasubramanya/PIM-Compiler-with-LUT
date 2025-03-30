###  **PIM Compiler with LUT**

---

###  **Project Overview**

The **PIM Compiler with LUT** is a web-based application that allows users to upload C++ matrix multiplication programs and translate them into **Processing in Memory (PIM)** ISA (Instruction Set Architecture) instructions. The application offers the following functionalities:
- Compilation of C++ matrix multiplication programs into **LLVM Intermediate Representation (IR)**.
- Translation of **LLVM IR** to PIM ISA instructions.
- Generation of **binary PIM output**.
- **Look-Up Table (LUT)** generation for optimized instruction execution.
- Downloadable outputs: LLVM IR, ISA instructions, binary PIM, and LUT files.
- User-friendly web interface built using **Streamlit**.

---

###  **Key Features**

✅ Upload C++ matrix multiplication programs (.cpp).  
✅ Define matrix dimensions and values through the UI.  
✅ Compile and translate programs into PIM ISA.  
✅ Generate and download LLVM IR, PIM ISA, binary PIM, and LUT outputs.  
✅ View ISA instructions and LUT output in downloadable files.  
✅ Streamlit-powered interactive web interface.  

---

###  **Tech Stack Used**
- **Frontend:** Streamlit (Python)  
- **Backend:** Python  
- **Compiler:** Clang for LLVM IR generation  
- **File Handling:** Python for translation and file generation  
- **Output Formats:**  
  - `.ll` → LLVM IR  
  - `.isa` → PIM ISA instructions  
  - `.txt` → LUT output  
  - `.bin` → Binary PIM output  

---

### 💻 **Installation and Execution**

1. **Clone the Repository**
```bash
git clone <repository_link>
cd PIM-Compiler
```

2. **Create a Python Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux
venv\Scripts\activate      # For Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
streamlit run app.py
```

---

### 📂 **Project Structure**

```
/backend
    ├──__init__.py
    ├── lut_output.txt
    ├── matrix.ll
    ├── matrix_input.txt
    ├── output_pPIM.isa
    ├── pim_isa_output.txt
    ├── translate.py
/uploads
    ├── matrix_mul.cpp
main.py
requirements.txt
README.md
/Output Screenshots

```

---

###  **Usage Instructions**

1. **Upload C++ Program:**  
   - On the Streamlit UI, upload your C++ matrix multiplication program (`.cpp` file).

2. **Matrix Configuration:**  
   - Define the dimensions and matrix values using the matrix input forms.

3. **Compile and Translate:**  
   - Click **"Compile and Generate ISA"** to generate:
     - LLVM IR
     - PIM ISA instructions
     - Binary PIM output
     - LUT output

4. **Download Outputs:**  
   - Use the download buttons to save:
     - `.ll` → LLVM IR  
     - `.isa` → PIM ISA  
     - `.bin` → Binary PIM  
     - `.txt` → LUT output  

---

###  **Sample Screenshots**

 **Web Interface:**  
![Webpage](Output%20Screenshots/Webpage-1.jpg)

 **Matrix Input:**  
![Matrix Input](Output%20Screenshots/MAtrix%20input.jpg)

 **Generated Outputs:**
* ![LLVM IR Output](Output%20Screenshots/matrix_ll_preview.jpg) -  LLVM IR output  
* ![PIM ISA Instructions](Output%20Screenshots/ISA%20instructions.jpg) -  PIM ISA instructions  
* ![Binary PIM File](Output%20Screenshots/Binary%20ISA.jpg) - : Binary PIM file  
* ![LUT Output](Output%20Screenshots/LUT_output.jpg) -  Look Up Table 

 **Downloads Available:**  
![Downloadable Files](Output%20Screenshots/downloadable%20files.jpg)

---

###  **How It Works**

1. **LLVM Compilation:**  
   - The uploaded `.cpp` file is compiled into LLVM IR using `clang`.  
   - The IR is saved as `.ll` file.  

2. **PIM ISA Translation:**  
   - The LLVM IR instructions are translated into PIM ISA instructions.  
   - Outputs `.isa` file with translated instructions.  

3. **Binary and LUT Generation:**  
   - Binary PIM output (`.bin`) is generated from the ISA instructions.  
   - LUT (`.txt`) is created with instruction mappings for faster access.  

---

###  **Output Files Explained**

1. **LLVM IR (`.ll`)**
   - Intermediate representation of the compiled C++ code.  
   - Low-level, platform-independent instructions.  

2. **PIM ISA Instructions (`.isa`)**
   - Translated instructions for PIM architecture.  
   - Example:  
   ```
   LOAD R0, A[i][k]  
   ADD R1, R0, R2  
   STORE R1, C[i][j]  
   ```

3. **Binary PIM Output (`.bin`)**
   - PIM machine-readable binary output.  

4. **LUT Output (`.txt`)**
   - Optimized look-up table for instruction execution.  
   - Example:  
   ```
   1 LUT 36 78 55176  
   2 LUT 106 95 2188  
   ```

---

###  **Future Scope**

 **Optimized Compilation:** Improve LLVM optimization passes for better performance.  
 **Multi-File Compilation:** Support for compiling multiple C++ files.  
 **Expanded Instruction Set:** Add support for more complex PIM instructions.  
 **Cloud Deployment:** Deploy as a cloud-based compiler service.  

---

###  **Contributors**
- **Nidhish Balsubramanya**
- **Team Members:**

---

 **Enjoy Using the PIM Compiler with LUT!!!**
