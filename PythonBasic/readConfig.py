import os
from configparser import  ConfigParser

class ConfigReader():

    config = ConfigParser()

    def readConf(self):
        print(os.getcwd())
        # Get current working directory
        current_directory = os.getcwd()
        # Get the root folder name
        root_folder_name = os.path.basename(current_directory)
        # Remove the root folder name from the path
        parent_directory = current_directory.rstrip(root_folder_name)
        print("Parent Directory:", parent_directory)
        self.config.read(parent_directory+"data/Config.cfg")
        print(self.config.get("section1","username"))
        print(self.config.get("section1", "password"))


obj=ConfigReader()
obj.readConf()



