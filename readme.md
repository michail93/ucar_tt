### Тестовое задание для UCAR<>TOPDOER

* https://buildin.ai/share/e83a7360-91b2-4dda-88d1-44166182d964?code=1N7GCX

#### url для создания инцидента: 
* HTTP POST 127.0.0.1:8000/api/incidents/

```json
{
    "description": str, #описание инцидента
    "status": str, #статус инцидента("waiting", "in_work", "closed")
    "source": str, #источник("operator", "monitoring", "partner")
    "creation_date_time": str(необязательный параметр, формат параметра "YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z]"
}
```

#### url для получения списка инцидентов: 
* HTTP GET 127.0.0.1:8000/api/incidents/?status-filter=str (необязательный параметр, может принимать значения waiting, in_work, closed)
##### В ответ на запрос будет получен json:
```
[
    {
        "id": 3,
        "description": "incident description 3",
        "status": "in_work",
        "source": "operator",
        "creation_date_time": "2025-12-05T00:00:00Z"
    },
    {
        "id": 2,
        "description": "incident description 2",
        "status": "in_work",
        "source": "operator",
        "creation_date_time": "2025-11-07T12:24:20.293864Z"
    },
    {
        "id": 1,
        "description": "incident description 1",
        "status": "in_work",
        "source": "operator",
        "creation_date_time": "2025-11-07T12:24:19.341363Z"
    }
]
```

#### url для обновления статуса инцидента: 
* HTTP PATCH 127.0.0.1:8000/api/incidents/<incident_id:int>/
```json
{
    "status": str, #статус инцидента("waiting", "in_work", "closed")
}
```
##### В ответ на запрос будет получен json:
```json
{
        "id": <incident_id:int>,
        "description": str,
        "status": str,
        "source": str,
        "creation_date_time": str
}
```