class ConfigurationErrorException(Exception):
    def __init__(self, message):
        Exception.__init__(self, 'ConfigurationException: ' + message)
