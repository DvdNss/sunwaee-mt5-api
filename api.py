# coding:utf-8
"""
Filename : api.py
Role : api with pipelines hosting

@author : Sunwaee
"""

import os
import time

import fasttext
from fastapi import FastAPI

os.system('pip freeze venv/ > requirements.txt')


def ready_api_content():
    """
    Puts models in buffers and prepare API for requesting.
    """

    # Changing os dir
    dir_buffer = os.getcwd()
    os.chdir('system/')

    # Necessary imports
    import pipelines

    # Loading models
    language_detector = fasttext.load_model('language_detector/lid.176.ftz')
    classic_pipeline = None  # pipelines.run()

    # Returning in api  path
    os.chdir(dir_buffer)

    return language_detector, classic_pipeline


language_detector, classic_pipeline = ready_api_content()
app = FastAPI(title='MT5 API')


@app.get(path="/classic", tags=['inference'])
async def classic(text: str = ""):
    """
    Infers using classic pipeline.

        :param text: text on which apply classic task
        :return: dictionary which contains classic output
    """

    start = time.time()
    language = language_detector.predict(text=[text])
    # output = classic_pipeline(inputs=text)
    reponse_time = time.time() - start

    return {
        "input": text,
        "language": language[0][0][0].replace('__label__', ''),
        # "output": output,
        "response time": reponse_time
    }


@app.get(path='/pipeline', tags=['pipeline'])
async def pipeline(text: str = ""):
    """
    Generates a response given an input text

        :param text: text from which generate a response
        :return: a dictionary which contains the given response
    """

    return {
        'text': text,
        'output': 'Here is the pipeline output.',
        'features': 'Here are the features.',
        'response': 'Here is the response.'
    }


@app.get(path='/HelloWorld', tags=['test'])
async def hello():
    return {'text': 'Hello World!'}
