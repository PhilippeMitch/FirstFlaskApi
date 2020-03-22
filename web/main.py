# from flask import Flask, jsonify, request
# from flask_restful import Api, Resource 


# app = Flask(__name__)
# api = Api(app)

# def checkPostedData(postedData, functionName):
#     if(functionName == 'add' or functionName == 'subtract' or functionName == 'multiply'):
#         if 'x' not in postedData or 'y' not in postedData:
#             return 301
#         else:
#             return 200
#     elif (functionName == 'division'):
#         if 'x' not in postedData or 'y' not in postedData:
#             return 302
#         elif int(postedData['y'])==0:
#             return 302
#         else:
#             return 200

# class Add(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'add')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = x+y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)

# class Subtract(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'subtract')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = x-y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)

# class Multiply(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'multiply')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = x*y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)

# class Multiply(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'multiply')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = x*y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)

# class Multiply(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'multiply')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = x*y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)

# class Divide(Resource):
#     def post(self):
#         postedData = request.get_json()

#         status_code = checkPostedData(postedData, 'division')

#         if (status_code!=200):
#             retJson = {
#                 'Message': 'An error happened',
#                 'Status Code': status_code
#             }
#             return jsonify(retJson)

#         x = postedData['x']
#         y = postedData['y']
#         x = int(x)
#         y = int(y)

#         ret = (x*1.0)/y
#         retMap = {
#             'Message': ret,
#             'Status Code': 200
#         }
#         return jsonify(retMap)


# api.add_resource(Add, '/add')
# api.add_resource(Subtract, '/subtract')
# api.add_resource(Multiply, '/multiply')
# api.add_resource(Divide, '/divide')

# @app.route('/')
# def heloo_world():
#     return 'Hello World'


# if __name__ =='__main__':
#     app.run(host='0.0.0.0')