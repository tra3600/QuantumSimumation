from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Créer un circuit quantique avec un qubit et un bit classique pour la mesure
qc = QuantumCircuit(1, 1)

# Appliquer la porte Hadamard pour mettre le qubit en superposition
qc.h(0)

# Mesurer le qubit
qc.measure(0, 0)

# Simuler le circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = execute(qc, backend=simulator).result()

# Obtenir les résultats de la mesure
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)

# Afficher l'histogramme des résultats
plot_histogram(counts)
plt.show()