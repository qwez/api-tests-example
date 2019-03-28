import jsons
import datetime
from utils import utils


# adding custom serializer / deserializer
jsons.set_deserializer(utils.date_deserializer, str)
jsons.set_serializer(utils.date_serializer, datetime.date)
jsons.set_serializer(utils.datetime_serializer, datetime.datetime)
