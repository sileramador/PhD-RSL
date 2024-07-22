import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Definir las referencias y contextos para OB2
references_ob2 = [
    'A74', 'A71', 'A28', 'A72', 'A25', 'A16', 'A17', 'A18', 'A19', 'A22', 'A23', 'A24', 'A34',
    'A49', 'A55', 'A56', 'A57', 'A58', 'A50', 'A53', 'A54',
    'A13', 'A59', 'A60',
    'A51', 'A52'
]

contexts_ob2 = [
    ['A74', 'A71', 'A28', 'A72', 'A25', 'A16', 'A17', 'A18', 'A19', 'A22', 'A23', 'A24', 'A34'],
    ['A49', 'A55', 'A56', 'A57', 'A58', 'A50', 'A53', 'A54'],
    ['A13', 'A54', 'A55', 'A56', 'A57', 'A58', 'A59', 'A60'],
    ['A55', 'A56'],
    ['A49', 'A55', 'A56', 'A57', 'A58', 'A50', 'A53', 'A54'],
    ['A49', 'A50', 'A51', 'A52', 'A53', 'A57'],
    ['A55', 'A56'],
    ['A49', 'A50', 'A53', 'A57']
]

# Ordenar las referencias
references_ob2_sorted = sorted(references_ob2)

# Ordenar los contextos
contexts_ob2_sorted = [sorted(context) for context in contexts_ob2]

# Imprimir referencias ordenadas
print("Referencias ordenadas:")
print(references_ob2_sorted)

# Imprimir contextos ordenados
print("\nContextos ordenados:")
for i, context in enumerate(contexts_ob2_sorted):
    print(f"Contexto{i+1}: {context}")

# Crear un DataFrame de presencia/ausencia para las referencias ordenadas
df_ob2_sorted = pd.DataFrame(0, index=references_ob2_sorted, columns=[f'Contexto{i+1}' for i in range(len(contexts_ob2_sorted))])
for i, context in enumerate(contexts_ob2_sorted):
    for ref in context:
        df_ob2_sorted.loc[ref, f'Contexto{i+1}'] = 1

# Calcular la matriz de correlación
corr_matrix_ob2_sorted = df_ob2_sorted.corr()

# Generar el mapa de calor
plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix_ob2_sorted, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones entre Contextos - OB2')
plt.show()