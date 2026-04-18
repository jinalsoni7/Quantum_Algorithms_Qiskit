# Simon's Algorithm

This folder demonstrates Simon's algorithm to find the hidden period of a 2-to-1 function.

## Files

- `demo.ipynb`: Notebook version of Simon's algorithm demonstration.
- `simon_algo.py`: Standalone Python script that builds the oracle, runs the algorithm, collects samples, and solves for the secret string.

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
python "Simon's Algorithm/simon_algo.py"
```

## Description

The script implements Simon's algorithm using 2 input qubits and 2 output qubits. It randomly selects a secret string s, builds the corresponding oracle, runs the quantum algorithm to collect measurement samples, and solves for s using linear algebra over GF(2). The results are printed, showing the recovered secret.