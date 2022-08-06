from flight_fare.pipeline.pipeline import Pipeline
from flight_fare.exception import FareException
from flight_fare.logger import logging
from flight_fare.config.configuration import Configuration
import os

def main():
    try:
        #config_path = os.path.join("config","config.yaml")
        #pipeline = Pipeline(Configuration(config_file_path=config_path))
        ##pipeline.run_pipeline()
        #pipeline.start()
        #logging.info("main function execution completed.")

        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        print(e)

#if __name__ == "__main__":
 #   main()