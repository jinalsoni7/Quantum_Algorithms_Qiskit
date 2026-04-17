# Deutsch's Algorithm

This folder demonstrates Deutsch's algorithm for the function `f(x) = x`.

## Files

- `demo.ipynb`: Notebook version of the Deutsch's algorithm demonstration.
- `deutsch_algo.py`: Standalone Python script that builds the Deutsch circuit, runs the oracle, and simulates the result.

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
python "Deutsch’s Algorithm/deutsch_algo.py"
```

## Description

The script implements Deutsch's algorithm using a CNOT oracle for `f(x) = x`. It prepares the input and ancilla registers, applies the oracle, performs the final Hadamard transform, and measures the result. The measurement counts are printed and displayed as a histogram.