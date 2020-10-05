from qiskit import QuantumCircuit, execute, Aer, IBMQ
from numpy import pi
#backend = Aer.get_backend('qasm_simulator')

def which_clr():
    circuit = QuantumCircuit(2,2)
    circuit.ry(2*pi/3.0,0)
    circuit.ch(0,1)
    circuit.measure(0,0)
    circuit.measure(1,1)
    job=execute(circuit, backend, shots=1)
    res=job.result()
    for i in res.get_counts(circuit):
        if i == "00":
            return 0
        elif i == "01":
            return 1
        else:
            return 2

clrs = []
​
for i in range(40000):
    clrs += [which_clr()]
print(clrs)


