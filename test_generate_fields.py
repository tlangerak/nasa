import pyrebase
import random
import datetime

config = {
    "apiKey": "AIzaSyDbWlGG-aqzoePURjVEbAWeOVjXrqNXI_I",
    "authDomain": "farmate-f4c81.firebaseapp.com",
    "databaseURL": "https://farmate-f4c81.firebaseio.com",
    "projectId": "farmate-f4c81",
    "storageBucket": "farmate-f4c81.appspot.com",
    "serviceAccount": "Farmate-4a85a1daab0d.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("hello@thomaslangerak.nl", "random")

db = firebase.database()




for i in range(10):
    HP_list= random.sample(xrange(50), 30)
    RF_list= random.sample(xrange(50), 30)
    ET_list= random.sample(xrange(50), 30)
    DP_list= random.sample(xrange(50), 30)
    RO_list= random.sample(xrange(50), 30)
    IR_list = random.sample(xrange(50), 30)
    IR_rec_list = random.sample(xrange(50), 30)
    IR_rec= 9
    desired_depth_chart = random.sample(xrange(50), 30)
    critical_depth_chart = random.sample(xrange(50), 30)
    HP_pre_list = random.sample(xrange(50), 6)
    ET_pre_list = random.sample(xrange(50), 6)
    RF_pre_list = random.sample(xrange(50), 6)
    DP_pre_list = random.sample(xrange(50), 6)
    RO_pre_list = random.sample(xrange(50), 6)

    main = {"owner_id": i,
            "name": "field #1",
            "area": 4,
            "year_transplant": 2017,
            "month_transplant": 6,
            "day_transplant": 7,
            "year_irrigation": 2017,
            "month_irrigation": 6,
            "day_irrigation": 8,
            "long_shape": [892],
            "lat_shape": [89723],
            "lat_center": 0,
            "long_center": 0,
            "soil_type": 3,
            "crop_type": "rice",
            "HP": 0,
            "dike_height": 10,
            "HP_list": HP_list,
            "RF_list": RF_list,
            "ET_list": ET_list,
            "DP_list": DP_list,
            "RO_list": RO_list,
            "IR_list": IR_list,
            "IR_rec": IR_rec,
            "IR_rec_list": IR_rec_list,
            "HP_pre_list":HP_pre_list,
            "ET_pre_list":ET_pre_list,
            "RF_pre_list":RF_pre_list,
            "DP_pre_list":DP_pre_list,
            "RO_pre_list":RO_pre_list,
            "desired_depth_chart": desired_depth_chart,
            "critical_depth_chart": critical_depth_chart
    }

    db.child("main").push(main, user['idToken'])


