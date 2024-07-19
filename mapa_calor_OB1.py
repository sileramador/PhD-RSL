import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Definir las referencias y contextos para OB1
references_ob1 = [
    'A74', 'A25', 'A12', 'A02', 'A06', 'A68', 'A24', 'A35', 'A36', 'A37', 'A38', 'A72', 'A62', 'A21', 
    'A65', 'A10', 'A34', 'A11', 'A48', 'A49', 'A60', 'A71', 'A28', 'A23', 'A66', 'A01', 'A07', 'A09', 
    'A03', 'A05', 'A41', 'A40', 'A42', 'A43', 'A44', 'A46', 'A47', 'A50', 'A52', 'A53', 'A54', 'A55', 
    'A56', 'A57', 'A58', 'A59', 'A60'
]

# Definir los contextos con sus respectivas referencias
contexts_ob1 = [
    ['A74', 'A25', 'A12', 'A02', 'A06', 'A68', 'A24', 'A35', 'A36', 'A37', 'A38'],                 # Contexto 1
    ['A74', 'A72', 'A25', 'A62', 'A21', 'A65', 'A02', 'A10', 'A34', 'A12', 'A11', 'A48', 'A49', 'A60'], # Contexto 2
    ['A74', 'A71', 'A72', 'A25', 'A28', 'A62', 'A23', 'A66', 'A68', 'A02', 'A06', 'A34', 'A12', 'A35', 'A36', 'A37', 'A38', 'A01', 'A10', 'A07', 'A09', 'A03', 'A05', 'A11', 'A40', 'A41', 'A42', 'A43', 'A44', 'A46', 'A47', 'A48', 'A49', 'A50', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57', 'A58', 'A59', 'A60'], # Contexto 3
    ['A25', 'A72', 'A74'],                                                                              # Contexto 4
    ['A74', 'A72', 'A25', 'A62', 'A21', 'A65', 'A02', 'A10', 'A34', 'A12', 'A11', 'A48', 'A49', 'A60'], # Contexto 5
    ['A02', 'A10', 'A34', 'A12'],                                                                       # Contexto 6
    ['A74', 'A71', 'A72', 'A25', 'A28', 'A62', 'A23', 'A66', 'A68', 'A02', 'A06', 'A34', 'A12', 'A35', 'A36', 'A37', 'A38', 'A01', 'A10', 'A07', 'A09', 'A03', 'A05', 'A11', 'A40', 'A41', 'A42', 'A43', 'A44', 'A46', 'A47', 'A48', 'A49', 'A50', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57', 'A58', 'A59', 'A60']  # Contexto 7
]

# Ordenar las referencias alfabéticamente
references_ob1_sorted = sorted(references_ob1)

# Ordenar los contextos internamente
contexts_ob1_sorted = [sorted(context) for context in contexts_ob1]

# Crear un DataFrame de presencia/ausencia para las referencias ordenadas
df_ob1_sorted = pd.DataFrame(0, index=references_ob1_sorted, columns=[f'Context_{i+1}' for i in range(len(contexts_ob1_sorted))])

# Llenar el DataFrame con 1's donde las referencias están presentes en los contextos
for i, context in enumerate(contexts_ob1_sorted):
    for ref in context:
        df_ob1_sorted.loc[ref, f'Context_{i+1}'] = 1

# Verificar el DataFrame de presencia/ausencia
print("DataFrame de presencia/ausencia:")
print(df_ob1_sorted)

# Calcular la matriz de correlación
corr_matrix_ob1_sorted = df_ob1_sorted.corr()

# Verificar la matriz de correlación antes de generar el mapa de calor
print("Matriz de correlación:")
print(corr_matrix_ob1_sorted)

# Generar el mapa de calor
plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix_ob1_sorted, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones entre Contextos - OB1')
plt.show()

# Mostrar la matriz de correlación
print(corr_matrix_ob1_sorted)
