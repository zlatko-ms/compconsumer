#!/usr/local/bin/python3

import os
import time
import logging
import numpy as np

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
duration: int = int(os.getenv("JOB_DURATION_SECONDS", 60))
memallocmb: int = int(os.getenv("JOB_MEMORY_MBS", 1024))
endless: bool = duration < 1

logging.info("allocating " + str(memallocmb) + " MB(s) of memory before starting")
arr = np.zeros((memallocmb * 256, 1024, 4))

if endless:
    logging.info("job will run untill killed")
else:
    logging.info("job will run for " + str(duration) + " seconds")

start = time.time()
while 1 == 1:
    numbers: list = list(range(1, 1000))
    factoriel: int = 1
    for i in numbers:
        factoriel = factoriel * i
        currentDuration: int = time.time() - start
        if (currentDuration >= duration) and (not endless):
            logging.info("job exiting after " + str(currentDuration) + " seconds")
            os._exit(0)
