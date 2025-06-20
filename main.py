from USED_CAR_PREDICTION import logger
from USED_CAR_PREDICTION.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from USED_CAR_PREDICTION.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from USED_CAR_PREDICTION.pipeline.stage_03_model_training import  ModelTrainingPipeline
from USED_CAR_PREDICTION.pipeline.stage_04_Model_evaluation_with_Mlflow import   EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = "Prepare Base Model"



try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training"


try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"


try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


