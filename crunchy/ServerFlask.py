from flask import Flask, render_template , jsonify ,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.triangle import Triangle
from bson import json_util
import json

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['crunchy']
overView = db['overView']

app = Flask(__name__)
Triangle(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET', 'POST'])
def displayGraph():
	return render_template('index.html')

@app.route('/getDataForScatterPlot/', defaults={'column': None})
@app.route('/getDataForScatterPlot/<column>')
def Data(column):
	if(column == None):
		return "Column not specified"
	else:
		content = list(overView.find({},{'_id': 0,'date': 1,'count.'+column:1}))
		content1 = []
    		for x in content:
        		content1.append([x['date'] , x['count'][column]])
    		#return render_template('test.html', content=json_util.dumps(content1))
		return json_util.dumps(content1)

if __name__ == '__main__':
  app.debug = True
  app.run(debug=True)
