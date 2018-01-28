import mysql.connector
from mysql.connector import Error
 
  
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database='db', user='mason', password='JJxFwcBKvn2wgdt6!')             
    except Error as e:
        print(e)
    return conn

def execute_statement(statement, request=False):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(statement)
    result = ""
    if request:
        result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def account_exists(email):
    return [] != execute_statement("SELECT 1 FROM USERS WHERE EMAIL ='" + email +  "';", True)

def create_account(first, last, email, passwd):
    if not account_exists(email):
       execute_statement("INSERT INTO USERS (EMAIL, FIRST, LAST, PASSWD) VALUES ('" + email + "', '" + first + "', '" + last + "', '" + passwd +"');")
       return True
    else:
       return False

def login(email, password):
    return account_exists(email) and len(execute_statement("SELECT 1 FROM USERS WHERE PASSWD = '" + password + "' AND EMAIL = '" + email + "';", True)) == 1

def school_exits(domain):
    return [] != execute_statement("SELECT 1 FROM SCHOOLS WHERE DOMAIN='" + domain + "';", True)

def register_domain(domain):
    if not school_exits(domain):
        execute_statement("INSERT INTO SCHOOLS (DOMAIN) VALUES ('" + domain + "');")
        return True
    else:
        return False

def get_school_id(domain):
    if school_exists(domain):
        return execute_statement("SELECT ID FROM SCHOOLS WHERE DOMAIN='" + domain + "';", True)[0][0]
    return -1

def get_user_id(email):
    if account_exists(email):
        return execute_statement("SELECT ID FROM USERS WHERE EMAIL='" + email +"';", True)[0][0]
    return -1

def get_user_data(user_id):
    if len(execute_statement("SELECT 1 FROM USERS WHERE ID=" + str(user_id) + ";", True)) == 1:
        return execute_statement("SELECT FIRST, LAST, EMAIL, ID FROM USERS WHERE ID=" + str(user_id) + ";", True)[0]
    else:
        return None


