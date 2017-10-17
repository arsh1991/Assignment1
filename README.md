# Requirements

You will be implementing a dynamic Python invoker REST service. The service will have the following features:
docker build -t ubuntu-python3.6-rocksdb-grpc-flask:1.0 .


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
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/home/arsh/Downloads/assignment1/file/foo.py" "http://127.0.0.1:5000/api/v1/scripts"
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
GET http://127.0.0.1:5000/api/v1/scripts/123450
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



