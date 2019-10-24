import requests
import json
import sys

print("Running Endpoint Tester....\n")
address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
if address == '':
	address = 'http://localhost:5000'



#Making a POST Request - make a new puppy
print("Making a POST (creating a new puppy) request to /puppies...")
try:
	url = address + "/puppies?name=Fido&description=Playful+Little+Puppy"
	resp = requests.post(url)
	obj = json.loads(resp.text)
	print(obj)
	puppyID = obj['Puppy']['id']
	if resp.status_code != 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)

except Exception as err:
	print("Test 1 FAILED: Could not make POST Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully Made POST Request to /puppies")




#Making a GET Request - get all puppies
print("Making a GET Request for (all) /puppies...")
try:
	url = address + "/puppies"
	resp = requests.get(url)
	print(resp.text)
	if resp.status_code != 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)
except Exception as err:
	print ("Test 2 FAILED: Could not make GET Request to web server")
	print (err.args)
	sys.exit()
else:
	print ("Test 2 PASS: Succesfully Made GET Request to /puppies")




#Making GET Requests to /puppies/id - get a single puppy
print ("Making GET (get single puppy) requests to /puppies/id ")

try:
	id = puppyID
	url = address + "/puppies/%s" % id 
	resp= requests.get(url)
	print(resp.text)
	if resp.status_code!= 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)
	

except Exception as err:
	print("Test 3 FAILED: Could not make GET Requests to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Succesfully Made GET Request to /puppies/id")



#Making a PUT Request - update an existin gpuppy
print ("Making PUT (update) requests to /puppies/id ")

try:
	id = puppyID 

	url = address + "/puppies/%s?name=wilma&description=A+sleepy+bundle+of+joy" % id 
	resp = requests.put(url)
	print(resp.text)
	if resp.status_code != 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)

except Exception as err:
	print ("Test 4 FAILED: Could not make PUT Request to web server")
	print (err.args)
	sys.exit()
else:
	print ("Test 4 PASS: Succesfully Made PUT Request to /puppies/id")


#Making a DELETE Request
print ("Making DELETE requests to /puppies/id ... ")

try:
	id = puppyID
	url = address + "/puppies/%s" % id 
	resp = requests.delete(url)
	print(resp.text)
	if resp.status_code != 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)
	

except Exception as err:
	print ("Test 5 FAILED: Could not make DELETE Requests to web server")
	print (err.args)
	sys.exit()
else:
	print ("Test 5 PASS: Succesfully Made DELETE Request to /puppies/id")
	print ("ALL TESTS PASSED!!")

#Making a PUT Request - update an existin gpuppy
print ("Making PUT (update) requests to /puppies/id ")

try:
	id = puppyID 

	url = address + "/puppies/%s?name=wilma&description=A+sleepy+bundle+of+joy" % id 
	resp = requests.put(url)
	print(resp.text)
	if resp.status_code != 200:
		raise Exception('Received an unsuccessful status code of %d' % resp.status_code)

except Exception as err:
	print ("Test 4 FAILED: Could not make PUT Request to web server")
	print (err.args)
	sys.exit()
else:
	print ("Test 4 PASS: Succesfully Made PUT Request to /puppies/id")
