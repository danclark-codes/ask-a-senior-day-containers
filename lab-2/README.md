# Lab 2 - build a dockerfile

Shamelessly taken from [ArjanCodes -  This Is How You Write an Efficient Python Dockerfile ](https://www.youtube.com/watch?v=tc713anE3UY)


# Install

Install [https://docs.astral.sh/uv](https://docs.astral.sh/uv)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


# Setup

use UV to sync your dependencies
```
uv sync
```

# Run

use UV to run `uvicorn`, a web serving app that serves FastAPI endpoints

``` powershell
uv run uvicorn main:app --log-level info --host 0.0.0.0 --port 8081 
```

Then open up [http://localhost:8081/](http://localhost:8081/) or even [http://localhost:8081/?name=dan](http://localhost:8081/?name=dan) for a personalised greeting.


# Dockerfile
Create your dockerfile as a file called `Dockerfile` (no extension).

Add your commands, and then run the following to build from that dockerfile

```powershell
    docker build -t myapp:0.1 .
```

then you can run with:
```
    docker run -d --name myapp -p 8081:8081 myapp:0.1     
```

then you can check it's working by visiting [http://localhost:8081](http://localhost:8081)


### References
UV is a good place to start
[https://docs.astral.sh/uv/guides/integration/docker/#installing-uv](https://docs.astral.sh/uv/guides/integration/docker/#installing-uv)