import matplotlib.pyplot as plt
import pandas as pd
import os

directory = os.getcwd()
file_path = os.path.join(directory,'data_quil.csv')
charts_path = os.path.join(directory, 'charts')

if os.path.exists(charts_path):
  os.makedirs(charts_path)

df = pd.read_csv(file_path)

df['balance'] = df['balance].apply(lambda x : float(x)
df['time] = pd.to_datetime(df['date'])

plt.figure(figsize=(12,6))
plt.plot(df['time'], df['balance'], marker='o', linestyle='-', color='b')  # Line plot
plt.title('Quil Balance')
plt.xlabel('Time')
plt.ylabel('Balance')

plt.savefig(f'{charts_path}_Quil_Balance.png')
