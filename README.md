Script that pulls data from JSON or YAML and process it with a jinja2 template.

### Requirements

* Python 3.6
* [PyYAML](https://pypi.org/project/PyYAML/): Python YAML parser.
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/): Python template engine.


### Initialization
```shell
# install virtualenv
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv

# create virtualenv
virtualenv -p /usr/bin/python3 venv
source ./venv/bin/activate

# install requirements
pip3 install -r ./requirements.txt
```

# Run script
```shell
python3 config.py data_file.yaml template.j2 outputfile.txt
```
