from azure.mgmt.resource.resources import ResourceManagementClient


def create_resource_management_client(credential, subscription_id):

    return ResourceManagementClient(
        credential,
        subscription_id
    )


def get_resource_group_details(resource_client):

    resource_groups = []

    for resource_group in resource_client.resource_groups.list():

        resource_groups.append({
            "name": resource_group.name
        })

    return resource_groups