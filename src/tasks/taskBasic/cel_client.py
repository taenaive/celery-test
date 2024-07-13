from asyncio import run, sleep

import json
from main import TaskQueue


# write_log("log testing..... !!!!")

async def runClient():
        result = TaskQueue.delay("Hola Task for Celery!")
        # print( dir(result))
        print(f"${result.status} > {result.id}")
        await sleep(1)
        print(f"${result.status} > {result.result} > {result.task_id}")
        # print( vars(result))
        
run(runClient())