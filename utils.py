import datetime

def get_param_to_date_time_frame(days: int = 7) -> tuple:
    ''' 
    Get the the start and end date of the time frame.
    :param days: number of days to go back
    :return: start_date, end_date in string format YYYY-MM-DD 
    '''
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=days)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
