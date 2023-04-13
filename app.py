from flask import Flask
from flask_restful import Api, Resource
from mailing_automation import *
from database import *

app = Flask(__name__)
api=Api(app)

class addmail(Resource):
    def get(self, data):
        try:
            details = data.split("_")
            test=add_mail(details[1], details[0])
            if(test=="Error"):
                return {
                    "status": "DatabaseError"
                }
            sendmail().send(details[0], details[1])
            print("executed")
            return {
                "status": "success"
            }
        except:
            return {
                "status": "ServerError"
            }

api.add_resource(addmail, '/<string:data>' )

if __name__ == '__main__':
    app.run(debug=False)