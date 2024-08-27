import subprocess
import os
from pathlib import Path
import pandas as pd
from datetime import datetime
import requests

def run_ansible_playbook(playbook_path, inventory_path):

    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'

    try:
        result = subprocess.run(
            ['ansible-playbook', '-i', inventory_path, playbook_path],
            capture_output=True,
            text=True,
            check=True
        )
        print("Playbook executed successfully.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the playbook.")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    return result.stdout

# Example usage
playbook_path = 'quil_query.yml'
inventory_path = 'hosts'
result = run_ansible_playbook(playbook_path, inventory_path)
print("------------")

directory = os.getcwd()
file_path = os.path.join(directory,'ansi_quil.txt')

parent_directory = Path(file_path).parent
parent_directory.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w') as file:
    file.write(result)

version = []
balance = []

with open(file_path, 'r') as file:
    for line in file:
        if "Version:" in line:
            print(line.strip())
            val = line.strip().split(":")[1].strip().split("'")[1]
            print(val)
            version.append(str(val))
        if "Unclaimed Balance:" in line:
            print(line.strip())
            bal = line.strip().split(":")[1].strip().split("'")[1].split()[0]
            print(bal)
            balance.append(float(bal))

data = { 'version' : version, 'balance' : balance }
data['date'] = datetime.now().strftime("%Y-%m-%d")
df = pd.DataFrame(data)

#get quil price
url = "https://api.cryptorank.io/v0/tickers?isTickersForPriceCalc=true&limit=1&coinKeys=quilibrium"
response = requests.get(url)
quil_price = float(response.json()['data'][0]['usdLast'])
df['quil_price'] = quil_price

print(df)

csv_path = os.path.join(directory,'data_quil.csv')
file_exists = os.path.isfile(csv_path)
df.to_csv(csv_path, index=False, mode = 'a', header = not file_exists)
