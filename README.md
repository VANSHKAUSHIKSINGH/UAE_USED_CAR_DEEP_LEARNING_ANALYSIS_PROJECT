# 🏎️🚗🚘🚙UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT


### Workflows

1. Update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
0. Update the dvc.yaml
10. app.py


# How to run?

### STEPS:

clone the repository

```bash
https://github.com/VANSHKAUSHIKSINGH/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT/tree/main
```

### STEP 01 - Create a conda environment after opening the repository


```bash/(cmd terminal in vscode)
conda create -p usedcarDP python==3.8.5 -y
```

```bash
conda activate usedcarDP
```



### STEP 02 - install the requirements

```bash/cmd/(cmd terminal in vscode)
pip install -r requirements.txt
```


# Finally run the following command
python app.py

Now,

open up you local host and port



### MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)



##### cmd

- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = https://dagshub.com/DevilKaushik/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT.mlflow \
MLFLOW_TRACKING_USERNAME=DevilKaushik \
MLFLOW_TRACKING_PASSWORD = d78d49d4af46e838795bd66d175b97a5ccdf0079 \
python script.py


Run this to export as env variables:

### - If we use in macOS and Linux, we use export.
```bash

export MLFLOW_TRACKING_URI = https://dagshub.com/DevilKaushik/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT.mlflow

export MLFLOW_TRACKING_USERNAME=DevilKaushik

export MLFLOW_TRACKING_PASSWORD = d78d49d4af46e838795bd66d175b97a5ccdf0079

```

### - If we use Window, we use set.
```bash
set MLFLOW_TRACKING_URI = https://dagshub.com/DevilKaushik/UAE_USED_CAR_DEEP_LEARNING_ANALYSIS_PROJECT.mlflow

set MLFLOW_TRACKING_USERNAME=DevilKaushik

set MLFLOW_TRACKING_PASSWORD = d78d49d4af46e838795bd66d175b97a5ccdf0079

```



