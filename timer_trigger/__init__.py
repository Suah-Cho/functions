import logging
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger!!!11')
    logging.error('Python timer trigger!!!11')