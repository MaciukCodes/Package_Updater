# Package\_Updater



### 

### \##Overview

To create a no package dependant script to help install updates.



### \##Features

* Lists out of date packages
* Allows a list of packages as input to remove from the updater 
* Updates provided packages to last released update (will adjust for customized versions later)



### \##Installation

Currently none only a file to be ran in python interpreter



### \##Usage

run the command:

C:\\projects > py p\_updater.py

from the directory you want to check the python packages from and having either the updater in that directory or the complete path to the Updater file.

Or

Import func\_update.py and use the functions accordingly.



### \##Future Plans

To add additional features including:

* improving modularity by converting it to a Python package.
* Allowing the user to select and deselect package versions.
* 

### \##Required Package

As this is intended to be run without any dependencies jupyter is there to manage the project, idna and six are being used to test with.

