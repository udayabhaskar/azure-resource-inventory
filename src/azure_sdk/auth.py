from azure.identity import AzureCliCredential


def get_credential():
    """
    Returns Azure credentials from Azure CLI.
    """
    return AzureCliCredential()