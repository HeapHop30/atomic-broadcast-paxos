from utils import *
import sys

config = import_config(CONFIG_FILE)
network = create_network(config)
try:
    p_id = sys.argv[1]
except IndexError as error:
    print("You have to specify the process id as argument.")

while True:
    v = input()
    print(f"Submitted value: {v}")
