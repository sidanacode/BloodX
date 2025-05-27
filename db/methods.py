from models import engine,Donor,Request,BloodBank
from sqlalchemy.orm import sessionmaker
from datetime import date , timedelta,datetime
Session = sessionmaker(bind=engine,autoflush=True,autocommit=False)


## Crud operations 

def add_donor(db,usr_name,usr_dob,usr_gender,usr_bloodgroup,usr_mobnum,usr_pincode,usr_donated,usr_last_donation_date):
    if isinstance(usr_dob,str):
        usr_dob = datetime.strptime(usr_dob,"%d-%m-%Y").date()
    if isinstance(last_donation_date,str):
        last_donation_date = datetime.strptime(last_donation_date,"%d-%m-%Y").date()
    
    new_donor = Donor(name=usr_name,dob=usr_dob,gender=usr_gender,blood_group=usr_bloodgroup,mobile_no=usr_mobnum,pin_code=usr_pincode,)