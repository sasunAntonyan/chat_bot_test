from apps.core.utils import get_weather

pairs = {
    "hi": "hi",
    "what's the weather?": "weather in Yerevan {} C".format(get_weather()),
}
