from azure_sdk.auth import get_credential
from azure_sdk.resource_management import (
    create_resource_management_client,
    get_resource_group_names
)
from settings import AZURE_SUBSCRIPTION_ID


def main():

    credential = get_credential()

    resource_client = create_resource_management_client(
        credential,
        AZURE_SUBSCRIPTION_ID
    )

    resource_group_names = get_resource_group_names(resource_client)

    print("=" * 50)
    print("Azure Resource Inventory Tool")
    print("=" * 50)

    print(f"Subscription ID : {AZURE_SUBSCRIPTION_ID}\n")

    print("Resource Groups")
    print("-" * 50)

    for resource_group_name in resource_group_names:
        print(resource_group_name)


if __name__ == "__main__":
    main()