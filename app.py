from flask import Flask
from flask_restful import Api, Resource
from mailing_automation import *
from database import *
import multiprocessing
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api=Api(app)
cors = CORS(app)

class addmail(Resource):
    @cross_origin()
    def get(self, data):
        try:
            details = data.split("_")
            queue=multiprocessing.Queue()
            p1 = multiprocessing.Process(target=add_mail, args=(details[1], details[0], queue))

            p2= multiprocessing.Process(target=sendmail().send, args=(details[0], details[1]))
            #test=add_mail(details[1], details[0])
            p1.start()
            p2.start()
            p1.join()
            p2.join()

            if(queue.get()=="Error"):
                return {
                    "status": "DatabaseError"
                }
            #sendmail().send(details[0], details[1])
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