## Тестовое задание для UCAR<>TOPDOER

* https://buildin.ai/share/e83a7360-91b2-4dda-88d1-44166182d964?code=1N7GCX

## Перед запуском необходимо установить переменные окружения:
* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DB

## Запуск приложения
```bash
docker compose up --build
```

### URL для создания инцидента: 
* HTTP POST 127.0.0.1:8000/api/incidents/

```json
{
    "description": "str",
    "status": "str",
    "source": "str", 
    "creation_date_time": "str"
}
```
* description - описание инцидента
* status- статус инцидента("waiting", "in_work", "closed")
* source - источник("operator", "monitoring", "partner")
* creation_date_time - необязательный параметр, строка формата "YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z]"
##### В ответ на запрос будет получен json:
```json
{
        "id": "<incident_id:int>",
        "description": "str",
        "status": "str",
        "source": "str",
        "creation_date_time": "str"
}
```

### URL для получения списка инцидентов: 
* HTTP GET 127.0.0.1:8000/api/incidents/?status-filter=str (необязательный параметр, может принимать значения waiting, in_work, closed)
##### В ответ на запрос будет получен json:
```
[
    {
        "id": 3,
        "description": "incident description 3",
        "status": "waiting",
        "source": "operator",
        "creation_date_time": "2025-12-05T00:00:00Z"
    },
    {
        "id": 2,
        "description": "incident description 2",
        "status": "closed",
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

#### URL для обновления статуса инцидента: 
* HTTP PATCH 127.0.0.1:8000/api/incidents/<incident_id:int>/
```json
{
    "status": "str"
}
```
* status - статус инцидента("waiting", "in_work", "closed")
##### В ответ на запрос будет получен json:
```json
{
        "id": "<incident_id:int>",
        "description": "str",
        "status": "str",
        "source": "str",
        "creation_date_time": "str"
}
```
