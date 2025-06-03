# 🐍 Python Backend Serverless Monorepo

This is a **monorepo** for a fully **serverless Python backend** architecture, designed for scalability, modularity, and cost-efficiency.

## 🔧 Tech Stack

* **REST API**: [FastAPI](https://fastapi.tiangolo.com/) + [Mangum](https://mangum.fastapiexpert.com/) + [Serverless Framework](https://www.serverless.com/)
* **WebSocket**: [AWS Chalice](https://aws.github.io/chalice/tutorials/wschat.html), [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
* **Worker**: \[AWS Chalice], [Amazon SQS](https://aws.amazon.com/sqs/)
* **Scheduler (Cron)**: \[AWS Chalice]
* **CI/CD**: GitHub Actions

## 📁 Project Structure

```
python-backend-serverless/
│
├── .github/workflows/     # GitHub Actions workflows for CI/CD
├── restapi/               # REST API (FastAPI + Mangum + Serverless Framework)
├── websocket/             # WebSocket endpoint (AWS Chalice + DDB + CloudFormation)
├── scheduler/             # Scheduled tasks via EventBridge/Cron (AWS Chalice)
├── worker/                # Background task processor using SQS (AWS Chalice)
└── .gitignore
```

Each directory is an **independent serverless microservice**, deployable and testable in isolation.

---

## 🧹 Features

* **Monorepo with Modular Services**: Clear separation between API, background jobs, and real-time WebSocket layer
* **Fully Serverless**: Zero-server management using AWS Lambda, API Gateway, EventBridge, etc.
* **FastAPI-based REST APIs**: Modern Python web framework with OpenAPI documentation
* **Chalice for Lightweight Services**: Simplifies Lambda deployment for schedulers, WebSockets, and workers
* **WebSocket with State Management**: WebSocket service uses DynamoDB and CloudFormation based on [Chalice WebSocket Tutorial](https://aws.github.io/chalice/tutorials/wschat.html)
* **Worker Queue Integration**: Worker service processes asynchronous jobs via Amazon SQS
* **Production-Ready CI/CD**: GitHub Actions configured per service
* **Future-Ready**: Easily extendable to add more modules like analytics, admin tools, etc.

---

## 🚀 Getting Started

Each module contains its own `README.md` (coming soon) with specific setup instructions.
You can navigate into each directory and deploy independently:

```bash
# REST API
cd restapi
sls deploy

# Scheduler
cd scheduler
chalice deploy

# WebSocket
cd websocket
chalice package --stage dev --merge-template resources.json out
aws cloudformation package  --template-file out/sam.json --s3-bucket $BUCKET --output-template-file out/template.yml
aws cloudformation deploy --template-file out/template.yml --stack-name ChaliceChat --capabilities CAPABILITY_IAM

# Worker
cd worker
chalice deploy
```

> 💡 **Deployment is automated via GitHub Actions**. Each service has its own workflow file under `.github/workflows/` and is triggered on push to `main` or via manual dispatch.

---

## 🧪 Testing

Each module is designed to be testable independently.
We recommend setting up a local testing workflow per service using `pytest`, `moto`, or AWS SAM local (if needed).
