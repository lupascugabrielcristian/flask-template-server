import os
import configparser

class ConfigurationsService:
    configurations = None
    cwd = ""

    """ creates a singleton object, if it is not created, or else returns the previous singleton object"""
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(ConfigurationsService, self).__new__(self)
        return self.instance


    def __init__(self):
        self.cwd = os.getcwd() 
        self.configurations = self.read_configurations()

    def read_configurations(self):
        config = configparser.ConfigParser()

        configuration_file_path = self.cwd + '/configs/all.ini' 
        if not os.path.exists(configuration_file_path):

            # Daca nu gasesc in cwd caut dupa ~ directory
            configuration_file_path = os.path.expanduser('~') + "/bubble-server/configs/all.ini"

            if not os.path.exists(configuration_file_path):
                raise Exception("configuration file all.ini not found at " + configuration_file_path)
                print("Configurations file not found")
            else:
                self.cwd = os.path.expanduser('~') + "/bubble-server"

        # pentru local aici ar trebuie sa fie adresa diferita
        config.read(configuration_file_path)
        # pentru remote:
        #config.read('/root/statistici/configs/all.ini')

        return config

    def get_configurations(self):
        return self.configurations

    def db_name(self):
        return self.configurations['Connection']['database_name']

    def db_pass(self):
        return self.configurations['Connection']['database_password']

    def db_user(self):
        return self.configurations['Connection']['database_user']
