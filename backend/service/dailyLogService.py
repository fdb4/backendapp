from data.models import DailyLog
from flask import jsonify

def dailyLog(clientID, calorie, water, mood):
    newLog = DailyLog(
        clientID=clientID,
        calorie=calorie,
        water=water,
        mood=mood

    )
    newLog.save()
    return jsonify({"message": "Daily Log Recorded"})
