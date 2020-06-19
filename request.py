import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'umur':1, 'jantina':2, 'institusi':1, 'program':4,
	'mod_pengajian':1, 'cgpa_t1':1, 'taraf_perkahwinan':1, 'tajaan':4, 'kelayakan_masuk':2})

print(r.json())