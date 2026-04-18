# Deutsch-Jozsa Algorithm

This folder demonstrates the Deutsch-Jozsa algorithm for determining if a function is constant or balanced.

## Files

- `demo.ipynb`: Notebook version of the Deutsch-Jozsa algorithm demonstration.
- `deutsch_jozsa_algo.py`: Standalone Python script that builds the circuit with the oracle, runs the algorithm, and simulates the result.

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
python "Deutsch-Jozsa Algorithm/deutsch_jozsa_algo.py"
```

## Description

The script implements the Deutsch-Jozsa algorithm using 3 input qubits and 1 ancilla. The oracle is for the balanced function f(x) = x, and the algorithm determines the function type. The measurement results are simulated and displayed as a histogram.