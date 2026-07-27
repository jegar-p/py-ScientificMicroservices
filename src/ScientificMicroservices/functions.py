import json
import requests
# import numpy as np

__all__ = ["ABSynthesis", "MissingRowsCols", "MissingBias", "DetectOutliers", "MissingGraph"]

def ABSynthesis(email, key, data_dict):
    '''
    Run a meta-analysis on a set of experiments to determine the summary uplift and p-value.
    Takes a list of dicts containing at least four keys:
        successes_base: The number of events of interest (e.g. clicks) in the base condition, 1 element for each experiment.
        trials_base: The full number of people (e.g. visitors) who saw the base condition.
        successes_variant: The number of events of interest (e.g. clicks) in the variant condition, 1 element for each experiment.
        trials_variant: The full number of people (e.g. visitors) who saw the variant condition.
    '''
    Headers = {'email':email, 'key':key, 'content_type':"application/json" }
    Body  = json.dumps(data_dict)
    return requests.post(url = "https://api.scientificmicroservices.com/absynthesis", data = Body, headers=Headers).json()

def MissingRowsCols(email, key, data_dict):
    '''
    Return a report of the missing values in a dataset
    Takes a list of dicts or a pandas table.
    '''
    Headers = {'email':email, 'key':key, 'content_type':"application/json" }
    
    cls = type(data_dict)
    if cls.__name__ == 'DataFrame' and cls.__module__.startswith('pandas'):
        # Convert pandas data frames for use in the api, as this is a common use case. 
        cleaned_df = data_dict.replace({float('nan'): None})
        cleaned_df = cleaned_df.to_dict(orient='records')
        Body  = json.dumps(cleaned_df)
    else:
        Body  = json.dumps(data_dict)
    
    return requests.post(url = "https://api.scientificmicroservices.com/missingrowscols", data = Body, headers=Headers).json()

def MissingBias(email, key, array_pair_dict):
    '''
    Determine whether missing data in one column of a table is more likely depending on a second column.
    Takes a two column pandas table, or a list of dicts containing two key-value pairs each.
    '''
    Headers = {'email':email, 'key':key, 'content_type':"application/json" }
    Body  = json.dumps(array_pair_dict)
    return requests.post(url = "https://api.scientificmicroservices.com/missingbias", data = Body, headers=Headers).json()

def DetectOutliers(email, key, array_dict):
    '''
    Detect unusual values in a list based on three common statistical tests.
    Takes a list of values that can be strings or numbers.
    '''
    Headers = {'email':email, 'key':key, 'content_type':"application/json" }
    Body  = json.dumps(array_dict)
    return requests.post(url = "https://api.scientificmicroservices.com/detectoutliers", data = Body, headers=Headers).json()

def MissingGraph(email, key, data_dict):
    '''
    Return a graph of the missing values in a dataset
    Takes a list of dicts or a pandas table.
    '''
    Headers = {'email':email, 'key':key, 'content_type':"application/json" }
    
    cls = type(data_dict)
    if cls.__name__ == 'DataFrame' and cls.__module__.startswith('pandas'):
        # Convert pandas data frames for use in the api, as this is a common use case. 
        cleaned_df = data_dict.replace({float('nan'): None})
        cleaned_df = cleaned_df.to_dict(orient='records')
        Body  = json.dumps(cleaned_df)
    else:
        Body  = json.dumps(data_dict)
    
    response = requests.post(url = "https://api.scientificmicroservices.com/missinggraph", data = Body, headers=Headers)
    response.raise_for_status()
    return response.content