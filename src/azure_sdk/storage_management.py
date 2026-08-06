from azure.mgmt.storage import StorageManagementClient

from utils.azure_helpers import get_resource_group_name


def create_storage_management_client(
    credential,
    subscription_id
):

    return StorageManagementClient(
        credential,
        subscription_id
    )


def get_storage_account_details(storage_client):

    storage_accounts = []

    for storage_account in storage_client.storage_accounts.list():

        storage_accounts.append({
            "name": storage_account.name,
            "resource_group": get_resource_group_name(storage_account.id),
            "location": storage_account.location
        })

    return storage_accounts