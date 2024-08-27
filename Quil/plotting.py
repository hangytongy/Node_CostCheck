import matplotlib.pyplot as plt
import pandas as pd
import os


def plot_df():
  directory = os.getcwd()
  file_path = os.path.join(directory,'data_quil.csv')
  charts_path = os.path.join(directory, 'charts')

  if os.path.exists(charts_path):
    os.makedirs(charts_path)

  df = pd.read_csv(file_path)

  if len(df) <=1 :
    return None

  else:

    df['balance'] = df['balance'].apply(lambda x : float(x))
    df['time'] = pd.to_datetime(df['date'])
  
    #get server price
    server_price = 10/(30*24*60)
  
    df['quil_earned'] = df['balance'].diff()
    df['quil_profit'] = df['quil_earned']*df['quil_price']
    df['time_delta'] = df['time'].diff().dt.total_seconds() / 60
    df['server_cost'] = server_price* df['time_delta']
  
    plt.figure(figsize=(12,6))
    plt.plot(df['time'], df['quil_earned'], linestyle='-', marker='s',color='b', label = 'quil earned')  # Line plot
    plt.plot(df['time'], df['quil_profit'], color = 'r', marker='o', label = 'quil profit')
    plt.plot(df['time'], df['server_cost'], color = 'g', label = 'server cost')
    plt.plot(df['time'], df['quil_price'], color = 'orange', label = 'quil price')
    plt.title('Quil Mining Profitability')
    plt.xlabel('Time')
    plt.ylabel('Balance')
    plt.legend(loc='best')
    plt.savefig(f'{charts_path}_Quil_Balance.png')
  
    return f"{charts_path}_Quil_Balance.png"
