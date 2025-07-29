import json
DATA_FILE = "data.json"
EXPECTED_IP_PREFIX = "198"
 # Open and load the JSON data
 # This will crash if:
 # - data.json does not exist
 # - data.json is not valid JSON
 # - 'ip' key is missing or its value is not a string
with open(DATA_FILE, 'r') as f:
  data = json.load(f)

  
 #After data = json.load(f) executes, the data variable in your Python script will hold a Python dictionary 
 
ip_address = data['ip'] # This will crash if 'ip' key is missing,This will fetch key ip from a dict and get its value
 
 # Check if the IP address starts with the expected prefix
 # This will crash if ip_address is not a string (e.g., if it's a number)
if ip_address.startswith(EXPECTED_IP_PREFIX):
    print(f"Success: The IP address '{ip_address}' starts with '{EXPECTED_IP_PREFIX}'.")
else:
    print(f"Validation Failed: The IP address '{ip_address}' in '{DATA_FILE}' does NOT start with '{EXPECTED_IP_PREFIX}'.")
