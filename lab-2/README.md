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