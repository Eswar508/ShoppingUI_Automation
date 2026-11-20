from faker import Faker
import json
def get_registration_data(data:str|None=None):
    fake=Faker()
    reg_data={
        "first_name":fake.first_name(),
        "last_name":fake.last_name(),
        "email":fake.email(),
        "password":fake.password()
    }
    return reg_data|data if data is not None else reg_data
def get_test_data(data_name):
    file_name="test_data/"+data_name+".json"
    with open(file_name,"r") as file:
        test_data=json.load(file)
    return test_data
