from queue import Queue

class Scheduler:
    def __init__(self, jobs):
        self.jobs = {job.name: job for job in jobs}
        self.queue = Queue()

    def resolve_dependencies(self):
        for job in self.jobs.values():
            if not job.dependencies:
                self.queue.put(job)

    def get_next_job(self):
        if not self.queue.empty():
            return self.queue.get()
        return None

    def mark_complete(self, job):
        job.completed = True

        for j in self.jobs.values():
            if not j.completed and not j.failed:
                if all(self.jobs[d].completed for d in j.dependencies):
                    self.queue.put(j)