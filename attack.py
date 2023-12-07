import subprocess

# Define the cURL command as a list of strings
curl_command = [
    "curl",
    "--location",
    "http://127.0.0.1:5000/login",
    "--header",
    'Cookie: session=eyJfZnJlc2giOmZhbHNlLCJwaG9uZSI6IisyMjE3NzI1NzA0MTQiLCJ1c2VybmFtZSI6Im1hZCJ9.ZWXdDA.wBXF_aqEPF1V2K0OdcqpFM-cYWA',
    "--form",
    'username="mad"',
    "--form",
    'password="passer"',
    "--form",
    'submit="Connexion"'
]

# Define the number of iterations for the loop
num_iterations = 3

# Execute the cURL command within a for loop
for _ in range(num_iterations):
    try:
        result = subprocess.run(curl_command, check=True, capture_output=True, text=True)
        # Print the response for each iteration
        #print("Response:")
        #print(result.stdout)
    except subprocess.CalledProcessError as e:
        # If the cURL command fails, print the error for each iteration
        print("Error:", e)
        print("Error Output:")
        print(e.stderr)

