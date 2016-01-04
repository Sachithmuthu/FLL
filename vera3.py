import urllib2

while(1):

	key = input('Type: ')

	if(key==0):
		url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=4&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0')

	if(key==1):
		url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=4&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=1')


	if(key==2):
		url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=5&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0')

	if(key==3):
		url_response = urllib2.urlopen('http://192.168.81.1:3480/data_request?id=lu_action&output_format=json&DeviceNum=5&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=1')