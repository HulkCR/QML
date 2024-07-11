import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Definir los datos de ejemplo
data = np.array([
    [0.1, 0.2],
    [0.5, 0.4],
    [0.4, 0.6],
    [0.9, 0.8],
    [0.3, 0.1],
    [0.7, 0.3],
    [0.2, 0.7],
    [0.6, 0.5]
])

# Crear un circuito cuántico
num_qubits = 2
qc = QuantumCircuit(num_qubits, num_qubits)

# Aplicar puertas cuánticas para representar los datos
for point in data:
    qc.ry(point[0], 0)
    qc.ry(point[1], 1)
    qc.cx(0, 1)
    qc.barrier()

# Medir los qubits para obtener la distancia cuántica
qc.measure(range(num_qubits), range(num_qubits))

# Definir el backend para simulación
backend = Aer.get_backend('qasm_simulator')

# Compilar y ejecutar el circuito en el backend
job = execute(qc, backend)
result = job.result()

# Obtener los resultados de las mediciones
counts = result.get_counts(qc)

# Mostrar los resultados de las mediciones
print("Resultados de las mediciones:")
print(counts)
