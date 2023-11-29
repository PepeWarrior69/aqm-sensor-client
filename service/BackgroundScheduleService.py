from apscheduler.schedulers.background import BackgroundScheduler
from typing import List, Dict, Union
import uuid

class BackgroundScheduleService:
    def __init__(self):
        self.schedule_jobs: List[Dict[str, Union[BackgroundScheduler, str]]] = []
    
    # handle cleanup if it's needed
    def cleanup(self):
        for job in self.schedule_jobs:
            job["handle"].shutdown()
            print(f"Job with id={job['id']} is stopped")
        
        self.schedule_jobs = []
        
        print("BackgroundScheduleService cleanup is finished")
        
    def add_background_job(self, job, seconds) -> str:
        id = str(uuid.uuid4())[0:8]
        
        scheduler = BackgroundScheduler()
        scheduler.add_job(job, 'interval', seconds=seconds)
        
        self.schedule_jobs.append({
            "id": id,
            "handle": scheduler
        })
        
        return id
    
    def _get_job_by_id(self, id):
        job = next(item for item in self.schedule_jobs if item["id"] == id)
        
        if not job:
            raise Exception(f"Background job with {id=} is missing")
        if not job["handle"]:
            raise Exception(f"Handle of job with {id=} is missing")
        
        return job
    
    def start(self, id: str) -> bool:
        job = self._get_job_by_id(id)
        job["handle"].start()
        
        return True
    
    def stop(self, id) -> bool:
        job = self._get_job_by_id(id)
        job["handle"].shutdown()
        
        return True
