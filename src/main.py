import logging
from azure_sdk.auth import get_credential
from azure_sdk.storage_management import (
    create_storage_management_client,
    get_storage_account_details
)
from azure_sdk.resource_management import (
    create_resource_management_client,
    get_resource_group_details
)
from azure_sdk.vm_management import (
    create_compute_management_client,
    get_virtual_machine_details
)
from settings import AZURE_SUBSCRIPTION_ID
from exporter.csv_export import write_csv_report
from logging_config import configure_logging


def main():

    logger = configure_logging()

    logger.info("Azure Resource Inventory started.")
    
    try:
        
        credential = get_credential()

        resource_client = create_resource_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
        )
        storage_client = create_storage_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
        )
        compute_client = create_compute_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
        )

        resource_group_details = get_resource_group_details(resource_client)
        logger.info(
        f"Retrieved {len(resource_group_details)} Resource Groups."
        )
        storage_account_details = get_storage_account_details(storage_client)
        logger.info(
        f"Retrieved {len(storage_account_details)} Storage Accounts."
        )
        virtual_machine_details = get_virtual_machine_details(compute_client)
        logger.info(
        f"Retrieved {len(virtual_machine_details)} Virtual Machines."
        )

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
        print()

        print("Virtual Machines")
        print("-" * 50)
        for virtual_machine in virtual_machine_details:
            
            print(f"Name           : {virtual_machine['name']}")
            print(f"Resource Group : {virtual_machine['resource_group']}")
            print(f"Location       : {virtual_machine['location']}")
            print(f"Power State    : {virtual_machine['power_state']}")
            print(f"Size           : {virtual_machine['size']}")
            print(f"Operating Sys. : {virtual_machine['operating_system']}")
            print("-" * 50)

        print()
        virtual_machine_report_created = write_csv_report(
        virtual_machine_details,
        "output/virtual_machines.csv"
        )

        if storage_report_created:
             logger.info("Storage Account CSV report generated successfully.")
             print("Storage Account CSV report generated successfully.")
        else:
             print("No Storage Accounts found. CSV report was not generated.")

        if virtual_machine_report_created:
             logger.info("Virtual Machine CSV report generated successfully.")
             print("Virtual Machine CSV report generated successfully.")
        else:
             print("No Virtual Machines found. CSV report was not generated.")

        logger.info("Azure Resource Inventory completed successfully.")
    
    except Exception as ex:

        logger.exception("Failed to generate Azure Resource Inventory.")

        print("\nERROR: Failed to generate Azure Resource Inventory.")

        print(f"Reason: {ex}")
if __name__ == "__main__":
    main()