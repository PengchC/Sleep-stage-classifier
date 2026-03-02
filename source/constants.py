from source import utils



class Constants(object):
    WAKE_THRESHOLD = 0.5  #
    REM_THRESHOLD = 0.35

    EPOCH_DURATION_IN_SECONDS = 30
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_DAY = 3600 * 24
    SECONDS_PER_HOUR = 3600
    VERBOSE = True
    CROPPED_FILE_PATH = utils.get_project_root().joinpath('outputs/cropped/')
    FEATURE_FILE_PATH = utils.get_project_root().joinpath('outputs/features/')
    LOWER_BOUND = -0.2
