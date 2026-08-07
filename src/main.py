from azure_sdk.auth import get_credential
from azure_sdk.storage_management import (
    create_storage_management_client,
    get_storage_account_details
)
from azure_sdk.resource_management import (
    create_resource_management_client,
    get_resource_group_details
)
from settings import AZURE_SUBSCRIPTION_ID
from exporter.csv_export import write_csv_report


def main():

    credential = get_credential()

    resource_client = create_resource_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
    )
    storage_client = create_storage_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
    )

    resource_group_details = get_resource_group_details(resource_client)
    storage_account_details = get_storage_account_details(storage_client)

    print("=" * 50)
    print("Azure Resource Inventory Tool")
    print("=" * 50)

    print(f"Subscription ID : {AZURE_SUBSCRIPTION_ID}\n")

    print("Resource Groups")
    print("-" * 50)

    for resource_group in resource_group_details:
        print(resource_group["name"])
    
    print()

    print("Storage Accounts")
    print("-" * 50)

    for storage_account in storage_account_details:

        print(f"Name           : {storage_account['name']}")
        print(f"Resource Group : {storage_account['resource_group']}")
        print(f"Location       : {storage_account['location']}")
        print("-" * 50)
    print()

    storage_report_created = write_csv_report(
    storage_account_details,
    "output/storage_accounts.csv"
)

    if storage_report_created:
        print("Storage Account CSV report generated successfully.")
    else:
        print("No Storage Accounts found. CSV report was not generated.")

if __name__ == "__main__":
    main()