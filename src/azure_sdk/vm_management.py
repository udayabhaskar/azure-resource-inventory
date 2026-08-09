from azure.mgmt.compute import ComputeManagementClient
from utils.azure_helpers import get_resource_group_name


def create_compute_management_client(
    credential,
    subscription_id
):

    return ComputeManagementClient(
        credential,
        subscription_id
    )
def get_virtual_machine_details(compute_client):    

    virtual_machines = []

    for vm in compute_client.virtual_machines.list_all():
        virtual_machines.append({
            "name": vm.name,
            "resource_group": get_resource_group_name(vm.id),
            "location": vm.location,
            "power_state": compute_client.virtual_machines.instance_view(
                get_resource_group_name(vm.id), vm.name
            ).statuses[1].display_status,
            "size": vm.hardware_profile.vm_size,
            "operating_system": vm.storage_profile.os_disk.os_type.value,
        })

    return virtual_machines