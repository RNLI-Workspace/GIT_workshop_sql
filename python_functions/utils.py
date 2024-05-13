import requests
import json
import logging

logger = logging.getLogger(__name__)

def sample_function(group_id, dataset_id, auth):
    """A function to refresh a dataset that BI is pointing at

    Args:
        group_id (str): dataset to update
        dataset_id (int): which id requires updating
        auth (str): authentication string pulled from databricks secrets

    Raises:
        ConnectionError: On any response other than 200

    Returns:
        object: response object from requests
    """    
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/refreshes"
    payload = json.dumps({"notifyOption": "NoNotification"})
    headers = {
        "Content-Type": "application/json",
        "Authorization": auth,
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response
    
    else:
        raise ConnectionError

print ("I hate Python   Excel rules....")
