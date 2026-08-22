import subprocess
import shutil


def get_resource_group_name(resource_id):

    return resource_id.split("/")[4]

def get_subscription_id():

    az_command = shutil.which("az")

    if not az_command:
        raise RuntimeError("Azure CLI (az) was not found in PATH.")

    subscription_id = subprocess.run(
        [az_command, "account", "show", "--query", "id", "-o", "tsv"],
        capture_output=True,
        text=True,
        check=True
    ).stdout.strip()

    return subscription_id
