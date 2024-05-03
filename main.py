import json
import random
import string

# Function to generate random string for 'name' field
def generate_random_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Number of JSON objects to generate
num_objects = 200

# List to store JSON objects
json_objects = []

# Generate JSON objects
for _ in range(num_objects):
    obj = {
    "name": generate_random_name(),
    "hosts": [
      {
        "scheme": "match",
        "location": [
          {
            "hostname": "www.google.com"
          }
        ]
      }
    ],
    "balancer": "primary_failover",
    "tls_verify": {
      "use_sni": True,
      "allow_self_signed_certs": False,
      "sni_hint_and_strict_san_check": "www.google.com"
    },
    "override_host_header": "www.google.com"
  }
    json_objects.append(obj)

# Convert list of JSON objects to JSON string
json_string = json.dumps(json_objects, indent=4)

# Print JSON string
print(json_string)
