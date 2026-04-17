"""
Phase Oracle Implementation

This script implements a phase oracle for the function f(x) = x.
The oracle acts on the state |x>|-> and applies a phase of (-1)^{f(x)} to the input.

Author: Jinal Soni
Date: March 2, 2026
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def create_phase_oracle():
    """
    Create the phase oracle gate for f(x) = x.

    Returns:
        Gate: The phase oracle as a quantum gate.
    """
    oracle = QuantumCircuit(2, name='U_f')
    oracle.cx(0, 1)
    return oracle.to_gate(label='U_f')


def build_circuit():
    """
    Build the full quantum circuit for the phase oracle demonstration.

    Returns:
        QuantumCircuit: The complete circuit with an input qubit and ancilla.
    """
    qc = QuantumCircuit(2, 1)

    # Prepare input qubit in superposition
    qc.h(0)

    # Prepare ancilla in |-> state
    qc.x(1)
    qc.h(1)

    # Apply the phase oracle
    qc.append(create_phase_oracle(), [0, 1])

    # Measure the input qubit
    qc.measure(0, 0)
    return qc


def simulate_circuit(qc, shots=1000):
    """
    Simulate the circuit using AerSimulator and return the measurement counts.

    Args:
        qc (QuantumCircuit): The circuit to simulate.
        shots (int): Number of shots for the simulation.

    Returns:
        dict: Measurement counts.
    """
    simulator = AerSimulator()
    qc_compiled = transpile(qc, simulator)
    job = simulator.run(qc_compiled, shots=shots)
    result = job.result()
    return result.get_counts()


def main():
    """
    Main entry point for the phase oracle demonstration.
    """
    qc = build_circuit()

    print('Circuit diagram:')
    print(qc.draw())

    counts = simulate_circuit(qc)
    print('Simulation counts for qc (phase oracle f(x)=x):', counts)

    plot_histogram(counts)


if __name__ == '__main__':
    main()
