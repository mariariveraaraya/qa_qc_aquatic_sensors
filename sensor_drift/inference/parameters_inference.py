# Import necessary modules and parameters
from main_param import senid, start_date, end_date, prm, logged_model_arima
import mlflow

# Get the run data from the logged ARIMA model
run_data_dict = mlflow.get_run(f'{logged_model_arima}').data.to_dictionary()

# Extract the p, d, and q parameters from the run data
p_ = int(run_data_dict['params']['p'])
q_ = int(run_data_dict['params']['q'])
d_ = int(run_data_dict['params']['d'])

# Combine the parameters into a list
pdq = [p_, d_, q_]

# Define directory and folder names
dir = 'userupload'
id = 'etdl'
folder = 'sensor_drift'

# Import the dataclass decorator from the dataclasses module
from dataclasses import dataclass

# Define a dataclass for sensor information
@dataclass
class Sensors:
   start_date: str
   end_date: str
   senid: str = None
   prm: list = None

# Create an instance of the Sensors class
senid = Sensors(senid = senid, start_date = start_date, end_date = end_date, prm = prm)

# Define a dataclass for the model
@dataclass
class model:
    logged_model: str = None

# Create an instance of the model class
logged_model = model(logged_model = logged_model_arima)

# Define a dataclass for calibration parameters
@dataclass
class CalibrationParameters:
    hour_low: int
    hour_high: int
    persist_low: int = None
    persist_high: int = None

# Create an instance of the CalibrationParameters class
calib_params = CalibrationParameters(hour_low=7, hour_high=17, persist_low=3, persist_high=7)

# Define a dataclass for LSTM parameters
@dataclass
class LSTMParameters:
    time_steps: int
    samples: int
    cells: int
    dropout: float
    patience: int

# Create an instance of the LSTMParameters class
LSTM_params = LSTMParameters(time_steps=20, samples=20000, cells=128, dropout=0.2, patience=6)

# Define a dataclass for site and sensor specific parameters
@dataclass
class Parameters:
    max_range: float = None
    min_range: float = None
    persist: int = None
    calib_threshold: float = None
    window_sz: int = None
    alpha: float = None
    threshold_min: float = None
    widen: int = None
    pdq: [int, int, int] = None

# Define a dictionary of site parameters
site_params = {
    'East Trinity': {
        'temp' : Parameters(max_range=40, min_range=10, persist=120, window_sz=30, alpha=0.0001, threshold_min=0.25, widen=1, pdq= pdq),
        'cond' : Parameters(max_range=70, min_range=0.03, persist=30, window_sz=30, alpha=0.0001, threshold_min=10.0, widen= 10, pdq=pdq),
        'ph' : Parameters(max_range=10, min_range=3, persist=15, window_sz=30, alpha=0.00001, threshold_min=1, widen=1, pdq=pdq),
        'do' : Parameters(max_range=30, min_range=2, persist=45, window_sz=30, alpha=0.0001, threshold_min=0.15, widen=1, pdq=pdq)
    }
}