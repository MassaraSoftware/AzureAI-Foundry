# Purpose: Test connection to Azure AI Foundry using SDK
# How to run:
#   1. Open PowerShell
#   2. cd "C:\Users\massa\Desktop\Python\Reference\AzureAI-Foundry"
#   3. python test_foundry_connection.py

from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

# Azure subscription + resource details
subscription_id = "4e72e1a7-c2d3-438d-ac49-7a013a697c08"  # Your paid subscription
resource_group = "NobelDynamicsRG"                       # Resource group you created
workspace = "NobelFoundryWS"                             # Foundry workspace you created

# Authenticate with Azure (uses your Azure CLI login)
cred = DefaultAzureCredential()

# Connect to Azure AI Foundry workspace
ml_client = MLClient(cred, subscription_id, resource_group, workspace)

print("✅ Connected to Azure AI Foundry")
print(f"Workspace: {ml_client.workspace_name}")
print(f"Resource Group: {ml_client.resource_group_name}")
