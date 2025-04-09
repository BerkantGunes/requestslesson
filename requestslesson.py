import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text) #adres uzerinden gelen JSON bilgisini konsola yazdirir #json.loads ekleyerek type str den list donusturuldu
# list turune cevirdikten sonra istedigimiz bilgiye istedigimiz sekilde erisebildik!


print(result[0]["title"]) # response [200] cevabi basarili bir sonucun geldigini soyler # [] lari ekledikten sonra 1. kismin titleni konsola yazdirdi (delectus aut autem)
print(result[0]) # gelen JSON kaydi icinden sadece ilk olani konsola yazdirdi
print(type(result)) # gelen bilginin tipini yazdirdi ('str')


for i in result: # butun bilgileri satir satir yazdirmayi sagladi (dict turunde)
    print(i)


for i in result:
    print(i["title"]) # sadece title larin ciktisini verir


# filtreleyerek konsola yazdirmak icin (sadece userId'si 1 olan) kayitlari konsola yazdirir.
for i in result:
    if i["userId"] == 1:
        print(i["title"])
