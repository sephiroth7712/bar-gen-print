#!/usr/bin/env python
import barcode
import svgwrite
from flask import Flask, render_template, request, url_for
from werkzeug import secure_filename
from lib.barcode_generator import barcode_svg, generate_barcode
app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        text = request.form['cx']
        value  = request.form['r']
        format=request.form['barcode_format']
        return render_template( 'submit.html', svg=generate_barcode(text,value,format))
    elif request.method == 'GET':
        return render_template( 'submit.html' )

if __name__=='__main__':
    app.debug = True
    app.run(host= '192.168.0.133')
