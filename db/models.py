from sqlalchemy import create_engine,Column,String,Integer,Boolean,Date
from sqlalchemy.orm import declarative_base
db_url = "postgresql+psycopg://postgres:1234@localhost:5433/blood"
engine = create_engine(db_url,echo=True)
Base = declarative_base()

class Donor(Base):
    __tablename__ = "donors"
    donor_id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    dob = Column(Date,nullable=False)
    gender = Column(Boolean,nullable=False)
    blood_group = Column(String,nullable=False)
    mob_num = Column(String,nullable=False)
    pin_code = Column(String,nullable=False)
    donated=Column(Boolean,nullable=False)
    last_donation_date=Column(Date,nullable=True)
class Request(Base):
    __tablename__="requests"
    request_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    mobile_no=Column(String,nullable=False)
    blood_group=Column(String,nullable=False)
    units_req=Column(Integer,nullable=False)
    spd_req=Column(Boolean,nullable=False)

class BloodBank(Base):
    __tablename__="BloodBanks"
    bloodbank_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    address=Column(String,nullable=False)
    number=Column(String,nullable=True)
    
    
Base.metadata.create_all(bind=engine)