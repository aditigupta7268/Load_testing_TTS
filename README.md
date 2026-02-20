## 🚀 Load Testing TTS Microservice using Locust

This project demonstrates performance and load testing of a Text-to-Speech (TTS) microservice using Locust.
The goal is to evaluate scalability, latency behavior, throughput, and system reliability under concurrent user traffic.

## 📌 Project Overview

Modern TTS systems often face:

Blocking API calls

File I/O bottlenecks

High latency under concurrent load

Poor observability under stress

This project benchmarks a TTS /generate endpoint under simulated concurrent users to analyze:

Response time distribution

Requests per second (RPS)

Failure rates

System stability

## 🛠️ Tech Stack

Python 3.11

FastAPI (TTS backend)

gTTS (Text-to-Speech engine)

Locust (Load testing framework)

Uvicorn / Gunicorn (ASGI server)

📂 Project Structure
```
Load_testing_TTS/
│
├── locustfile.py        # Locust load test script
├── requirements.txt     # Project dependencies
├── README.md            # Documentation
```
## ⚙️ Installation

```
Clone the repository:

git clone https://github.com/aditigupta7268/Load_testing_TTS.git
cd Load_testing_TTS

Install dependencies:

pip install -r requirements.txt
## ▶️ Running the TTS Server

Make sure your FastAPI TTS backend is running:

uvicorn main:app --reload

Default host:

http://localhost:8000
🧪 Running Load Test with Locust

Start Locust:

locust -f locustfile.py

Open browser:

http://localhost:8089

Configure:

Number of Users (e.g., 100)

Spawn Rate (e.g., 10)

Host: http://localhost:8000

Click Start Swarming.
```

## 📊 Sample Test Results

From a test with:

👥 Users: 100

🚀 RPS: ~19.75

❌ Failures: 0%

Observations:

Median Response Time: 11 ms

95th Percentile: 2400 ms

99th Percentile: 2700 ms

Average Response Time: 665 ms

System remained stable under concurrent load

This indicates:

High tail latency (likely due to blocking TTS processing)

No request failures

Stable throughput

## 📈 Performance Insights
Bottlenecks Identified

Synchronous TTS generation

File write operations

CPU-bound audio generation

Lack of background task queue

Potential Improvements

Use async background workers (Celery / RQ)

Introduce caching for repeated inputs

Stream audio instead of saving files

Add horizontal scaling (multiple workers)

Deploy with Gunicorn + multiple Uvicorn workers

Example production command:

gunicorn main:app -k uvicorn.workers.UvicornWorker -w 4

## 🎯 Learning Outcomes

Designed realistic load testing scenarios

Measured latency percentiles

Analyzed tail latency behavior

Evaluated system scalability under 100 concurrent users

Identified production-level optimizations
