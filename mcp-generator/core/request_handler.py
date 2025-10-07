import requests

def call_api(base_url, method, path, params=None, data=None, headers=None):
    params = params or {}
    headers = headers or {}
    
    # Replace path parameters
    for key in list(params.keys()):
        if f"{{{key}}}" in path:
            path = path.replace(f"{{{key}}}", str(params[key]))
            params.pop(key)
    
    url = f"{base_url}{path}"
    
    # For POST/PUT/PATCH, send JSON body
    json_data = None
    if method.upper() in ["POST", "PUT", "PATCH"] and "body" in data:
        json_data = data["body"]
    
    try:
        response = requests.request(method, url, params=params, json=json_data, headers=headers)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}
