# Phase Oracle

This folder demonstrates a phase oracle for the function `f(x) = x`.

## Files

- `demo.ipynb`: Notebook version of the phase oracle demonstration.
- `phase_oracle.py`: Standalone Python script that builds the phase oracle circuit and simulates it.

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
python "Phase Oracle/phase_oracle.py"
```

## Description

The script creates a phase oracle for `f(x) = x`, prepares the input and ancilla qubits, applies the oracle, and measures the input qubit. The simulation result is displayed and rendered as a histogram.