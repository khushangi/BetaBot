import requests     
import json
import random

class apiView():
        def apiCall():
            response_API = requests.get('https://the-trivia-api.com/api/questions?limit=1')
            data = response_API.text
            #print(response_API.status_code)
            #print(data)
            q_list = json.loads(data)
            z=q_list[0]
            k=0
            # corrans=data[0]
            # listAll=data[0][3]
                    #Testing for api
            a=z["correctAnswer"]
            b=z["incorrectAnswers"]
            ques=z["question"]
            rightans = z["correctAnswer"]
            b.append(a)
            random.shuffle(b)
            for i in range(0,4):
                  if b[i]==a:
                        k=i
                        break

            dictTest=[a,b,ques,k]
            return dictTest
            
# class test:
#       dict=apiView.apiCall()
#       print (dict)
