import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def speedtest(path):
    os.system("speedtest-cli --simple >> " + path)

def safeToFile(path):
    testInformation = "{}\n\n".format(datetime.now())
    resultFile = open(path, "a")
    resultFile.write(testInformation)
    resultFile.close()

def recordTest():
    path = "SpeedTest_Results.txt"
    print("Begin Test..")
    speedtest(path)
    safeToFile(path)
    print("Test Completed..")

recordTest()
scheduler = BlockingScheduler()
scheduler.add_job(recordTest, 'interval', minutes=30)
scheduler.start()