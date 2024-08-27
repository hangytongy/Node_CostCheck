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

#get server price
server_price = 12.5/30

df['quil_earned'] = df['balance'].diff()
df['quil_profit'] = df['quil_earned']*df['quil_price']
df['server_cost'] = server_price

plt.figure(figsize=(12,6))
plt.plot(df['time'], df['quil_earned'], marker='o', linestyle='-', color='b', label = 'quil earned')  # Line plot
plt.plot(df['time'], df['quil_profit'], color = 'r', label = 'quil profit')
plt.plot(df['time'], df['server_cost'], color = 'g', label = 'server cost / day')
plt.title('Quil Mining Profitability')
plt.xlabel('Time')
plt.ylabel('Balance')
plt.legend(loc='best')
plt.savefig(f'{charts_path}_Quil_Balance.png')
