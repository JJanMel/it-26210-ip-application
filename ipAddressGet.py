from requests import get


#This variable is used to get the ip from the user's computer
ip = get('https://ip.seeip.org/geoip').text

#This is used to print the ip and other information
print ('My public IPv4 address and a few more bits of information: {}'.format(ip))
