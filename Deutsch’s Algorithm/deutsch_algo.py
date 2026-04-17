"""
Deutsch's Algorithm Implementation

This script implements Deutsch's algorithm for the balanced function f(x) = x.
It constructs the oracle, prepares the input and ancilla qubits,
applies the oracle, and simulates the circuit.

Author: Jinal Soni
Date: March 3, 2026
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def create_oracle():
    """
    Create the Deutsch oracle for f(x) = x.

    Returns:
        Gate: The oracle gate.
    """
    oracle = QuantumCircuit(2, name='U_f')
    oracle.cx(0, 1)
    return oracle.to_gate(label='U_f')


def build_circuit():
    """
    Build the Deutsch's algorithm circuit.

    Returns:
        QuantumCircuit: The full circuit with measurement.
    """
    qc = QuantumCircuit(2, 1)
    qc.h(0)  # Put input qubit in superposition
    qc.x(1)  # Prepare ancilla in |1>
    qc.h(1)  # Put ancilla in superposition
    qc.append(create_oracle(), [0, 1])
    qc.h(0)  # Convert phase into amplitude on input qubit
    qc.measure(0, 0)
    return qc


def simulate_circuit(qc, shots=1000):
    """
    Simulate the given circuit and return measurement counts.

    Args:
        qc (QuantumCircuit): The circuit to simulate.
        shots (int): Number of measurement shots.

    Returns:
        dict: The measurement counts.
    """
    simulator = AerSimulator()
    qc_compiled = transpile(qc, simulator)
    job = simulator.run(qc_compiled, shots=shots)
    result = job.result()
    return result.get_counts()


def main():
    """
    Run the Deutsch algorithm demonstration.
    """
    qc = build_circuit()
    print('Circuit diagram:')
    print(qc.draw())

    counts = simulate_circuit(qc)
    print('Simulation counts for qc (Deutsch algorithm, f(x)=x):', counts)
    plot_histogram(counts)


if __name__ == '__main__':
    main()
