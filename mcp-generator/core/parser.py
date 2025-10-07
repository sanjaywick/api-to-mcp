import json

def parse_openapi_spec(spec_path):
    with open(spec_path, "r") as f:
        spec = json.load(f)
    
    tools = []
    paths = spec.get("paths", {})
    
    for path, methods in paths.items():
        for method, details in methods.items():
            tool = {
                "name": details.get("operationId", f"{method}_{path}"),
                "description": details.get("summary", ""),
                "method": method.upper(),
                "path": path,
                "parameters": []
            }
            # Collect parameters
            for param in details.get("parameters", []):
                tool["parameters"].append({
                    "name": param.get("name"),
                    "in": param.get("in"),
                    "required": param.get("required", False),
                    "type": param.get("schema", {}).get("type", "string")
                })
            # Check requestBody for POST/PUT
            if "requestBody" in details:
                tool["parameters"].append({
                    "name": "body",
                    "in": "body",
                    "required": True,
                    "type": "object"
                })
            tools.append(tool)
    return tools
