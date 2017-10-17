# Description

Implementing a dynamic Python invoker REST service. The service has the following features:

# Requirement
Docker image with flask and rocksdb dependency: Use the docker file for the image

## 1. Python Script Uploader

```bash
POST http://localhost:8000/api/v1/scripts
```

### Request

__foo.py__

```python
# foo.py
print("Hello World")
```

```bash
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@Path to local file" "http://127.0.0.1:5000/api/v1/scripts"
```

```bash
201 Created
```

```json
{
    "script-id": "123456"
}
```

## 2. Python Script Invoker

```bash
GET http://localhost:8000/api/v1/scripts/{script-id}
```

### Request

```bash
curl -i http://127.0.0.1:5000/api/v1/scripts/12350
```

```bash
200 OK
```

```json
Hello World
```



