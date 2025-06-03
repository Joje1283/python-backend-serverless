from fastapi import FastAPI, Depends
from pydantic import BaseModel
from enum import StrEnum
from sqs import get_sqs_client

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Serverless FastAPI!"}


class PushMessage(BaseModel):
    type: str
    user_id: str
    title: str
    message: str


class QueueName(StrEnum):
    push = "push"


@app.post("/push")
def push_message(message: PushMessage, sqs_client=Depends(get_sqs_client)):
    """
    Push a message to the SQS queue.
    """
    message_json = message.model_dump_json()
    queue_url = sqs_client.get_queue_url(QueueName=QueueName.push)
    sqs_client.send_message(QueueUrl=queue_url.get("QueueUrl"), MessageBody=message_json, DelaySeconds=0)
    return {"status": "Message sent", "message": message}
