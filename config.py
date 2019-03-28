class TodoistApi:

    class Settings:
        auth = 'Bearer 2b49b14bbe3b4438c2ff9ce1b6b4e8db762967b0'
        base_url = 'https://beta.todoist.com/API/v8'
        content = 'application/json'
        delay = 0

    DATE_FORMAT = '%Y-%m-%d'
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    DATE_LENGTH = 10
    DATETIME_LENGTH = 20


class Constants:

    class TimeZone:
        MOSCOW = "Europe/Moscow"
