from data.exts import db
from sqlalchemy.sql import text

def getWorkouts():
    query = text(
        "select info2.workoutID, info2.workoutname, info2.videolink, info2.difficulty, info2.musclegroup1, info2.musclegroup2, m.musclegroup as musclegroup3 " 
        "from "
            "(select info1.workoutID, info1.workoutname, info1.videolink, info1.musclegroupID1, info1.musclegroupID2, info1.musclegroupID3, info1.difficulty, info1.musclegroup1, m.musclegroup as musclegroup2 "
            "from "
                "(select workoutID, workoutname, videolink, musclegroupID1, musclegroupID2, musclegroupID3, difficulty, m.musclegroup as musclegroup1 "
                "from workoutbank "
                "left join "
                "musclegroup m "
                "on musclegroupID1 = musclegroupID "
                "order by workoutID asc) info1 "
            "left join "
            "musclegroup m "
            "on musclegroupID2 = musclegroupID "
            "order by workoutID asc) info2 "
        "left join "
        "musclegroup m "
        "on musclegroupID3 = musclegroupID "
        "order by workoutID asc "
    )
    results = db.session.execute(query).fetchall()
    return results
