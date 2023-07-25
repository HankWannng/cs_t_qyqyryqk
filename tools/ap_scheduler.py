from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    n = 0
    n += 1
    print(n)



def Bscheduler(job):
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', minutes=5)
    try:
        scheduler.start()
    except Exception as err:
        print(err)
        return


if __name__== '__main__':
    Bscheduler(job)