import json
import csv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
#este se ejecuta de cuarto

authenticator = IAMAuthenticator('gcZmVQqg0TlzEh03qurbQAYxqE-rxgJ52K3j6HowVGX-')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/aa50adf8-dedb-45a1-b858-c4ac497ecb8c')

row_count = 0    
with open('./normal.csv', 'rt',encoding="utf8") as f:
    row_count = sum(1 for row in f)
    print(row_count)

f.close()

with open('./normal.csv', 'rt',encoding="utf8") as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    for i in range(1, row_count):
        print(i)
        texto = mycsv[i][1]
        response = natural_language_understanding.analyze(
        text=texto,
        features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=30,language="spanish"))).get_result()
        
        out_file = open('./jsons/res'+str(i)+'.json', "w")
        json.dump(response, out_file, indent=2)
        out_file.close() 