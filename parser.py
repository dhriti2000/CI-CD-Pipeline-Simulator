import yaml
from pipeline import Job
import time
import random
from logger import log

# Job functions
def build():
    time.sleep(1)
    log("Build successful")

def test():
    time.sleep(1)
    if random.choice([True, False]):
        raise Exception("Random test failure")
    log("Tests passed")

def deploy():
    time.sleep(1)
    log("Deployment done")

FUNCTION_MAP = {
    "build": build,
    "test": test,
    "deploy": deploy
}

def load_pipeline(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    if "jobs" not in data:
        raise Exception("Invalid YAML: 'jobs' key missing")

    jobs = []

    for job_data in data["jobs"]:
        name = job_data.get("name")
        if not name:
            raise Exception("Job missing 'name'")

        dependencies = job_data.get("depends_on", [])
        retries = job_data.get("retries", 2)

        job = Job(
            name=name,
            dependencies=dependencies,
            func=FUNCTION_MAP.get(name),
            retries=retries
        )
        jobs.append(job)

    return jobs