from flight_fare.components.data_ingestion import DataIngestion
#from flight_fare.components.data_transformation import DataTransformation
from flight_fare.components.data_validation import DataValidation
#from flight_fare.components.model_trainer import ModelTrainer
#from flight_fare.components.model_evaluation import ModelEvaluation
#from flight_fare.components.model_pusher import ModelPusher
from flight_fare.exception import FareException
from flight_fare.logger import logging, get_log_file_name
import os,sys,uuid
from flight_fare.config.configuration import Configuration
from flight_fare.entity.artifact_entity import *
from flight_fare.entity.config_entity import *
import pandas as pd
from multiprocessing import Process
from threading import Thread
from datetime import datetime
from collections import namedtuple
from flight_fare.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
                                       "running_status", "start_time", "stop_time", "execution_time", "message",
                                       "experiment_file_path", "accuracy", "is_model_accepted"])





class Pipeline(Thread):
    experiment: Experiment = Experiment(*([None] * 11))
    experiment_file_path = None

    def __init__(self, config: Configuration ) -> None:
        try:
            os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path=os.path.join(config.training_pipeline_config.artifact_dir,EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")
            self.config = config

        except Exception as e:
            raise FareException(e, sys) from e


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise FareException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_pipeline_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()

        except Exception as e:
            raise FareException(e, sys) from e

    def run_pipeline(self):
        try:
            

            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            
            

        except Exception as e:
            raise FareException(e, sys) from e


    
