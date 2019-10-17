# API Rest in Flask

## This is a sample of HelloWorld 

### Python virtual environment

Install a [Python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments).
Run the following to set up and activate a new virtual environment:

```bash
python2.7 -m virtualenv env
source env/bin/activate
```

### Pip


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies


```bash
pip install -r requirements.txt
```

### Run local

```bash
python main.py
```

### Test

curl -X POST \
  http://localhost:8000/hello \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "[YOUR NAME HERE]"
}'
