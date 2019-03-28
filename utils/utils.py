import datetime
from config import TodoistApi as conf
from time import sleep


def date_deserializer(obj: str, cls: type, **kwargs) -> object:
    if type(obj) != cls:
        return cls(obj)
    elif len(obj) == conf.DATE_LENGTH:
        return datetime.datetime.strptime(obj, conf.DATE_FORMAT).date()
    elif len(obj) == conf.DATETIME_LENGTH:
        return datetime.datetime.strptime(obj, conf.DATETIME_FORMAT)
    return obj


def date_serializer(obj: datetime.date, **kwargs) -> str:
    return obj.strftime(conf.DATE_FORMAT)


def datetime_serializer(obj: datetime.datetime, **kwargs) -> str:
    return obj.strftime(conf.DATETIME_FORMAT)


def delay(decorated):
    def with_delay(instance, *args, **kwargs):
        sleep(instance.delay)
        return decorated(instance, *args, **kwargs)
    return with_delay
