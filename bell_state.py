#bells state
from qiskit import QuantumCircuit
from qiskit_aer import Aer
qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts(qc)

print(qc.draw())

print("ACTUAL RESULTS:", counts)
