from azure.mgmt.resource.resources import ResourceManagementClient


def get_resource_client(credential, subscription_id):

    return ResourceManagementClient(
        credential,
        subscription_id
    )