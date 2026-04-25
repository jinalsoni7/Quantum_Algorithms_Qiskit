# Grover's Algorithm

This folder demonstrates Grover's algorithm for unstructured search on a 5-qubit search register.

## Files

- `demo.ipynb`: Notebook version of the Grover algorithm demonstration.
- `grover_algo.py`: Standalone Python script that builds the oracle, diffusion operators, and full Grover circuit, then simulates the search.

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
python "grover_algo.py"
```

## Description

The script implements Grover's search algorithm for a fixed marked state `|10110>`. It constructs the oracle `Uf`, the reflection about the all-zero state `R0`, and the diffusion operator `Rs`, then applies the Grover iteration approximately `sqrt(N)` times. The result is simulated and displayed as measurement counts and a histogram.