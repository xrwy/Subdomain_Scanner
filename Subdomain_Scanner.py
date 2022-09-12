from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def main():
	return render_template('subdomain.html')

@app.route('/domain_name_result', methods = ['GET','POST'])
def subDomainResult():
	requestResults_ = []
	if request.method == 'POST':
		domain_name = request.form['domain_name']
		if domain_name == '':
			return 'Do not leave the fields blank'

		with open('Subdomain_Names.txt','r') as file:
			name = file.read()
			sub_dom = name.splitlines()

		requestResults_ = domainScanner(domain_name,sub_dom)
	
		if len(requestResults_) == 0:
			requestResults_ = 0
		else:
			pass
		
		return render_template('subdomain_result.html', requestResults = requestResults_)

	else:
		return 'For post requests only.'

def domainScanner(domainName,subDomNames):
	requestResults = []
	for subDomain in subDomNames:
		url = 'https://{0}.{1}'.format(subDomain, domainName)
		try:
			requests.get(url)
			res = '[+] {0}'.format(url)
			requestResults.append(res)

		except requests.ConnectionError:
			pass

	return requestResults


if __name__ == '__main__':
	app.run(debug=True, port=5000)
