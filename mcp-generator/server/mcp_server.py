from fastapi import FastAPI, HTTPException
from core.parser import parse_openapi_spec
from core.generator import generate_mcp_tools
from core.request_handler import call_api

import os

BASE_URL = "https://petstore.swagger.io/v2"
SPEC_PATH = "spec/petstore.json"

app = FastAPI(title="MCP Petstore Server")

# Parse spec and generate MCP tools
parsed_tools = parse_openapi_spec(SPEC_PATH)
tools = generate_mcp_tools(parsed_tools)

# In-memory lookup by tool name
tool_lookup = {tool["name"]: tool for tool in tools}

@app.get("/tools")
def list_tools():
    return tools

@app.post("/invoke/{tool_name}")
def invoke_tool(tool_name: str, payload: dict):
    tool = tool_lookup.get(tool_name)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    
    result = call_api(BASE_URL, tool["method"], tool["path"], params=payload, data=payload)
    return result
