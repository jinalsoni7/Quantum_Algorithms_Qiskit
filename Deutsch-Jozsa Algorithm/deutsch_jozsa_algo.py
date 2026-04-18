"""
Deutsch-Jozsa Algorithm Implementation

This script implements the Deutsch-Jozsa algorithm for a balanced function f(x) = x.
It uses 3 input qubits and 1 ancilla qubit, with a CNOT-based oracle.

Author: Jinal Soni
Date: March 7, 2026
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def create_oracle():
    """
    Create the Deutsch-Jozsa oracle for f(x) = x.

    Returns:
        Gate: The oracle gate.
    """
    oracle = QuantumCircuit(4, name='U_f')
    oracle.cx(0, 3)
    return oracle.to_gate(label='U_f')


def build_circuit():
    """
    Build the Deutsch-Jozsa algorithm circuit.

    Returns:
        QuantumCircuit: The full circuit with measurements.
    """
    qc = QuantumCircuit(4, 3)
    qc.h([0, 1, 2])  # Put input qubits in superposition
    qc.x(3)  # Prepare ancilla in |1>
    qc.h(3)  # Put ancilla in superposition
    qc.append(create_oracle(), [0, 1, 2, 3])  # Apply oracle
    qc.h([0, 1, 2])  # Convert phase into amplitude on input qubits
    qc.measure([0, 1, 2], [0, 1, 2])  # Measure input qubits
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
    Run the Deutsch-Jozsa algorithm demonstration.
    """
    qc = build_circuit()
    print('Circuit diagram:')
    print(qc.draw())

    counts = simulate_circuit(qc)
    print('Simulation counts for qc (Deutsch-Jozsa algorithm, f(x)=x):', counts)
    plot_histogram(counts)


if __name__ == '__main__':
    main()