# Shor's Algorithm

This folder demonstrates Shor's algorithm for integer factorization.

## Files

- `demo.ipynb`: Notebook version of Shor's algorithm demonstration.
- `shor_algo.py`: Standalone Python script that implements the classical part of Shor's algorithm, using sympy for order finding.

## Requirements

- Python 3.8+
- `sympy`

Install required packages with:

```bash
pip install sympy
```

## Running

```bash
python "shor_algo.py"
```

## Description

The script demonstrates Shor's factoring algorithm for N=15. It randomly selects a base a, computes GCD(a, N), and if coprime, finds the order r classically using sympy. If r is even, it computes potential factors using the order. Note: This is a classical demonstration; full quantum order finding is not implemented.