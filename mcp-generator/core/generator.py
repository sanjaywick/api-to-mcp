def generate_mcp_tools(parsed_tools):
    mcp_tools = []
    for tool in parsed_tools:
        input_properties = {}
        required = []
        for param in tool["parameters"]:
            input_properties[param["name"]] = {"type": param.get("type", "string")}
            if param.get("required", False):
                required.append(param["name"])
        
        mcp_tools.append({
            "name": tool["name"],
            "description": tool["description"],
            "method": tool["method"],
            "path": tool["path"],
            "input_schema": {
                "type": "object",
                "properties": input_properties,
                "required": required
            },
            "output_schema": {"type": "object"}
        })
    return mcp_tools
