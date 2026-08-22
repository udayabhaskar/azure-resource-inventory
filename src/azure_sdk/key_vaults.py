from azure.mgmt.keyvault import KeyVaultManagementClient
from utils.azure_helpers import get_resource_group_name


def create_key_vault_management_client(
    credential,
    subscription_id
):
    return KeyVaultManagementClient(
        credential,
        subscription_id
    )


def get_key_vault_details(key_vault_client):
    key_vaults = []

    for key_vault in key_vault_client.vaults.list():
        resource_group = get_resource_group_name(key_vault.id)

        key_vault_details = key_vault_client.vaults.get(
            resource_group,
            key_vault.name
        )

        key_vaults.append({
            "name": key_vault_details.name,
            "resource_group": resource_group,
            "location": key_vault_details.location,
            "sku": (
                key_vault_details.properties.sku.name
                if key_vault_details.properties.sku
                else "N/A"
            ),
            "tenant_id": key_vault_details.properties.tenant_id,
            "soft_delete_enabled": (
                key_vault_details.properties.enable_soft_delete
            ),
            "purge_protection_enabled": (
                key_vault_details.properties.enable_purge_protection
            ),
            "public_network_access": (
                key_vault_details.properties.public_network_access
            ),
            "provisioning_state": (
                key_vault_details.properties.provisioning_state.value
                if key_vault_details.properties.provisioning_state
                else "N/A"
            ),
            "rbac_authorization_enabled": (
                key_vault_details.properties.enable_rbac_authorization
                if hasattr(
                    key_vault_details.properties,
                    "enable_rbac_authorization"
                )
                else "N/A"
            )
        })

    return key_vaults