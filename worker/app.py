from enum import StrEnum
from chalice import Chalice

app = Chalice(app_name="worker")


class QueueName(StrEnum):
    push = "push"


@app.on_sqs_message(QueueName.push, batch_size=1)
def push_handler(event):
    for record in event:
        body = record.body
        # Assuming body is a JSON string, you can parse it here if needed
        print(f"Received message: {body}")
        # Process the message as needed
        # For example, you could log it or perform some action based on its content
