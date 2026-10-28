# Titanic Survival Prediction — MLOps Pipeline

A machine learning project that predicts whether a passenger survived the Titanic disaster. The project covers model training, model persistence, API serving with FastAPI, containerization with Docker, and automated testing with GitHub Actions.

## Dataset and Source

- **Dataset:** Titanic — Machine Learning from Disaster
- **Source:** Kaggle's official Titanic competition
- **Dataset page:** https://www.kaggle.com/competitions/titanic/data
- **Competition overview:** https://www.kaggle.com/competitions/titanic

The dataset contains passenger information such as passenger class, sex, age, number of siblings/spouses aboard, number of parents/children aboard, fare, and port of embarkation. The target column is `Survived` (`0` = did not survive, `1` = survived).

### Getting the dataset

1. Open the [Kaggle Titanic data page](https://www.kaggle.com/competitions/titanic/data).
2. Sign in to Kaggle and accept the competition rules if prompted.
3. Download the dataset files, including `train.csv` and `test.csv`.
4. Use `train.csv` for model training and validation in Jupyter Notebook or Google Colab.

**Dataset attribution:** The data is provided through Kaggle's Titanic competition. Review the competition page for its current terms and data-use details.

## Project Workflow

1. Downloaded the Kaggle Titanic dataset.
2. Trained and evaluated a machine learning model in Google Colab/Jupyter.
3. Saved the preprocessing and prediction pipeline as `models/model.joblib`.
4. Loaded the saved pipeline in a FastAPI application.
5. Tested the API endpoints locally.
6. Packaged the API and model in a Docker image.
7. Added automated tests and a GitHub Actions CI workflow.

## Tech Stack

- Python
- pandas and NumPy
- scikit-learn
- joblib
- FastAPI
- Uvicorn
- Docker
- pytest
- GitHub Actions

## Repository Structure

```text
titanic-mlops-pipeline/
├── models/
│   └── model.joblib
├── main.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_api.py
└── .github/
    └── workflows/
        └── ci.yaml
```

The `tests/`, `Dockerfile`, and workflow paths above describe the intended project layout; adjust them if your repository uses different filenames or locations.

## Run Locally

### 1. Create and activate a virtual environment (recommended)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

The saved scikit-learn model should be loaded with a compatible scikit-learn version. The project requirements pin `scikit-learn==1.6.1` to match the version used when the model was saved.

### 3. Start the API

```powershell
python -m uvicorn main:app --reload
```

Open these URLs in your browser:

- API root: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

If your application implements a `/health` endpoint, you can also test `http://127.0.0.1:8000/health`.

## Test the Prediction API

In the Swagger UI at http://127.0.0.1:8000/docs:

1. Expand `POST /predict`.
2. Select **Try it out**.
3. Submit a JSON request such as:

```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

A successful request should return HTTP `200` and a JSON response containing a numeric `prediction` and a `survival_status`, for example:

```json
{
  "prediction": 0,
  "survival_status": "Did not survive"
}
```

The exact prediction depends on the saved model and input values.

## Run with Docker

Make sure Docker Desktop is running before using Docker commands.

### Build the image

Run these commands from the repository root, where the `Dockerfile` is located:

```powershell
docker build -t titanic-survival-api .
```

### Start the container

```powershell
docker run -d --name titanic-api -p 8000:8000 titanic-survival-api
```

Then visit http://127.0.0.1:8000/docs and test `POST /predict` while the container is running.

Useful Docker commands:

```powershell
docker images
docker ps
docker ps -a
docker logs titanic-api
```

Stop and remove the container when finished:

```powershell
docker stop titanic-api
docker rm titanic-api
```

If a container named `titanic-api` already exists, remove it before creating another container with the same name.

## Run Tests

If the repository contains pytest tests, run:

```powershell
python -m pip install pytest httpx
python -m pytest -v
```

## Continuous Integration

GitHub Actions runs the configured CI workflow when changes are pushed to the repository. The workflow installs dependencies and runs automated tests. Check the **Actions** tab in GitHub to view workflow results:

https://github.com/SanidhyaSingh0604r/titanic-mlops-pipeline/actions

## GitHub Repository

https://github.com/SanidhyaSingh0604r/titanic-mlops-pipeline

## Notes

- This project is for educational and demonstration purposes.
- Model predictions are estimates and should not be treated as historical certainty for an individual passenger.
- Keep the model artifact and dependency versions compatible. A model serialized with one scikit-learn version may not load reliably under a different version.
