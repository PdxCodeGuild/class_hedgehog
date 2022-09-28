from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render (request, 'pep_app/index.html')

def examiner(request):
        state_id = request.POST.get('states', None)
        # print(request.POST.get('states'))
        data = {
            "isInternal":False,"countryId":184,"pageModel":{"first":0,"rows":1200,"sortOrder":1,"filters":{},"globalFilter":None},"selectedFunctionCodes":[{"id":1155,"functionCode":"DPE-PE-ASEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":185,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1156,"functionCode":"DPE-CIRE-ASEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":186,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1157,"functionCode":"DPE-ATPE-ASEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":187,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1158,"functionCode":"DPE-PE-AMEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":188,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1159,"functionCode":"DPE-CIRE-AMEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":189,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1160,"functionCode":"DPE-ATPE-AMEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":190,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1161,"functionCode":"DPE-PE-ASES","functionCodeDescription":None,"authorizationName":None,"sortOrder":191,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1162,"functionCode":"DPE-CIRE-ASES","functionCodeDescription":None,"authorizationName":None,"sortOrder":192,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1163,"functionCode":"DPE-ATPE-ASES","functionCodeDescription":None,"authorizationName":None,"sortOrder":193,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1164,"functionCode":"DPE-PE-AMES","functionCodeDescription":None,"authorizationName":None,"sortOrder":194,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1165,"functionCode":"DPE-CIRE-AMES","functionCodeDescription":None,"authorizationName":None,"sortOrder":195,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1166,"functionCode":"DPE-ATPE-AMES","functionCodeDescription":None,"authorizationName":None,"sortOrder":196,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1167,"functionCode":"DPE-TYPE-XXXX","functionCodeDescription":None,"authorizationName":None,"sortOrder":197,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":True,"selectedTypeRatings":[],"typeId":None},{"id":1168,"functionCode":"DPE-PPE-XXXX","functionCodeDescription":None,"authorizationName":None,"sortOrder":198,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":True,"selectedTypeRatings":[],"typeId":None},{"id":1326,"functionCode":"DPE-SPE-ASES","functionCodeDescription":None,"authorizationName":None,"sortOrder":332,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1327,"functionCode":"DPE-SPE-ASEL","functionCodeDescription":None,"authorizationName":None,"sortOrder":333,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1328,"functionCode":"DPE-FIE-ASE","functionCodeDescription":None,"authorizationName":None,"sortOrder":334,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1329,"functionCode":"DPE-FIE-AME","functionCodeDescription":None,"authorizationName":None,"sortOrder":335,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1330,"functionCode":"DPE-FIEI-ASE","functionCodeDescription":None,"authorizationName":None,"sortOrder":336,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None},{"id":1331,"functionCode":"DPE-FIEI-AME","functionCodeDescription":None,"authorizationName":None,"sortOrder":337,"limitation":None,"isAutomaticPreapproval":None,"isAuthorized":None,"designeeTypeId":24,"decisionId":None,"category":{"code":None,"id":1,"name":"Airplane","isActive":False},"categoryId":1,"functionCodeDecisions":None,"hasTypeRating":False,"selectedTypeRatings":[],"typeId":None}],"designeeTypeId":24,"isLocationSearch":True,"firstName":None,"lastName":None,"designator":None,"city":None,"county":None,"stateId":state_id,"zipCode":None,"firstClassAME":False,"examinerAME":False,"himsAME":False,
        }

        url = 'https://designee.faa.gov/designeeapi/api/Cloa/Search/'

        response = requests.post(url, json = data)

        examiner_info = response.json()

        context = {
            'examiners': examiner_info,
            'stateId': state_id,
            # 'status': status, 
            # 'phone_email': phone_email,
            # 'office_name': office_name,
            # 'address': address,
            # 'function_codes': function_codes,
        }
            
        return render(request, 'pep_app/examiner.html', context)

def state_search(request):
    if request.method == 'POST':
        data = {
    "isInternal": False,
    "countryId":184,
    "pageModel":{
        "first":0,
        "rows":10,
        "sortOrder":1,
        "filters":{},
        "globalFilter": None
    },
    "selectedFunctionCodes":[],
    "designeeTypeId":24,
    "isLocationSearch": True,
    "firstName": None,
    "lastName": None,
    "designator": None,
    "city": None,
    "county": None,
    "stateId":int(request.POST.get('states')[0]),
    "zipCode": None,
    "firstClassAME": False,
    "examinerAME": False,
    "himsAME": False
}
        states = requests.post('https://designee.faa.gov/designeeapi/api/Cloa/Search/',json=data)
        # print('status code:', states.status_code)
        # print(request.POST)
        # print(int(request.POST.get('states')[0]))
        return render(request, 'pep_app/index.html', {'designee': states.json()})
    else:
        return render(request, 'pep_app/index.html')