#####################################
# PARAMETERS #
#####################################
# This file assigns parameters for the steps of the sensor drift workflow. You can modify relevant parameters in lines 17-35. Calibration and site parameters can also be modified. Refer to the UAT guide for more information about this topic.

# Choosing your station and location
# Select the location (senid), start and end dates (start_date and end_date) and water quality measurement('cond' for electrical conductivity, 
#'ph' for pH and 'temp' for water temperature. senid should be sourced from the column [Location_code] in the view etdl_curated.measurement.

senid = 'wqm7_WP81'
start_date = '2009-01-01'
end_date = '2010-01-01'
prm = ['cond']

# Choosing the model parameters: Experiment with the model parameters for arima and lstm. Examples are given below as guidelines.

#For arima:
    
pdq_ec = [3,5,10]
pdq_temp = [1,1,3]
pdq_ph = [5,1,2]
pdq_do = [5,1,2]


# Location of source file

dir = 'userupload'
id = 'etdl'
folder = 'sensor_drift'

#END OF USER INPUTS
##########################################################

# The following describes the parameters generally:
#   max_range, min_range, persist are used for rules based anomaly detection.
#   window_sz, alpha, threhsold_min are used in determining the dynamic threshold.
#   widen is the widening factor.
#   pdq are ARIMA hyper parameters.

from dataclasses import dataclass

@dataclass
class Sensors:
   start_date: str
   end_date: str
   senid: str = None
   prm: list = None

senid= Sensors(senid = senid, start_date = start_date,
end_date = end_date, prm = prm)
    

# CALIBRATION PARAMETERS #
#########################################

@dataclass
class CalibrationParameters:
    hour_low: int
    hour_high: int
    persist_low: int = None
    persist_high: int = None


calib_params = CalibrationParameters(hour_low=7,
                                     hour_high=17,
                                     persist_low=3,
                                     persist_high=7)



# SITE AND SENSOR SPECIFIC PARAMETERS
#########################################

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


site_params = {
    'East Trinity': {
        'temp' : Parameters(max_range=40,
                           min_range=10,
                           persist=120, #before it was 30
                           window_sz=30,
                           alpha=0.0001,
                           threshold_min=0.25,
                           widen=1,
                           pdq= pdq_temp),
        'cond' : Parameters(max_range=70,
                            min_range=0.03,
                            persist=30,
                            window_sz=30,
                            alpha=0.0001,
                            threshold_min=10.0,
                            widen= 10,
                           pdq = pdq_ec), 
        'ph' : Parameters(max_range=10,
                          min_range=3,
                          persist=15,
                          window_sz=30,
                          alpha=0.00001,
                          threshold_min=1,
                          widen=1,
                          pdq=pdq_ph),
        'do' : Parameters(max_range=30,
                          min_range=2,
                          persist=45,
                          window_sz=30,
                          alpha=0.0001,
                          threshold_min=0.15,
                          widen=1,
                          pdq=pdq_do)},
}

