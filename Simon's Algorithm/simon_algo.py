"""
Simon's Algorithm Implementation

This script implements Simon's algorithm to find the hidden period of a 2-to-1 function.
It uses 2 input qubits and 2 output qubits, with a randomly chosen secret string s.

Author: Jinal Soni
Date: March 9, 2026
"""

import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def mcx_safe(qc, controls, target):
    """
    Helper function to apply multi-controlled X gate safely.

    Args:
        qc (QuantumCircuit): The quantum circuit.
        controls (list): List of control qubits.
        target (int): Target qubit.
    """
    try:
        qc.mcx(controls, target)
    except Exception:
        # Some Qiskit versions use 'mct'
        qc.mct(controls, target)


def create_oracle(n, s, mapping):
    """
    Create the Simon oracle for the given mapping.

    Args:
        n (int): Number of input bits.
        s (int): Secret string.
        mapping (dict): Mapping from x to f(x).

    Returns:
        QuantumCircuit: The oracle circuit.
    """
    num_qubits = n + n  # input + output
    oracle = QuantumCircuit(num_qubits, name='SimonOracle')

    # For each input x, set the output register to mapping[x]
    for x in range(2**n):
        y = mapping[x]
        y_bits = [(y >> i) & 1 for i in range(n)]  # LSB first
        controls = list(range(n))  # input qubits 0..n-1

        for i, bit in enumerate(y_bits):
            if bit == 0:
                continue

            # Flip input bits where x_j == 0
            flip_positions = [j for j in range(n) if ((x >> j) & 1) == 0]
            for j in flip_positions:
                oracle.x(j)

            # Apply MCX
            mcx_safe(oracle, controls, n + i)

            # Undo flips
            for j in flip_positions:
                oracle.x(j)

    return oracle


def build_mapping(n, s):
    """
    Build the 2-to-1 mapping for Simon's function.

    Args:
        n (int): Number of input bits.
        s (int): Secret string.

    Returns:
        dict: Mapping from x to f(x).
    """
    mapping = {}
    next_label = 0
    for x in range(2**n):
        if x in mapping:
            continue
        y = next_label
        mapping[x] = y
        mapping[x ^ s] = y
        next_label += 1
    return mapping


def build_circuit(n, oracle):
    """
    Build the Simon's algorithm circuit.

    Args:
        n (int): Number of input bits.
        oracle (QuantumCircuit): The oracle circuit.

    Returns:
        QuantumCircuit: The full circuit.
    """
    num_qubits = n + n
    qc = QuantumCircuit(num_qubits, n)  # Measure only input register

    # Prepare input in superposition
    qc.h(range(n))

    # Apply oracle
    qc.append(oracle.to_gate(label='U_f'), list(range(num_qubits)))

    # Apply H again to input qubits
    qc.h(range(n))

    # Measure input qubits
    qc.measure(range(n), list(range(n)))

    return qc


def simulate_and_get_samples(qc, n, shots=None):
    """
    Simulate the circuit and get measurement samples.

    Args:
        qc (QuantumCircuit): The circuit to simulate.
        n (int): Number of input bits.
        shots (int): Number of shots (default n).

    Returns:
        list: List of measured bitstrings.
    """
    if shots is None:
        shots = n
    simulator = AerSimulator()
    qc_compiled = transpile(qc, simulator)
    job = simulator.run(qc_compiled, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # Expand counts into individual samples
    samples = []
    for bitstr, c in counts.items():
        for _ in range(c):
            samples.append(bitstr)
    return samples


def bitstr_to_int(bitstr):
    """
    Convert bitstring to integer (LSB is bit 0).

    Args:
        bitstr (str): Bitstring from Qiskit.

    Returns:
        int: Integer value.
    """
    return int(bitstr[::-1], 2)


def solve_for_s(n, z_values):
    """
    Solve for the secret s from the measured z values.

    Args:
        n (int): Number of input bits.
        z_values (list): List of z values.

    Returns:
        list: List of candidate s values.
    """
    candidates = []
    for cand in range(1, 2**n):
        ok = True
        for z in z_values:
            dot = bin(z & cand).count('1') % 2
            if dot != 0:
                ok = False
                break
        if ok:
            candidates.append(cand)
    return candidates


def main():
    """
    Run Simon's algorithm demonstration.
    """
    n = 2  # Number of input bits

    # Choose random secret s
    s = random.choice([i for i in range(1, 2**n)])
    print(f"Secret s (binary): {s:0{n}b}")

    # Build mapping
    mapping = build_mapping(n, s)
    print('Mapping:', mapping)

    # Create oracle
    oracle = create_oracle(n, s, mapping)

    # Build circuit
    qc = build_circuit(n, oracle)
    print('Circuit diagram:')
    print(qc.draw())

    # Simulate and get samples
    samples = simulate_and_get_samples(qc, n)
    print('Measured z strings:', samples)

    # Convert to integers
    z_values = [bitstr_to_int(b) for b in samples]
    print('z values (as integers):', z_values)

    # Solve for s
    candidates = solve_for_s(n, z_values)
    print('Candidates for s (binary):', [f"{c:0{n}b}" for c in candidates])

    if len(candidates) == 1:
        found_s = candidates[0]
        print(f"Recovered s: {found_s:0{n}b}")
    else:
        print('Could not uniquely determine s; need more samples.')
        if candidates:
            print('Possible s values:', [f"{c:0{n}b}" for c in candidates])

    print('Actual secret s:', f"{s:0{n}b}")


if __name__ == '__main__':
    main()