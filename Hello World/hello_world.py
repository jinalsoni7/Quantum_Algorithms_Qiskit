"""
Hello World Quantum Circuit Script

This script demonstrates a basic quantum circuit simulation using Qiskit.
It creates a Bell state, defines various Pauli observables, computes expectation values,
and plots the results.

Author: Jinal Soni
Date: March 1, 2026
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli
from qiskit_aer.primitives import Estimator
import matplotlib.pyplot as plt


def create_bell_state():
    """
    Create a Bell state quantum circuit.

    Returns:
        QuantumCircuit: A 2-qubit Bell state circuit.
    """
    qc = QuantumCircuit(2)
    qc.h(0)  # Apply Hadamard gate to first qubit
    qc.cx(0, 1)  # Apply CNOT gate with control on qubit 0 and target on qubit 1
    return qc


def define_observables():
    """
    Define the Pauli observables for measurement.

    Returns:
        list: List of Pauli operators.
    """
    observables = [
        Pauli("ZZ"),  # Z tensor Z
        Pauli("ZI"),  # Z tensor I
        Pauli("IZ"),  # I tensor Z
        Pauli("XX"),  # X tensor X
        Pauli("XI"),  # X tensor I
        Pauli("IX"),  # I tensor X
    ]
    return observables


def run_estimator(qc, observables):
    """
    Run the estimator to compute expectation values.

    Args:
        qc (QuantumCircuit): The quantum circuit.
        observables (list): List of observables.

    Returns:
        list: Expectation values for each observable.
    """
    estimator = Estimator()
    job = estimator.run([qc] * len(observables), observables)
    return job.result().values


def plot_results(data_labels, values):
    """
    Plot the expectation values.

    Args:
        data_labels (list): Labels for the x-axis.
        values (list): Expectation values.
    """
    plt.plot(data_labels, values, '-o')
    plt.xlabel('Observables')
    plt.ylabel('Expectation Values')
    plt.title('Expectation Values of Observables')
    plt.show()


def main():
    """
    Main function to execute the quantum simulation.
    """
    # Create the quantum circuit
    qc = create_bell_state()

    # Define observables
    observables = define_observables()

    # Run estimator
    values = run_estimator(qc, observables)

    # Prepare data labels
    data_labels = ['ZZ', 'ZI', 'IZ', 'XX', 'XI', 'IX']

    # Plot results
    plot_results(data_labels, values)


if __name__ == "__main__":
    main()