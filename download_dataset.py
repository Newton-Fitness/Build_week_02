#import urllib2
from urllib.request import urlopen
import os
import tarfile
import shutil
import glob

# Constant
dataset_dir = './TransportationData'
datasetBalanced = dataset_dir + '/datasetBalanced'
rawOriginaldata = dataset_dir + '/_RawDataOriginal'
url_list = ['http://cs.unibo.it/projects/us-tm2017/static/dataset/extension/5second/dataset_5secondWindow.csv',
			'http://cs.unibo.it/projects/us-tm2017/static/dataset/extension/halfsecond/dataset_halfSecondWindow.csv',
			'http://cs.unibo.it/projects/us-tm2017/static/dataset/raw_data/raw_data.tar.gz']
dataset5second = 'dataset_5secondWindow.csv'
datasethalfsecond = 'dataset_halfSecondWindow.csv'
rawdataorig = "raw_data.tar.gz"
url1= 'http://cs.unibo.it/projects/us-tm2017/static/dataset/extension/5second/dataset_5secondWindow.csv'
url2= 'http://cs.unibo.it/projects/us-tm2017/static/dataset/raw_data/raw_data.tar.gz'
url3= "http://cs.unibo.it/projects/us-tm2017/static/dataset/raw_data/raw_data.tar.gz"

if __name__ == "__main__":
	# create folders
	if not os.path.exists(dataset_dir):
		os.makedirs(dataset_dir)

	if not os.path.exists(datasetBalanced):
		os.makedirs(datasetBalanced)

	if not os.path.exists(rawOriginaldata):
		os.makedirs(rawOriginaldata)

	print("DOWNLOAD........")
	for url in url_list:
		response = urlopen(url)
		csv = response.read()
		if url == url1:
			outfile = datasetBalanced + '/' + dataset5second
		elif url == url2:
			outfile = rawOriginaldata + '/' + rawdataorig
		else:
			outfile = datasetBalanced + '/' + datasethalfsecond

		with open(outfile, 'wb') as f:
			f.write(csv)

		if url == url3:
			tar = tarfile.open(outfile, "r:gz")
			tar.extractall(path="TransportationData/")
			tar.close()
			for filename in glob.iglob('TransportationData/raw_data/*/*.csv'):
				shutil.move(filename, rawOriginaldata)
			os.remove(outfile)
			shutil.rmtree('TransportationData/raw_data/')

	print("DOWNLOAD ENDED.")
