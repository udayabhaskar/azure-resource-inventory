from core.auth import get_credential
from config import SUBSCRIPTION_ID
from core.resource_management import get_resource_client


def main():

    credential = get_credential()

    resource_client = get_resource_client(
        credential,
        SUBSCRIPTION_ID
    )

    print("Azure Resource Inventory Tool")

    print(f"Client : {type(resource_client).__name__}")


if __name__ == "__main__":
    main()