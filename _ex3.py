import requests
print('Selamat datang, mau tahu berita apa hari ini?')
listBerita = ['Berita seputar teknologi','Berita seputar bisnis','Berita seputar olahraga','Berita seputar kesehatan','Berita seputar science']
for elem in listBerita:
    print('[',listBerita.index(elem) + 1,']', elem)

url1 = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=d74795ff6074428dbef4ae2c2cd2b1c9'
url2 = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=d74795ff6074428dbef4ae2c2cd2b1c9'
url3 = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=d74795ff6074428dbef4ae2c2cd2b1c9'
url4 = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=d74795ff6074428dbef4ae2c2cd2b1c9'
url5 = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=d74795ff6074428dbef4ae2c2cd2b1c9'
cathegory = ['technology','business', 'sports', 'health', 'science']
listurl = [url1, url2, url3, url4, url5]

urlinput = int(input('Ketik pilihan anda [1/2/3/4/5] : '))

data = requests.get(listurl[urlinput-1])
output = data.json()

print('')
print('Berikut adalah top 5 berita Indonesia bidang', cathegory[urlinput-1], ':')
for x in range(0,5,1):
	print(x+1, output['articles'][x]['title'])