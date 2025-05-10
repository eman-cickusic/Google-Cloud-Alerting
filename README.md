# Google Cloud Alerting

This repository contains a sample application and configuration files demonstrating how to set up alerting in Google Cloud. The project shows how to deploy a simple Python Flask application to App Engine and create alerting policies to monitor its performance and availability.

## Overview

In this project, you'll learn how to:
- Deploy a Python Flask application to Google Cloud App Engine
- Create uptime checks and alerts in Google Cloud Monitoring
- Create an alerting policy using both the Google Cloud Console and CLI
- Test alerting policies by simulating latency and errors in the application

## Prerequisites

- A Google Cloud Platform account with billing enabled
- Google Cloud SDK (gcloud) installed
- Python 3.12 installed

## Video

https://youtu.be/_enf0RujnLc


## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/google-cloud-alerting.git
cd google-cloud-alerting
```

### 2. Set up your Python environment

```bash
python3 -m pip install --upgrade pip
python3 -m venv myenv
source myenv/bin/activate
pip install -r app/requirements.txt
```

### 3. Test the application locally

```bash
cd app
python main.py
```

The application should be accessible at http://localhost:8080

### 4. Deploy to App Engine

Create an App Engine application (only needed once per project):

```bash
gcloud app create --region=REGION
```

Deploy the application:

```bash
gcloud app deploy --version=one --quiet
```

## Creating Alerting Policies

### Console Method

1. Navigate to Monitoring > Alerting in the Google Cloud Console
2. Click "Create Policy"
3. Select the appropriate metrics:
   - For latency: GAE Application > Http > Response latency
   - Configure thresholds and notification channels

### CLI Method

Deploy the alerting policy using gcloud:

```bash
cd alerting
gcloud alpha monitoring policies create --policy-from-file="app-engine-error-percent-policy.json"
```

## Testing Alerting Policies

### Testing Latency Alert

Modify `main.py` to include a delay:

```python
@app.route("/")
def main():
    model = {"title": "Hello GCP."}
    time.sleep(10)  # 10-second delay
    return render_template('index.html', model=model)
```

### Testing Error Alert

Modify `main.py` to generate random errors:

```python
@app.route("/")
def main():
    num = random.randrange(49)
    if num == 0:
        return json.dumps({"error": 'Error thrown randomly'}), 500
    else:
        model = {"title": "Hello GCP."}
        return render_template('index.html', model=model)
```

Generate load to trigger alerts:

```bash
while true; do curl -s https://YOUR_PROJECT_ID.appspot.com/ | grep -e "<title>" -e "error"; sleep .$[( $RANDOM % 10 )]s; done
```

## Files Description

- `app/main.py`: The Flask application
- `app/requirements.txt`: Python dependencies
- `app/app.yaml`: App Engine configuration
- `app/templates/index.html`: HTML template for the app
- `alerting/app-engine-error-percent-policy.json`: Alerting policy configuration

## Resources

- [Google Cloud App Engine Documentation](https://cloud.google.com/appengine/docs)
- [Google Cloud Monitoring Documentation](https://cloud.google.com/monitoring/docs)
- [Alerting Policies Documentation](https://cloud.google.com/monitoring/alerts)
