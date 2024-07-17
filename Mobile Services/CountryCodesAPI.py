import os
import logging
import pymysql
from dotenv import load_dotenv
from flask import Blueprint, Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

load_dotenv(dotenv_path='.env')

class CountryCodes:
    def __init__(self):
        self.USER = os.getenv("USER")
        self.PASSWORD = os.getenv("PASSWORD")
        self.HOST = os.getenv("HOST")
        self.PORT = int(os.getenv("PORT"))
        self.DATABASE = os.getenv("DATABASE")
    
    def CountryCodeDataTable(self):
        try:
            connection = pymysql.connect(
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT,
                database=self.DATABASE
            )
            
            cursor = connection.cursor()
            query = "SELECT CountryName, CountryCode FROM CountryCodes"
            
            cursor.execute(query); result = cursor.fetchall()
            countries = [{"CountryName": row[0], "CountryCode": row[1]} for row in result]
            
            return countries
        except Exception as e:
            logging.error("An Error Occured: ", exc_info=e)
            raise e
        finally:
           if connection:
               cursor.close()
               connection.close()
               
class CountryCodes_API:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.CountryCodes_blueprint = Blueprint('CountryCodes', __name__)
        self.CountryCodes_blueprint.add_url_rule('/CountryCodes', 'CountryCodes', self.CountryCodesData, methods=['POST'])
        self.CountryCodes_ = CountryCodes()
        
    def CountryCodesData(self):
        try:
            token = request.get_json()
            
            if token["token"] == "CountryCodes":
                data = self.CountryCodes_.CountryCodeDataTable()
            
                response = {
                    "success": True,
                    "data": data,
                    "message": "Country Codes Successfully fetched."
                }
                
                return jsonify(response), 200
            else:
                response = {
                    "success": False,
                    "data": {},
                    "message": "unknown Request"
                }
                
                return jsonify(response), 200
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            response = {
                "success": False,
                "data": {},
                "message": str(e)    
            }
            return jsonify(response), 400
        
    def run(self):
        try:
            self.app.register_blueprint(self.CountryCodes_blueprint)
            self.app.run(debug=True)
        except Exception as e:
            logging.error('An Error Occured: ', exc_info=e)
            raise e


if __name__=="__main__":
    
    countrycodes = CountryCodes_API()
    countrycodes.run()