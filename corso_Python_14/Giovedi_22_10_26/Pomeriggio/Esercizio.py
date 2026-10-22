import pandas as pd
import matplotlib.pyplot as plt

temperature = {
    'temperature': [ 18.5, 19.2, 20.1, 17.8, 21.3, 22.0, 19.7, 18.9, 23.1, 24.0, 22.5, 21.8, 20.4, 19.5, 25.2, 26.1, 24.8, 23.6, 22.9, 21.5,20.7, 19.8, 18.2, 17.5, 21.0, 23.4, 24.2, 22.7, 20.9, 19.3,10]
}

df_temperature = pd.DataFrame(temperature)

print(df_temperature)

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
y=df_temperature['temperature']




plt.figure()
max_temp = df_temperature["temperature"].max()
giorno_max = df_temperature["temperature"].idxmax()
plt.annotate(f"Massima: {max_temp}°C", (giorno_max + 1, max_temp))

min_temp = df_temperature["temperature"].min()
giorno_min = df_temperature["temperature"].idxmin()
plt.annotate(f"Minima: {min_temp}°C", (giorno_min + 1, min_temp))

mean_temp = df_temperature["temperature"].mean()
plt.annotate(f"Media: {mean_temp}°C", (10, mean_temp))
print("Temperatura media ", mean_temp , " °C")

median_temp = df_temperature["temperature"].median()
plt.annotate(f"Mediana: {median_temp}°C", (15, median_temp))
print("Mediana ", median_temp, " °C")

plt.title('Grafico a Scatter delle temperature di ottobre a Genova')
plt.scatter(x,y)
plt.show()