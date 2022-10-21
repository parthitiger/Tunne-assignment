import uvicorn
from fastapi import FastAPI, Depends, Request, Form, APIRouter
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
#from common import details
#import functools

app = FastAPI()

details = []

from fastapi.staticfiles import StaticFiles


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")  

"""@app.on_event('startup')
def init_data():
    print("init call")
    details = [] """

@app.get('/details_list')
async def get_all_details(request:Request, response_class=HTMLResponse):
    return templates.TemplateResponse("details.html", {"request": request, "details": details})


@app.get('/')
async def get_initial_question(request:Request, reponse_class=HTMLResponse):
    #details = []
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/age_question')
async def get_age_question(request:Request, reponse_class=HTMLResponse):
    return templates.TemplateResponse('age.html', {"request": request})

@app.post('/age_question')
async def get_age_question(request: Request, question_result = Form(...)):
    out = {}
    out['question'] = "how much you weight?"
    out['value'] = question_result
    details.append(out)
    response = RedirectResponse('/details_list', status_code=303)
    return response
    

@app.get('/dye_question')
async def get_dye_question(request:Request, reponse_class=HTMLResponse):
    return templates.TemplateResponse('dye.html', {"request": request})

@app.post('/dye_question')
async def get_dye_question(request: Request,question_result = Form(...)):
    out = {}
    out['question'] = "how often you dye your hair?"
    out['value'] = question_result
    details.append(out)
    response = RedirectResponse('/details_list', status_code=303)
    return response

@app.get('/question')
async def get_initial_question(request:Request, reponse_class=HTMLResponse):
    #details = []
    return templates.TemplateResponse('index.html', {"request": request})

@app.post('/question')
async def get_question(request: Request, question_result = Form(...)):
    #details = []
    out = {}
    out['question'] = "when you were born?"
    out['value'] = question_result
    details.append(out)
    print(question_result)
    if int(question_result) > 35:
        response = RedirectResponse('/age_question', status_code=303)
    else:
        response = RedirectResponse('/dye_question', status_code=303)       
    return response

@app.post('/')
async def get_question(request: Request, question_result = Form(...)):
    #details = []
    out = {}
    out['question'] = "when you were born?"
    out['value'] = question_result
    details.append(out)
    print(question_result)
    if int(question_result) > 35:
        response = RedirectResponse('/age_question', status_code=303)
    else:
        response = RedirectResponse('/dye_question', status_code=303)       
    return response

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')  