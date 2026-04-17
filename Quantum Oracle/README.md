# Quantum Oracle

This folder demonstrates a quantum oracle for the function `f(x) = ~x`.

## Files

- `demo.ipynb`: Notebook version of the quantum oracle demonstration.
- `quantum_oracle.py`: Standalone Python script that builds the oracle, constructs the full circuit, and simulates the result.

## Requirements

- Python 3.8+
- `qiskit`
- `qiskit-aer`
- `matplotlib`

Install required packages with:

```bash
pip install qiskit qiskit-aer matplotlib
```

## Running

```bash
python "Quantum Oracle/quantum_oracle.py"
```

## Description

The script creates an oracle gate for `f(x) = ~x`, prepares the input qubits, applies the oracle, and simulates the circuit using Qiskit Aer. The results are printed and visualized with a histogram.