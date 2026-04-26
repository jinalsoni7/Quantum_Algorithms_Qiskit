# Quantum Algorithms with Qiskit

A comprehensive collection of quantum algorithms implemented using IBM's Qiskit framework. This repository contains implementations of key quantum algorithms, including oracle-based algorithms and search algorithms, with both notebook and Python script versions.

## Table of Contents

- [Overview](#overview)
- [Algorithms](#algorithms)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Overview

This project demonstrates practical implementations of various quantum algorithms ranging from foundational examples to advanced search and factorization algorithms. Each algorithm includes detailed documentation and both interactive notebook and standalone script versions.

## Algorithms

### 1. Hello World
A simple introduction to Qiskit demonstrating:
- Bell state creation
- Pauli observable estimation
- Expectation value computation

**Files:** `hello_world.py`, `demo.ipynb`  
**Location:** `Hello World/`

### 2. Quantum Oracle
Demonstrates a quantum oracle for the function f(x) = ~x:
- Oracle circuit construction
- Bell state preparation
- Circuit simulation and measurement

**Files:** `quantum_oracle.py`, `demo.ipynb`  
**Location:** `Quantum Oracle/`

### 3. Phase Oracle
Implements a phase oracle for f(x) = x:
- Phase kickback mechanism
- Ancilla qubit preparation
- Observable measurement

**Files:** `phase_oracle.py`, `demo.ipynb`  
**Location:** `Phase Oracle/`

### 4. Deutsch's Algorithm
Determines if a function is constant or balanced using a single query:
- Oracle implementation for f(x) = x
- Superposition and interference
- Deterministic function property detection

**Files:** `deutsch_algo.py`, `demo.ipynb`  
**Location:** `Deutsch's Algorithm/`

### 5. Deutsch-Jozsa Algorithm
Extends Deutsch's algorithm to n input qubits:
- Multi-qubit superposition
- Balanced function detection
- Exponential speedup demonstration

**Files:** `deutsch_jozsa_algo.py`, `demo.ipynb`  
**Location:** `Deutsch-Jozsa Algorithm/`

### 6. Bernstein-Vazirani Algorithm
Finds a hidden bit string in a single query:
- 6-qubit input register
- Oracle with multiple controlled gates
- Secret string recovery via measurement

**Files:** `berstein_vazirani_algo.py`, `demo.ipynb`  
**Location:** `Berstein-Vazirani Algorithm/`

### 7. Simon's Algorithm
Finds the period of a 2-to-1 function:
- Multi-controlled X gate construction
- Measurement sample collection
- Linear algebra over GF(2) for solving

**Files:** `simon_algo.py`, `Simon's_Algorithm.ipynb`  
**Location:** `Simon's Algorithm/`

### 8. Grover's Algorithm
Unstructured search algorithm for finding a marked state:
- 5-qubit search register with 1 ancilla
- Oracle and diffusion operator construction
- Amplitude amplification (~sqrt(N) speedup)

**Files:** `grover_algo.py`, `Grover_Algorithm.ipynb`  
**Location:** `Grover's Algorithm/`

### 9. Shor's Algorithm
Classical demonstration of integer factorization:
- GCD computation
- Classical order finding (using sympy)
- Potential factor extraction

**Files:** `shor_algo.py`, `Shor_Algorithm.ipynb`  
**Location:** `Shor's Algorithm/`

## Project Structure

```
Quantum_Algorithms_Qiskit/
├── README.md                              # This file
├── Hello World/
│   ├── hello_world.py
│   ├── demo.ipynb
│   └── README.md
├── Quantum Oracle/
│   ├── quantum_oracle.py
│   ├── demo.ipynb
│   └── README.md
├── Phase Oracle/
│   ├── phase_oracle.py
│   ├── demo.ipynb
│   └── README.md
├── Deutsch's Algorithm/
│   ├── deutsch_algo.py
│   ├── demo.ipynb
│   └── README.md
├── Deutsch-Jozsa Algorithm/
│   ├── deutsch_jozsa_algo.py
│   ├── demo.ipynb
│   └── README.md
├── Berstein-Vazirani Algorithm/
│   ├── berstein_vazirani_algo.py
│   ├── demo.ipynb
│   └── README.md
├── Simon's Algorithm/
│   ├── simon_algo.py
│   ├── Simon's_Algorithm.ipynb
│   └── README.md
├── Grover's Algorithm/
│   ├── grover_algo.py
│   ├── Grover_Algorithm.ipynb
│   └── README.md
├── Shor's Algorithm/
│   ├── shor_algo.py
│   ├── Shor_Algorithm.ipynb
│   └── README.md
├── quantum_oracle.py
├── phase_oracle.py
├── deutsch_algo.py
├── deutsch_jozsa_algo.py
├── berstein_vazirani_algo.py
├── simon_algo.py
├── grover_algo.py
└── shor_algo.py
```

## Requirements

All algorithms require Python 3.8 or higher. Specific package requirements:

### Core Packages
- **qiskit** (v0.37+): Quantum circuit framework
- **qiskit-aer** (v0.11+): Quantum simulator
- **matplotlib** (v3.4+): Plotting and visualization

### Optional Packages
- **sympy** (for Shor's Algorithm): Number theory functions

Install all requirements with:

```bash
pip install qiskit qiskit-aer matplotlib sympy
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jinalsoni7/Quantum_Algorithms_Qiskit.git
cd Quantum_Algorithms_Qiskit
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install qiskit qiskit-aer matplotlib sympy
```

## Usage

### Running Python Scripts

Run any algorithm script directly:

```bash
# Example: Run Deutsch's Algorithm
python deutsch_algo.py

# Example: Run Grover's Algorithm
python grover_algo.py
```

### Running Jupyter Notebooks

Launch Jupyter and open the notebook files:

```bash
jupyter notebook
```

Then navigate to any `demo.ipynb` or `*_Algorithm.ipynb` file and run the cells.

### Example: Running Grover's Algorithm

```bash
python grover_algo.py
```

## Algorithm Complexity Summary

| Problem | Classical Queries | Quantum Algorithm | Quantum Queries | Asymototic Speedup |
|-----------|-----------|---------|-------|-------------|
| n-bit Parity | n | Deutsch | n/2 | None |
| Constant vs Balanced | 1 | Deutsch-Jozsa | 1 | None |
| Dot Product String | n | Bernstein-Vazirani | 1 | Plynomial |
| XOR Mask | 2^(n/2) | Simon | n | Exponential |
| Unstructured Searching | N | Grover | √N | Quadratic |
| Factorization | n³ log n | Shor | n^3 | Polynomial |

## Learning Path

1. **Beginners:** Start with Hello World and Quantum/Phase Oracles
2. **Intermediate:** Move to Deutsch and Deutsch-Jozsa algorithms
3. **Advanced:** Explore Simon's, Grover's, and Shor's algorithms

## Resources

- [Qiskit Official Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Composer](https://quantum-computing.ibm.com/composer)

## Contributing

Contributions are welcome! Please feel free to:
- Report issues
- Submit pull requests
- Suggest improvements
- Share additional quantum algorithms

## Author

**Jinal Soni**

- GitHub: [@jinalsoni7](https://github.com/jinalsoni7)
- Repository: [Quantum_Algorithms_Qiskit](https://github.com/jinalsoni7/Quantum_Algorithms_Qiskit)

---

**Last Updated:** April 25, 2026

