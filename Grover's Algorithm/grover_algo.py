"""
Grover's Algorithm Implementation

This script implements Grover's search algorithm for a fixed target state on 5 qubits.
It builds the oracle, reflection operators, and full Grover circuit, then simulates the result.

Date: March 13, 2026
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import MCMT
import matplotlib.pyplot as plt


def build_oracle(n, target_state, ancilla):
    """
    Build the Grover oracle Uf for a fixed marked state.

    Args:
        n (int): Number of search qubits.
        target_state (str): Bitstring of the marked state.
        ancilla (int): Ancilla qubit index.

    Returns:
        QuantumCircuit: Oracle circuit.
    """
    oracle = QuantumCircuit(n + 1, name='Uf')
    for i, bit in enumerate(target_state):
        if bit == '0':
            oracle.x(i)

    oracle.mcx(list(range(n)), ancilla)

    for i, bit in enumerate(target_state):
        if bit == '0':
            oracle.x(i)

    return oracle


def build_R0(n):
    """
    Build the reflection about |0^n> on the search register.

    Args:
        n (int): Number of search qubits.

    Returns:
        Gate: R0 gate.
    """
    R0 = QuantumCircuit(n, name='R0')
    R0.x(range(n))

    mcz_gate = MCMT('cz', n - 1, 1)
    R0.append(mcz_gate, list(range(n - 1)) + [n - 1])

    R0.z(0)
    R0.x(0)
    R0.z(0)
    R0.x(range(1, n))

    return R0.decompose().to_gate(label='R0')


def build_Rs(n, R0_gate):
    """
    Build the diffusion operator Rs = H R0 H.

    Args:
        n (int): Number of search qubits.
        R0_gate (Gate): R0 gate.

    Returns:
        Gate: Rs gate.
    """
    Rs = QuantumCircuit(n, name='Rs')
    Rs.h(range(n))
    Rs.append(R0_gate, range(n))
    Rs.h(range(n))
    return Rs.to_gate(label='Rs')


def build_grover_circuit(n, target_state):
    """
    Build the full Grover circuit.

    Args:
        n (int): Number of search qubits.
        target_state (str): Marked state bitstring.

    Returns:
        QuantumCircuit: The complete Grover circuit.
    """
    ancilla = n
    qc = QuantumCircuit(n + 1, n)

    qc.h(range(n))
    qc.x(ancilla)
    qc.h(ancilla)

    oracle = build_oracle(n, target_state, ancilla)
    R0_gate = build_R0(n)
    Rs_gate = build_Rs(n, R0_gate)

    iterations = int((2**n)**0.5)
    for _ in range(iterations):
        qc.append(oracle.to_gate(label='Uf'), list(range(n + 1)))
        qc.append(Rs_gate, range(n))

    qc.measure(range(n), range(n))
    return qc


def simulate_circuit(qc, shots=1000):
    """
    Simulate the quantum circuit and return measurement counts.

    Args:
        qc (QuantumCircuit): Circuit to simulate.
        shots (int): Number of shots.

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
    Run the Grover algorithm demonstration.
    """
    n = 5
    target_state = '10110'

    print(f"Marked item |w> = |{target_state}>")

    qc = build_grover_circuit(n, target_state)
    print('Grover circuit:')
    print(qc.draw())

    counts = simulate_circuit(qc)
    print('Measurement counts:')
    print(counts)

    plot_histogram(counts)
    plt.show()

    most_common = max(counts, key=counts.get)
    most_common_reversed = most_common[::-1]
    print(f"Most common measurement result: |{most_common_reversed}>")
    print(f"Marked state |w> = |{target_state}>")
    if most_common_reversed == target_state:
        print('Success! The most common result is the marked state |w>.')
    else:
        print('The most common result is NOT the marked state |w>.')


if __name__ == '__main__':
    main()
