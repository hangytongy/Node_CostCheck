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
    df['time'] = pd.to_datetime(df['date'], unit = 's')
  
    #get server price
    server_price = 10/(30*24*60)
  
    df['quil_earned'] = df['balance'].diff()
    df['quil_profit'] = df['quil_earned']*df['quil_price']
    df['time_delta'] = df['time'].diff().dt.total_seconds() / 60
    df['server_cost'] = server_price* df['time_delta']
  
    # Generate Chart
    plt.figure(figsize=(12,6))
    fig, ax1 = plt.subplots(figsize=(12,6))

    # Primary axis
    ax1.plot(df['time'], df['quil_earned'], linestyle='-', marker='s', color='b', label='quil earned')
    ax1.plot(df['time'], df['quil_profit'], color='r', marker='o', label='quil profit')
    ax1.plot(df['time'], df['server_cost'], color='g', label='server cost')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Balance')

    # Secondary axis for quil price
    ax2 = ax1.twinx()
    ax2.plot(df['time'], df['quil_price'], color='orange', label='quil price', alpha = 0.5, linestyle = '--')
    ax2.set_ylabel('Quil Price')
    ax2.set_ylim(0.1, 0.5)


    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

    plt.title('Quil Mining Profitability')
    plt.grid()
    plt.savefig(f'{charts_path}_Quil_Balance.png')
    
    return f"{charts_path}_Quil_Balance.png"
