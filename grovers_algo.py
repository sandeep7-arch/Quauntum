from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(3, 3)
//creating superpostion
qc.h([0, 1, 2])
//disguising the target
qc.x(1)

//oracle
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
//removing the disguise
qc.x(1)



//amplitude amplification , flip of states around the average making //the target states probabilty high
qc.h([0, 1, 2])
qc.x([0, 1, 2])

qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)

qc.x([0, 1, 2])
qc.h([0, 1, 2])

qc.measure([0, 1, 2], [0, 1, 2])

simulator = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()

counts = result.get_counts()

print("Measurement Results:")
for state, count in counts.items():
    print(f"{state}: {count}")
