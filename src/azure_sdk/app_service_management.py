from azure.mgmt.web import WebSiteManagementClient
from utils.azure_helpers import get_resource_group_name

def create_web_management_client(
    credentials,
    subscription_id
):
    return WebSiteManagementClient(
        credentials,
        subscription_id
    )

def get_app_service_details(app_service_client):
    app_services = []

    for app_service in app_service_client.web_apps.list():
        print("APP SERVICE:", app_service.name)
        app_services.append({
            "name": app_service.name,
            "resource_group": get_resource_group_name(app_service.id),
            "location": app_service.location,
            "state": app_service.state,
            "default_host_name": app_service.default_host_name,
            "app_service_plan_name": app_service.server_farm_id.split('/')[-1] if app_service.server_farm_id else "N/A",
            "os_type": app_service.kind,
            "pricing_tier": app_service.sku.name if app_service.sku else "N/A",
            "app_service_url": f"https://{app_service.default_host_name}" if app_service.default_host_name else "N/A",
            "deployment_slots": [slot.name for slot in app_service_client.web_apps.list_slots(get_resource_group_name(app_service.id), app_service.name)],
            "custom_domains": [domain.name for domain in app_service_client.web_apps.list_host_name_bindings(get_resource_group_name(app_service.id), app_service.name)]
        })

    return app_services