# Carrega Bibliotecas
import pandas as pd

# Carregamento do arquivo de dados
df = pd.read_excel("input/Taco.xlsx")

# Eliminar colunas não usadas
df = df[['Grupo', 'Descrição do Alimento', 'Umidade(%)',
         'Energia(kcal)', 'Energia(kJ)', 'Proteína(g)', 'Lipídeos(g)',
         'Colesterol(mg)', 'Carboidrato(g)', 'Fibra Alimentar(g)', 'Cinzas(g)',
         'Cálcio(mg)', 'Magnésio(mg)', 'Manganês(mg)', 'Fósforo(mg)',
         'Ferro(mg)', 'Sódio(mg)', 'Potássio(mg)', 'Cobre(mg)', 'Zinco(mg)', 'VitaminaC(mg)']]

df.to_excel('output/dados-tratados.xlsx', index=False)
