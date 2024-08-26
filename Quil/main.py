import subprocess
import os

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

# Example usage
playbook_path = 'quil_query.yml'
inventory_path = 'hosts'
run_ansible_playbook(playbook_path, inventory_path)
