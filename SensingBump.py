import requests

particle_url = 'https://api.particle.io/v1/events/bump?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1'

rsp = requests.get(url = particle_url)

print (rsp)
