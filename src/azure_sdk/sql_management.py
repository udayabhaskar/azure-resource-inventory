from azure.mgmt.sql import SqlManagementClient
from utils.azure_helpers import get_resource_group_name

def create_sql_management_client(
    credential,
    subscription_id
):

    return SqlManagementClient(
        credential,
        subscription_id
    )
def get_sql_database_details(sql_client):    

    sql_databases = []

    for sql_server in sql_client.servers.list():
        for sql_database in sql_client.databases.list_by_server(
            get_resource_group_name(sql_server.id), sql_server.name
        ):
            sql_databases.append({
                "name": sql_database.name,
                "server_name": sql_server.name,
                "resource_group": get_resource_group_name(sql_server.id),
                "location": sql_database.location,
                "status": sql_database.status,
                "max_size_bytes": sql_database.max_size_bytes,
                "pricing_tier": sql_database.sku.name if sql_database.sku else "N/A"
            })

    return sql_databases