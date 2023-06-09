from fastapi import FastAPI, Request,Response
from time import gmtime, strftime
from app.routes.log import log
app = FastAPI()

app.include_router(log)
