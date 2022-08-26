from sqlalchemy import create_engine

# Credentials to database connection
hostname="localhost"
dbname="dbpro"
uname="root"
pwd=""

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

class dataSave(object):

    @classmethod
    def getData(cls, data):
        data.to_sql('tb_projet', engine, index=False)
        return 'Data'
