from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.sql.models import FirewallRule

credential = DefaultAzureCredential()
subscription_id = "495a7f20-5240-47b1-af1b-03f424a91e12" 
resource_group = "rg-east-us-prod-tatenlyle"   
server_name = "sqlsrv-east-us-prod-tatenlyle"      


sql_client = SqlManagementClient(credential, subscription_id)


firewall_rule_name = "LimitedAccessRule"
start_ip_address = "106.195.7.203" 
end_ip_address = "106.195.7.203"     

firewall_rule = FirewallRule(start_ip_address=start_ip_address, end_ip_address=end_ip_address)

sql_client.firewall_rules.create_or_update(
    resource_group,
    server_name,
    firewall_rule_name,
    firewall_rule
)

print(f"Firewall rule '{firewall_rule_name}' added successfully.")
