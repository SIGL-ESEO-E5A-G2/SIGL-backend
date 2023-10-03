# Setting up the venv
## Create a virtual environment
First things first, create a virtual environment with `virtualenv`. (If not installed install with `pip install virtualenv`.)   
Create a new virtual environment with the following command in terminal.

``` sh
virtualenv venv  # Specify python version if multiple installed
```

this will create a new folder `venv`. Now activate the environment with following command (faite ça dès que vous voulez travailler avec le back):
Windows:

```sh
.\venv\Scripts\activate
```

linux:

```sh
source ./venv/bin/activate
```

## Install Dependencies (on ne sait jamais, normalement le conteneur à tout)
```sh
pip install --no-cache-dir -r requirements.txt
```