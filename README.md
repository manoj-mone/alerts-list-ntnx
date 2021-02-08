# Alerts List in HTML and CSV for Nutanix

## Introduction
This app generates a HTML and CSV list of all alerts generated in your Nutanix cluster. The data has been gathered using the Nutanix v2 API alerts endpoint. It is cleaned and structured using pandas.


## Requirements

We recommend you to create a separate virtual environment running Python 3 for this app, and install all of the required dependencies there. 

Run in Terminal/Command Prompt:

```
git clone https://github.com/manoj-mone/alerts-list-ntnx.git
cd alerts-list-ntnx/
python3 -m pip install virtualenv
python3 -m virtualenv venv
```
In UNIX system:

```source venv/bin/activate```

In Windows:

```venv\Scripts\activate```

To install all of the required packages to this environment, simply run:

```pip install -r requirements.txt```

and all of the required pip packages, will be installed, and the app will be able to run.


## How to use this app

You have to specify the Nutanix cluster that you wish to connect to before running the app.

To do so, open the `alerts-list-ntnx/request.py` file using a common text editor like Sublimetext or vim. An example is shown in the file as well. You will have to just replace the IP address of the cluster and the credentials you would use to login as well. Save and quit from the file.

After this you could run this app 

Run the app

```python alerts-list.py```

Two files will get generated in the alerts-list-ntnx folder -
    1. alerts_data.csv
    2. alerts_data.html
    

## License
[MIT](https://choosealicense.com/licenses/mit/)
