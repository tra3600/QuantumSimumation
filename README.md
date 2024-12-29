# QuantumSimumation
Simulation de qubits quantiques

La simulation de qubits quantiques et le calcul de gains de temps nécessitent une compréhension de base de l'informatique quantique. Un qubit (quantum bit) est l'unité de base de l'information quantique, qui peut exister dans une superposition de 0 et 1.

Pour illustrer cela, nous allons utiliser la bibliothèque qiskit, qui est un framework open-source pour développer des programmes d'informatique quantique. Nous allons créer un exemple simple où nous créerons un qubit, appliquerons une porte Hadamard pour le mettre en superposition, et mesurerons le qubit.

Prérequis
Installer Qiskit :

pip install qiskit

Explications
Création du Circuit Quantique :

Nous créons un circuit quantique avec un seul qubit et un seul bit classique pour la mesure.
Application de la Porte Hadamard :

La porte Hadamard (qc.h(0)) met le qubit en superposition, ce qui signifie qu'il a une probabilité égale d'être mesuré en 0 ou en 1.
Mesure du Qubit :

qc.measure(0, 0) mesure l'état du qubit et stocke le résultat dans le bit classique correspondant.
Simulation du Circuit :

Nous utilisons le simulateur qasm_simulator de Qiskit pour exécuter le circuit.
transpile et assemble sont utilisés pour préparer le circuit pour la simulation.
execute exécute le circuit sur le simulateur.
Résultats de la Mesure :

result.get_counts(qc) obtient les résultats de la mesure. Les résultats montrent la distribution des mesures entre 0 et 1.
Affichage des Résultats :

plot_histogram(counts) affiche un histogramme des résultats de la mesure.
Gain de Temps
L'informatique quantique promet de résoudre certains problèmes beaucoup plus rapidement que l'informatique classique. Par exemple :

Factoring : L'algorithme de Shor pour le factoring des grands nombres entiers est exponentiellement plus rapide que les meilleurs algorithmes classiques connus.
Recherche : L'algorithme de Grover pour la recherche non structurée offre une accélération quadratique par rapport aux algorithmes classiques.
Cependant, il est important de noter que les ordinateurs quantiques actuels sont encore en phase expérimentale et ne sont pas encore capables de surpasser les ordinateurs classiques pour des tâches pratiques courantes.

Utiliser des simulateurs quantiques comme Qiskit sur des machines classiques permet de comprendre et de tester les concepts de l'informatique quantique en attendant que la technologie mûrisse.

Conclusion
Ce programme simple montre comment créer et simuler un circuit quantique en utilisant Qiskit. Vous pouvez l'étendre pour explorer des algorithmes quantiques plus complexes et comprendre comment ceux-ci peuvent offrir des gains de performance significatifs pour certains types de problèmes.
