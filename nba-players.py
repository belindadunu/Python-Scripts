import requests
import csv

# Get API key  
api_key = input("Enter your RapidAPI key: ")

# Get filename
filename = input("Enter CSV name: ")

# Set up headers
headers = {
  "X-RapidAPI-Key": api_key,
  "X-RapidAPI-Host": "free-nba.p.rapidapi.com" 
}

# Set up query params
querystring = {"page":"0","per_page":"100"} 

# Make API request
url = "https://free-nba.p.rapidapi.com/players"
response = requests.get(url, headers=headers, params=querystring)

# Handle non-200 status code
if response.status_code != 200:
  print(f"Error {response.status_code}")
  
# Parse JSON 
data = response.json()

# Extract player data
players = []

for p in data["data"]:
  name = p["first_name"] + " " + p["last_name"]
  position = p["position"]
  team = p["team"]["full_name"]

  player = [name, position, team]
  players.append(player)

# Write CSV
with open(filename, "w") as f:

  writer = csv.writer(f)
  
  for player in players:
    writer.writerow(player)
    
print("Written successfully!")
