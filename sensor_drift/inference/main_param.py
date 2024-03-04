#####################################
# PARAMETERS #
#####################################

# This file selects the location, start and end datetime of data to be used in the inference step. Only fill lines up to 18.
# senid is the location as recorded in the column [Location_code] in the view etdl_curated.measurement. Only use locations listed there. 
# start date is the  date in the format 'yyyy-mm-dd' where the inference should start.
# end date is the  date in the format 'yyyy-mm-dd' where the inference should end.
# prm is the water quality parameter to be labeled. Please use one of the following options: 'cond' for electrical conductivity, 'temp' for water temperature and 'ph' for pH.
# the variables dir, id and folder define the location of the source data, in case they need to be changed.
# logged_model_arima is the runid of the arima model to be used when combining several models. For example in logged_model = 'runs:/e44451c9d9c841f885ed505b5b799c56/model' the runid is 'e44451c9d9c841f885ed505b5b799c56. Run ids can be found in Experiments/sensor_drift_training when clicking in a run name.


senid = 'firebund2'
start_date = '2019-01-01'
end_date = '2020-01-01'
prm = ['cond']


logged_model_arima = 'ec0a24fbe9d6485c8e377fb7ee1f2a4c'