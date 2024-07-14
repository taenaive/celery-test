from asyncio import run, sleep

import json
from main import TaskQueue

async def runClient():
        result = TaskQueue.delay("Hola Task for Celery!")
        # print( dir(result))
        #print(f"${result.status} > {result.id}")
        while  result.status == 'PENDING':
                await sleep(1)
                print(f"${result.status} > {result.result} > {result.task_id}")
                # print( vars(result))
        
        
run(runClient())