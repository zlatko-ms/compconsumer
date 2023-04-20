# compconsumer

## Rationale

In order to test scaling out of containerized solutions you often need a tiny workaload that consumes CPU without waitios.

This is exectly what this workload is designed for. 

It will run for a given duration, or infintely, depending on the parameters and can be used to test scale out scenarios on K8 or serverless container solutions.


## Configuration 

CompConsumer being quite trivial, it exposes only the following configuration parameter addressed via environnement variables : 

| Env Var Name    | Default Value       | Purpose                                            |
|-----------------|---------------------|----------------------------------------------------|
| JOB_DURATION_SECONDS| 60                  | Run duration in seconds. Specify -1 for endless processing    |

## Code

The code is even more trivial as the whole implementation is contained in the 30 line python3 script named compconsumer.py.

## Docker Image

The Docker image is continously build and stored on the [Docker Hub](https://hub.docker.com/repository/docker/zlatkoa/compconsumer).

## Running as standalone

In order to run the Greeter, you'll need to install python3 and pip3 then issue the following commands : 

```bash
export JOB_DURATION_SECONDS=10
python3 ./compconsumer.py
```


