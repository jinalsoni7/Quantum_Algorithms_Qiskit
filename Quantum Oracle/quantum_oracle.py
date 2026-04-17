"""
Quantum Oracle Implementation

This script implements a quantum oracle for the function f(x) = ~x.
The quantum oracle Uf acts as |x> |y> --> |x> |y ⊕ f(x)>.

Author: Jinal Soni
Date: March 2, 2026
"""

import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram


def create_oracle():
    """
    Create the quantum oracle circuit for f(x) = ~x.

    Returns:
        QuantumCircuit: The oracle circuit.
    """
    qc = QuantumCircuit(2, name='Q_Oracle')
    qc.x(1)
    qc.cx(1, 0)
    qc.x(1)
    return qc


def build_full_circuit():
    """
    Build the full quantum circuit with Hadamard gates and oracle.

    Returns:
        QuantumCircuit: The complete circuit.
    """
    oracle = create_oracle().to_gate()
    oracle.name = "Oracle"

    qc_1 = QuantumCircuit(2)
    qc_1.h([0, 1])
    qc_1.append(oracle, [0, 1])
    qc_1.measure_active()
    return qc_1


def simulate_and_plot(qc, shots=1000):
    """
    Simulate the quantum circuit and plot the results.

    Args:
        qc (QuantumCircuit): The circuit to simulate.
        shots (int): Number of shots for simulation.
    """
    # Create simulator
    simulator = AerSimulator()

    # Transpile for the simulator backend (optional but recommended)
    qc_compiled = transpile(qc, simulator)

    # Run the job
    job = simulator.run(qc_compiled, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # Print and plot
    print("Simulation Results for qc_1:")
    print(counts)

    # Display histogram (in script, this will show if in interactive environment)
    plot_histogram(counts)


def main():
    """
    Main function to run the quantum oracle simulation.
    """
    # Build the circuit
    qc_1 = build_full_circuit()

    # Draw the circuit (optional, for visualization)
    print("Circuit Diagram:")
    print(qc_1.draw())

    # Simulate and plot
    simulate_and_plot(qc_1)


if __name__ == "__main__":
    main()