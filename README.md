# qa_qc_aquatic_sensors

This repo showcases a demo of a solution implemented to detect periods where aquatic sensors are drifting. Sensor drift refers to the deviation of a sensor's reading over time, which can lead to inaccurate measurements. The code below is used in conjunction with other components of the Azure ecosystem, such as Data Factory and Blob Storage. The code in this repo is only showing what is run in Databricks.


- `sensor_drift_training.ipynb` and `sensor_drift_inference.ipynb` contain the main code for training a model to detect sensor drift (in the training notebook) and using that model to infer or predict sensor drift in new data (in the inference notebook).

- `sensor_drift_training_visualisation.ipynb` and `sensor_drift_inference_visualisation.py` are used for visualizing the results of the training and inference processes, respectively. This include the plots of sensor readings over time, showing where the model has detected potential drift.

- `sensor_utilities_training.ipynb` and `sensor_utilities_inference.ipynb` contain utility functions or procedures that are used in the training and inference notebooks. This include data cleaning functions, functions to calculate metrics for evaluating the model, etc.


### Sensor drift identification for water quality parameters from aquatic sensors

This project contains the files associated with the development work (identification of sensor drift in water quality measurements), and  interaction with it (model management).

## Prerequisites:

- Access to a Databricks service in the QESD platform (etdl-databricks-prd).
- Familiarity with the [Databricks Machine Learning interface](https://learn.microsoft.com/en-us/azure/databricks/workspace/unified-nav) and etdl-databricks-uat/prd
- Familiarity with model management in Databricks. See [here](https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/model-registry) for more information.

## Related files:

- Inference or classification/reclassification of water quality measurement data: To label/relabel data using the arima model already created/registered in the model registry ('Models' tab in Databricks).
Located in sensor_drift/inference
    - sensor_drift_inference: Databricks notebook that contains the source code that creates the models and corresponding results.
    - parameters_inference.py: File where user can select Location codes, start dates and end dates to use for training. Model hyperparameters should also be changed here. 
    - sensor_utilities_inference.py: File with functions to preprocess data.
    - requirements_inference.txt: File with dependencies to run the notebook sensor_drift_inference.ipynb.

- Use and management of current model. This use case is about training models to identify sensor drift in water quality measurements. The models are then registered and used for inference.

Located in sensor_drift/training
    - sensor_drift_training: Databricks notebook that contains the source code that creates the models and corresponding results.
    - parameters_training.py: File where user can select Location codes, start dates and end dates to use for training. Model hyperparameters should also be changed here. 
    - sensor_utilities_training.py: File with functions to preprocess data.
    - sensor_drift_training_visualisation: Databricks notebook to visualise detection after training.
    - requirements_training.txt: File with dependencies to run the notebook sensor_drift_training.ipynb.

## Main instructions:

These instructions assumes you are familiar with Databricks in etdl-databricks. This use case assumes a model (selected from Experiments or Registered Models) has been chosen. Users take the provided model (or one they have chosen) and run the notebook. The output of the notebook includes relabelled observations with 82 and 83 as stated in the workflow sketched in the flowchart at the end of this page.

### To use for model inference:


| Tasks | Instructions |
| -------- | ------- |
| Be able to login to a modelling workspace and select the required sensor drift model.  | Login into etdl-databricks-prd through portal.azure.com. Navigate to Workspace, then platform_repo/sensor_drift/inference.   |
|  Be able to apply a sensor drift model to pre-2019 data, by selecting a dataset/time period.| Open the file parameters_inference.py located in platform_repo/sensor_drift/ and follow instructions included there to select the location (senid), start and end dates (start_date and end_date) and water quality measurement ('cond' for electrical conductivity, 'ph' for pH and 'temp' for water temperature). Open the file sensor_drift_inference.ipynb located in platform/sensor_drift/inference and press 'Run all' located at the right upper corner of the screen. Wait for the notebook to finish. Then log into to etdl-synapse-prd and browse the view [etdl_curated].[sensor_drift_inference] to check results. Remember to get familiar with the automated data dictionary.  |
| Be able to have oversight/audit capabilities of the model, typically being able to inspect/visualise the model process at each stage, enabling step-through of the model pipeline.  | Users can access the 'Registered Models', select 'arima' in the column/field Name and visualise the results.  |
| Have access to an interface where they can view the proposed quality code changes.  Be able to commit the quality code changes and/or create new records. | If users are not satisfied with the results and the new labels created by this process, they can fill out the xlsx template available at lake-userupload/sensor_drift/override/ with the new labels and an automated pipeline will override the results to the view [etdl_curated].[sensor_drift_inference_override]. |
| Advise the modeller if the change/update succeeded or failed.  | A notification will be sent to the user to advise if the process was successful or not.  |
| Have access to an interface to view the committed changes and/or created records. They will be able to view where the change come from, when it was changed, from which model.  | Users can access the view [etdl_curated].[sensor_drift_inference_override] to check the results.  |

### To use for model experimentation/training:

| Tasks | Instructions |
| -------- | ------- |
| Be able to select an available model (registered or unregistered) and run a new experiment.  | Users can access the 'Registered Models', select 'arima' in the column/field Name and visualise the results.  |
| Be able to reconfigure the model run, e.g. feature selection, success metric, number of iterations/folds, percent of train/validate data. Have access to change the model parameters/hyper-parameters. | Login into etdl-databricks-prd through portal.azure.com. Navigate to Workspace, then platform_repo/sensor_drift/training. Open the file parameters_training.py located in platform_repo/sensor_drift/training and follow instructions there to include the location (senid), start and end dates (start_date and end_date) and water quality measurement ('cond' for electrical conductivity, 'ph' for pH and 'temp' for water temperature). These parameters must follow the formats included in the Synpase view etdl_curated.measurement. Also include p,d,q (parameters related to ARIMA). Open the file sensor_drift_training.ipynb located in platform_repo/sensor_drift/training and press Run all located at the right upper corner of the screen. Click 'yes' when prompted. If all commands were run correctly, open the 'Experiments' tab in Databricks and browse the results. You can find metrics of interest there.  | 
| Be able to test the model using a test dataset (a step usually reserved for the best-performing model, occurs after training/validation).| Users can modify the test dataset in the file parameters_training.py, by selecting different time periods and locations. |
| Be able to deploy a new model to production and de-register a registered model.| Once the user is satisfied with the results and a particular model or combination of models, the model is registered and the runid is replaced in the string 'logged_arima_model' and then used the notebook sensor_drift_inference.ipynb is run again. |


## Instructions to run the notebooks:

- Optional: To visualise the results, open the file sensor_drift_training_visualisation. Use Location_codes found in etdl_curated measurement and water quality measurements from these options ('pH', 'EC', 'WaterTemp').

- Once the user is satisfied with the results and a particular model or combination of models, the model is registered and then used in the next step (or use case).