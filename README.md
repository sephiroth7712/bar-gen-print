# bar-gen-print
A flask application to generate and send commands to connected printers to print the barcode.

# Index
+ [Installation](#installation)
+ [Getting Started with the Application](#gswta)
+ [Modules Used](#modules)

## Installation<a name="installation"></a>
### Running Locally
Make sure you have [python-2.7.15](https://www.python.org/downloads/release/python-2715/) and [pip](https://pypi.org/project/pip/) installed.
1. Clone or download the repository 
```
	$ git clone https://github.com/sephiroth7712/bar-gen-print.git
	$ cd bar-gen-print
```
2. Install Dependencies
```
	$ pip install -r requirements.txt
```

3. Start the application
```
	$ gunicorn app:app
```

Your app server should now be running locally.

## Modules Used<a name="modules"></a>
1. [svgwrite](https://pypi.org/project/svgwrite/)
2. [Flask](http://flask.pocoo.org/)
3. [pyBarcode](https://pypi.org/project/pyBarcode/)
4. [Werkzeug](http://werkzeug.pocoo.org/)




## Getting Started with the Application<a name="gswta></a>
### Generating a barcode
1. Run the application to start the app server
```
  $gunicorn app:app
```
2. Go to link [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
3. Choose the barcode format
4. Enter value of the barcode and click on submit to view the generated barcode.


# Project is still under development and as such the Readme will be updated.
