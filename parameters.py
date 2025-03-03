# def fn_pdata(name,blood_group,*disease,email="Not given"):
#     print(f"The name of the patient is:{name}")
#     print(f"Blood group of the patient is:{blood_group}")
#     for x in disease:
#         print(f"Patient is suffering from:{x}")
#     print(f"Patients Email id is:{email}")
#     print("/r")
#
# fn_pdata("Chalan","B+","fever","cold")
# fn_pdata("Mohan","B+","Gastrick")

def fn_sdata(name,*email,**address):
    print(f"The nam of the student is:{name}")
    for x in email:
        print(f"The email ids provided by student is:{x}" )
    for i,j in address.items():
        print(f"{i}={j}")
    print("\r")

fn_sdata("Chalan NY","c@gmail.com","cc@gmail.com",address="Hassan",house="123")
fn_sdata("Mohan","mc@gmail.com",address="Hassan")






