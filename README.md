Steps to run:
1. cd mcp-generator
2. pip install -r requirments.txt
3. cd..
4. .venv/Scripts/activate
5. uvicorn server.mcp_server:app --reload

Test:
Open Postman 
Method = POST
URL= http://127.0.0.1:8000/invoke/addPet
Body = raw
{
  "body": {
    "id": 123,
    "name": "fluffy",
    "tag": "dog"
  }
}


Expected Output
{
    "status": "success",
    "data": {
        "id": 123,
        "name": "fluffy",
        "photoUrls": [],
        "tags": []
    }
}
