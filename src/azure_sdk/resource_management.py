from azure.mgmt.resource.resources import ResourceManagementClient


def create_resource_management_client(credential, subscription_id):

    return ResourceManagementClient(
        credential,
        subscription_id
    )


def get_resource_group_names(resource_client):

    resource_groups = resource_client.resource_groups.list()

    return [resource_group.name for resource_group in resource_groups]