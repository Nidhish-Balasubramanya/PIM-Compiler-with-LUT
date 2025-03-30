#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

// Function to read matrix from file
vector<vector<int>> readMatrix(ifstream& file, int rows, int cols) {
    vector<vector<int>> matrix(rows, vector<int>(cols));
    string line;
    for (int i = 0; i < rows; ++i) {
        getline(file, line);
        istringstream iss(line);
        for (int j = 0; j < cols; ++j) {
            iss >> matrix[i][j];
        }
    }
    return matrix;
}

int main() {
    ifstream inputFile("matrix_input.txt");
    if (!inputFile) {
        cerr << "Error: Unable to open input file!" << endl;
        return 1;
    }

    // Matrix dimensions
    int rowsA = 8, colsA = 8;
    int rowsB = 8, colsB = 8;

    // Read matrices A and B
    vector<vector<int>> A = readMatrix(inputFile, rowsA, colsA);
    string skipLine;
    getline(inputFile, skipLine);  // Skip comment line
    vector<vector<int>> B = readMatrix(inputFile, rowsB, colsB);

    // Result matrix C
    vector<vector<int>> C(rowsA, vector<int>(colsB, 0));

    // Complex Matrix Multiplication with additional operations
    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                // Simulate multiple operations to increase ISA instructions
                C[i][j] += A[i][k] * B[k][j];
                C[i][j] -= A[i][k] - B[k][j];
                C[i][j] += A[i][k] + B[k][j];
            }
        }
    }

    // Display result
    cout << "Result Matrix (C):\n";
    for (const auto& row : C) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    inputFile.close();
    return 0;
}