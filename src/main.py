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
from azure_sdk.sql_management import (
    create_sql_management_client,
    get_sql_database_details
)
from azure_sdk.app_service_management import (
    create_web_management_client,
    get_app_service_details
)
from azure_sdk.key_vaults import (
    create_key_vault_management_client,
    get_key_vault_details
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
        sql_client = create_sql_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
        )
        app_service_client = create_web_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
        )
        key_vault_client = create_key_vault_management_client(
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
        sql_database_details = get_sql_database_details(sql_client)
        logger.info(
        f"Retrieved {len(sql_database_details)} SQL Databases."
        )
        app_service_details = get_app_service_details(app_service_client)
        logger.info(
        f"Retrieved {len(app_service_details)} App Services."
        )
        key_vault_details = get_key_vault_details(key_vault_client)
        logger.info(
        f"Retrieved {len(key_vault_details)} Key Vaults."
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
        print()
        print("SQL Databases")
        print("-" * 50)
        for sql_database in sql_database_details:
            print(f"Name           : {sql_database['name']}")
            print(f"Server Name    : {sql_database['server_name']}")
            print(f"Resource Group : {sql_database['resource_group']}")
            print(f"Location       : {sql_database['location']}")
            print(f"Status         : {sql_database['status']}")
            print(f"Max Size (Bytes): {sql_database['max_size_bytes']}")
            print(f"Pricing Tier   : {sql_database['pricing_tier']}")
            print("-" * 50)
        print()
        sql_database_report_created = write_csv_report(
            sql_database_details,
            "output/sql_databases.csv"
        )
        print()
        print("App Services")
        print("-" * 50)
        for app_service in app_service_details:
            print(f"Name           : {app_service['name']}")
            print(f"Resource Group : {app_service['resource_group']}")
            print(f"Location       : {app_service['location']}")
            print(f"State          : {app_service['state']}")
            print(f"Default Host Name: {app_service['default_host_name']}")
            print(f"App Service Plan: {app_service['app_service_plan_name']}")
            print(f"OS Type        : {app_service['os_type']}")
            print(f"Pricing Tier   : {app_service['pricing_tier']}")
            print(f"App Service URL: {app_service['app_service_url']}")
            print(f"Deployment Slots: {', '.join(app_service['deployment_slots']) if app_service['deployment_slots'] else 'N/A'}")
            print(f"Custom Domains : {', '.join(app_service['custom_domains']) if app_service['custom_domains'] else 'N/A'}")
            print("-" * 50)
        print()
        app_service_report_created = write_csv_report(
            app_service_details,
            "output/app_services.csv"
        )   
        print()
        print("Key Vaults")
        print("-" * 50)
        for key_vault in key_vault_details:
            print(f"Name           : {key_vault['name']}")
            print(f"Resource Group : {key_vault['resource_group']}")
            print(f"Location       : {key_vault['location']}")
            print(f"Tenant ID      : {key_vault['tenant_id']}")
            print(f"Soft Delete Enabled: {key_vault['soft_delete_enabled']}")
            print(f"Purge Protection Enabled: {key_vault['purge_protection_enabled']}")
            print(f"Public Network Access: {key_vault['public_network_access']}")
            print(f"Provisioning State: {key_vault['provisioning_state']}")
            print("-" * 50)
        print()
        key_vault_report_created = write_csv_report(
            key_vault_details,
            "output/key_vaults.csv"
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
        if sql_database_report_created:
             logger.info("SQL Database CSV report generated successfully.")
             print("SQL Database CSV report generated successfully.")
        else:
             print("No SQL Databases found. CSV report was not generated.")
        if app_service_report_created:
             logger.info("App Service CSV report generated successfully.")
             print("App Service CSV report generated successfully.")
        else:
             print("No App Services found. CSV report was not generated.")
        
        logger.info("Azure Resource Inventory completed successfully.")
        if key_vault_report_created:
             logger.info("Key Vault CSV report generated successfully.")
             print("Key Vault CSV report generated successfully.")
        else:
             print("No Key Vaults found. CSV report was not generated.")
    
    except Exception as ex:

        logger.exception("Failed to generate Azure Resource Inventory.")

        print("\nERROR: Failed to generate Azure Resource Inventory.")

        print(f"Reason: {ex}")
if __name__ == "__main__":
    main()