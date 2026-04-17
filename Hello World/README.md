# Hello World

This folder contains a simple Qiskit demonstration of a 2-qubit Bell state and expectation value estimation.

## Files

- `demo.ipynb`: Notebook version of the Hello World demonstration.
- `hello_world.py`: Standalone Python script that creates a Bell state, evaluates several Pauli observables, and plots the expectation values.

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
python "Hello World/hello_world.py"
```

## Description

The script creates a Bell pair, defines a set of Pauli observables, computes their expectation values using Qiskit `Estimator`, and plots the results.