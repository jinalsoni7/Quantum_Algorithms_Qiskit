"""
Bernstein-Vazirani Algorithm Implementation

This script implements the Bernstein-Vazirani algorithm to find a hidden bit string.
It uses 6 input qubits and 1 ancilla qubit, with an oracle that encodes the secret string '101001'.

Author: Jinal Soni
Date: March 7, 2026
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def create_oracle():
    """
    Create the Bernstein-Vazirani oracle for the secret string '101001'.

    Returns:
        Gate: The oracle gate.
    """
    oracle = QuantumCircuit(7, name='U_f')
    oracle.cx(0, 6)  # Bit 0 of secret string
    oracle.cx(3, 6)  # Bit 3
    oracle.cx(5, 6)  # Bit 5
    return oracle.to_gate(label='U_f')


def build_circuit():
    """
    Build the Bernstein-Vazirani algorithm circuit.

    Returns:
        QuantumCircuit: The full circuit with measurements.
    """
    qc = QuantumCircuit(7, 6)
    qc.h([0, 1, 2, 3, 4, 5])  # Put input qubits in superposition
    qc.x(6)  # Prepare ancilla in |1>
    qc.h(6)  # Put ancilla in superposition
    qc.append(create_oracle(), [0, 1, 2, 3, 4, 5, 6])  # Apply oracle
    qc.h([0, 1, 2, 3, 4, 5])  # Convert phase into amplitude on input qubits
    qc.measure([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5])  # Measure input qubits
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
    Run the Bernstein-Vazirani algorithm demonstration.
    """
    qc = build_circuit()
    print('Circuit diagram:')
    print(qc.draw())

    counts = simulate_circuit(qc)
    print('Simulation counts for qc (Bernstein-Vazirani algorithm, secret=101001):', counts)
    plot_histogram(counts)


if __name__ == '__main__':
    main()