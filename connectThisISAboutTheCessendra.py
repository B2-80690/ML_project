import pymongo;

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/")

# here we are connectiong to which datadase i am connecting
db = client["dbda"]

    # here we are connecting the collection of that particular database
emp_collection = db['emp']

    # now on the collection we are finding all the data in that collections
all = emp_collection.find()



def my_connectior_():

    # here we are connectiong to which datadase i am connecting
    db = client["dbda"]

    # here we are connecting the collection of that particular database
    emp_collection = db['emp']

    # now on the collection we are finding all the data in that collections
    all = emp_collection.find()

    for val in all:
        # print(val)

        print(f"your id is = {val['_id']} , Your name is = {val['ename']} , your job is = {val['job']}")

# my_connectior_()


def all_manager_finder(all):

    criteria = {'job':'MANAGER'}

    emps = emp_collection.find(criteria)


    for val in emps:
        if val['job'] == 'MANAGER':
            print(val)



# all_manager_finder(all)



def insert_emp():

    newEmp = {"-id":101, "ename":"samir", "sal":1200, "job":"President","dept":000}

    emp_collection.insert_one(newEmp)

    print(f"your value is inserted congratulations .....")


# insert_emp()


def all_manager_finder_(all):

    criteria = {'job':'President'}

    emps = emp_collection.find(criteria)


    for val in emps:
        print(val)





# all_manager_finder_(all)


def delect_fun():

    empId = int(input(f"please enter your id for delection"))

    emp_collection.delete_one({'-id':empId})

    print(f"your given empid = {empId} is deleted ....")


# delect_fun()


def update_filds():

    emp_collection.update_one({'-id':101} , {'$set':{"ename":"Samir_Shinde"}})

#
# update_filds()
#
#
# my_connectior_()




def aggragation_pip():
    returned_val = emp_collection.aggregate([
        {
            '$sort':{'sal':1}
        },{
            '$project':{'ename':1 , 'sal':1 , '_id':0}
        }
    ])
    for val in returned_val:
        print(val)



def pipline_another():

    pipline = [
        {
            '$addFields':{
                'commission':{'$ifNull':['$comm',0]}
                        }

        },
        {
            '$addFields':{
                'totalSalary':{'$add':['$sal', '$commission']}
            }
        },
        {
            '$project':{'ename':1 , 'commission':1 , 'sal':1 , 'totalSalary':1}
        }
    ]

    res = emp_collection.aggregate(pipline)
    for val in res:
        print(val)

pipline_another()



# aggragation_pip()



