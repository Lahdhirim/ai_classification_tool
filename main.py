import argparse

# Import config loaders and pipeline classes for each task
from src.config_loaders.processing_config_loader import processing_config_loader
from src.processing_pipeline import ProcessingPipeline

from src.config_loaders.training_config_loader import training_config_loader
from src.training_pipeline import TrainingPipeline

from src.config_loaders.testing_config_loader import testing_config_loader
from src.testing_pipeline import TestingPipeline

from src.config_loaders.tuning_config_loader import tuning_config_loader
from src.tuning_pipeline import TuningPipeline


if __name__ == "__main__":
    """
    Main script for running the AI Classification Tool in different operational modes.

    This script provides a command-line interface to perform various tasks related to data processing, model training, hyperparameter tuning, and testing.
    Depending on the selected mode, it loads the appropriate configuration and executes the corresponding pipeline.
    """

    # Parse command-line argument to determine which mode to run
    parser = argparse.ArgumentParser(description="AI Classification Tool")
    parser.add_argument("mode", choices=["process_data", "train", "test", "fine_tune"],
                        default="process_data", nargs="?", help="Choose mode: process_data, train, test or fine_tune")
    args = parser.parse_args()

    # Launch the appropriate pipeline based on the selected mode
    if args.mode == "process_data":
        # Load processing config and run data preprocessing pipeline
        processing_config = processing_config_loader(config_path="config/processing_config.json")
        processing_pipeline = ProcessingPipeline(config=processing_config)
        processing_pipeline.run()
    
    elif args.mode == "train":
        # Load training config and run model training pipeline
        training_config = training_config_loader(config_path="config/training_config.json")
        training_pipeline = TrainingPipeline(config=training_config)
        training_pipeline.run()
    
    elif args.mode == "test":
        # Load testing config and run model testing pipeline
        testing_config = testing_config_loader(config_path="config/testing_config.json")
        testing_pipeline = TestingPipeline(config=testing_config)
        testing_pipeline.run()
    
    elif args.mode == "fine_tune":
        # Load tuning config and run hyperparameter tuning pipeline
        tuning_config = tuning_config_loader(config_path="config/tuning_config.json")
        tuning_pipeline = TuningPipeline(config=tuning_config)
        tuning_pipeline.run()
    
    else:
        print("Invalid mode. Please choose 'process_data', 'train', 'test', or 'fine_tune'.")