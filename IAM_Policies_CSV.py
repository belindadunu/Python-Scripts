# Script to export IAM policies to a CSV file

import boto3
import csv

# Initialize IAM client 
client = boto3.client('iam')

def iam_policy():

  # Get all IAM policies
  all_policies = client.list_policies()['Policies']

  # Set up CSV file
  csv_filename = "policies.csv"
  headers = ['PolicyName', 'PolicyId', 'Arn']

  # Open CSV file and write headers
  with open(csv_filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)

    # Write each policy to a row
    for policy in all_policies:
      row = [policy["PolicyName"], policy["PolicyId"], policy["Arn"]]
      writer.writerow(row)

  # Confirm CSV file created
  print(f"Your {csv_filename} has been successfully created!")

# Call the iam_policy function
iam_policy()

# NOTE: Configure AWS credentials with 'aws configure' first
