import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_FILENAME = 'results.csv'

WINDOW_SIZE = 40

S_EXACT = 0.25 * np.pi + 1.25 * np.arcsin(0.8) - 1.0

data = pd.read_csv(DATA_FILENAME)

data['Deviation_Wide'] = np.abs(data['Area_Wide'] - S_EXACT) / S_EXACT
data['Deviation_Narrow'] = np.abs(data['Area_Narrow'] - S_EXACT) / S_EXACT

data['Area_Wide_Trend'] = data['Area_Wide'].rolling(window=WINDOW_SIZE).mean()
data['Area_Narrow_Trend'] = data['Area_Narrow'].rolling(window=WINDOW_SIZE).mean()
data['Deviation_Wide_Trend'] = data['Deviation_Wide'].rolling(window=WINDOW_SIZE).mean()
data['Deviation_Narrow_Trend'] = data['Deviation_Narrow'].rolling(window=WINDOW_SIZE).mean()

# first graph

plt.figure(figsize=(12, 8))

plt.plot(data['N'], data['Area_Wide'], label='Приближение (широкая область)', alpha=0.5)
plt.plot(data['N'], data['Area_Narrow'], label='Приближение (узкая область)', alpha=0.5)

plt.plot(data['N'], data['Area_Wide_Trend'], color='blue', linestyle='--', linewidth=2, label='Тренд (широкая область)')
plt.plot(data['N'], data['Area_Narrow_Trend'], color='green', linestyle='--', linewidth=2, label='Тренд (узкая область)')

plt.axhline(y=S_EXACT, color='r', linestyle='-.', label=f'Точное значение S ≈ {S_EXACT:.4f}')

plt.title('График 1: Зависимость приближенной площади от числа точек N')
plt.xlabel('Количество точек (N)')
plt.ylabel('Вычисленная площадь (S)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()


# second graph

plt.figure(figsize=(12, 8))


plt.plot(data['N'], data['Deviation_Wide'], label='Отклонение (широкая область)', alpha=0.5)
plt.plot(data['N'], data['Deviation_Narrow'], label='Отклонение (узкая область)', alpha=0.5)

plt.plot(data['N'], data['Deviation_Wide_Trend'], color='blue', linestyle='--', linewidth=2, label='Тренд отклонения (широкая)')
plt.plot(data['N'], data['Deviation_Narrow_Trend'], color='green', linestyle='--', linewidth=2, label='Тренд отклонения (узкая)')

plt.yscale('log')

plt.title('График 2: Зависимость относительного отклонения от числа точек N')
plt.xlabel('Количество точек (N)')
plt.ylabel('Относительное отклонение (логарифмическая шкала)')
plt.grid(True, which="both", ls="-")
plt.legend()
plt.tight_layout()

plt.show()