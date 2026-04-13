import threading
from logger import log

class Worker(threading.Thread):
    def __init__(self, scheduler):
        super().__init__()
        self.scheduler = scheduler

    def run(self):
        while True:
            job = self.scheduler.get_next_job()
            if job is None:
                break

            log(f"Running job: {job.name}")

            job.run()

            if job.failed:
                log(f"Job FAILED: {job.name}")
                break
            else:
                log(f"Completed job: {job.name}")
                self.scheduler.mark_complete(job)