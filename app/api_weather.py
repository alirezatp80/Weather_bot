import requests
import jdatetime
from datetime import datetime

def convert_to_jalali(iso_time: str) -> str:
    
    time_obj = datetime.fromisoformat(iso_time)
    
    jalali_date = jdatetime.date.fromgregorian(date=time_obj.date())
    
    time_str = time_obj.strftime("%H:%M")
    
    return f"{jalali_date} ساعت {time_str}"

weather_codes = {
    0: "☀️ صاف",
    1: "🌤️ نیمه‌ابری",
    2: "☁️ ابری",
    3: "🌫️ مه",
    45: "🌫️🌧️ مه و باران سبک",
    48: "🌫️❄️ مه با باران یخ‌زده",
    51: "🌦️ نم نم باران",
    53: "🌧️ باران متوسط",
    55: "🌧️ باران شدید",
    56: "🌧️❄️ باران یخ‌زده ریز",
    57: "🌧️❄️ باران یخ‌زده شدید",
    61: "🌧️ باران",
    63: "🌧️ باران متوسط",
    65: "🌧️ باران شدید",
    66: "🌧️❄️ باران یخ‌زده",
    67: "🌧️❄️ باران یخ‌زده شدید",
    71: "❄️ برف سبک",
    73: "❄️ برف متوسط",
    75: "❄️ برف شدید",
    77: "❄️ دانه‌های برف (Snow grains)",
    80: "🌦️ باران رگباری",
    81: "🌧️ باران رگباری شدید",
    82: "🌧️ باران رگباری خیلی شدید",
    85: "❄️ برف رگباری",
    86: "❄️ برف رگباری شدید",
    95: "⛈️ رعد و برق",
    96: "⛈️🌧️ رعد و برق با باران سبک",
    99: "⛈️🌧️ رعد و برق با باران شدید"
}
def feels_emoji(feels_like):
    if feels_like <= 0:
        return "🥶"   # خیلی سرد
    elif feels_like <= 10:
        return "🧥"   # سرد
    elif feels_like <= 20:
        return "🙂"   # معتدل
    elif feels_like <= 30:
        return "😎"   # گرم
    else:
        return "🥵"   # خیلی گرم
    
def format_today_weather(data):
    
    today = data['current_weather']
    time_temp = today['time']
    time = convert_to_jalali(time_temp)
    time_of_day = "روز" if today['is_day'] == 1 else "شب"
    time_emoji = "🌞" if today['is_day'] == 1 else "🌙"
    
    temperature = today['temperature']
    wind = today['windspeed']
    humidity = today.get('relative_humidity', 50)
    feels_like_value = feels_tempurture(temperature, wind, humidity)
    feels_emo = feels_emoji(feels_like_value)
    
    today_also = data['daily']
    code = today['weathercode']
    today_weather_about = weather_codes.get(code, "نامشخص")
    precipitation_probability = today_also['precipitation_probability_max'][0]
    
    text = f"""
{time_emoji} زمان: {time_of_day} - {time}
🌡️ دما: {temperature}°C
{feels_emo} دمای احساس شده: {feels_like_value}°C
وضعیت هوا: {today_weather_about}
🌧️ احتمال بارش: {precipitation_probability}%
"""
    return text
def feels_tempurture(temperature, wind, humidity):
    if temperature<10:
        num = wind//10
        if num != 0:
            temperature -=num
        else:
             temperature
    elif temperature > 20 and humidity > 60:
         temperature += 2
    else:
        wind_num = wind//10
        if humidity>60:
            temperature+=2
        if wind_num != 0:
             temperature -= wind_num
        else:
             temperature
    return round(temperature , 1)

def today_weather(input_user:str):
    lat, lon = input_user.split(',')
    latitude = float(lat)
    longitude = float(lon)

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&current_weather=true"
        "&daily=apparent_temperature_max,apparent_temperature_min,precipitation_probability_max,weathercode"
        "&timezone=auto"
    )

    data = requests.get(url).json()
    return(format_today_weather(data))
    
    
