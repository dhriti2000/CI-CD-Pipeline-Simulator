import argparse
from scheduler import Scheduler
from worker import Worker
from logger import setup_logger, log
from config import MAX_WORKERS
from parser import load_pipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", default="pipeline.yaml")
    args = parser.parse_args()

    setup_logger()

    jobs = load_pipeline(args.pipeline)

    scheduler = Scheduler(jobs)
    scheduler.resolve_dependencies()

    workers = [Worker(scheduler) for _ in range(MAX_WORKERS)]

    for w in workers:
        w.start()

    for w in workers:
        w.join()

    log("Pipeline execution completed")

if __name__ == "__main__":
    main()