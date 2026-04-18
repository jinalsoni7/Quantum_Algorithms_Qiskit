# Berstein-Vazirani Algorithm

This folder demonstrates the Bernstein-Vazirani algorithm to find a hidden bit string.

## Files

- `demo.ipynb`: Notebook version of the Bernstein-Vazirani algorithm demonstration.
- `berstein_vazirani_algo.py`: Standalone Python script that builds the circuit with the oracle, runs the algorithm, and simulates the result.

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
python "Berstein-Vazirani Algorithm/berstein_vazirani_algo.py"
```

## Description

The script implements the Bernstein-Vazirani algorithm using 6 input qubits and 1 ancilla. The oracle encodes the secret string '101001', and the algorithm determines this string in a single query. The results are simulated and displayed as a histogram.