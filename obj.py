import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='root',
                                   database='mess')
        query = 'create table if not exists Desi_foods(Food varchar(200) primary key, Price int )'
        cur=self.con.cursor()
        cur.execute(query)
        print("First table is Created")
        query2 = 'create table if not exists Fast_foods(Food varchar(200) primary key, Price int )'
        cur=self.con.cursor()
        cur.execute(query2)
        print("Second table is Created")
        query = 'create table if not exists Owners(name varchar(200), phone_no int )'
        cur = self.con.cursor()
        cur.execute(query)
        print("Third table is Created")
        query = 'create table if not exists Dessert(Food varchar(200) primary key, Price int )'
        cur = self.con.cursor()
        cur.execute(query)
        print("Fourth table is Created")
        query = 'create table if not exists Riders(name varchar(200), phone_no int)'
        cur = self.con.cursor()
        cur.execute(query)
        print("Fifth table is Created")

    #Insertion function
    def insert_owner_details(self, name, phone_no):
        query1 = "Insert into owners(name, phone_no) values('{}', {})".format(name, phone_no)
        print(query1)
        cur = self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("Owners details data is saved in database")

    def insert_dessert_details(self, food, price):
        query1 = "Insert into Dessert(food, price) values('{}', {})".format(food, price)
        print(query1)
        cur = self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("Dessert details data is saved in database")

    def fetch_Dessert_details(self):
        query1='select * from Dessert'
        cur = self.con.cursor()
        cur.execute(query1)
        details = []

        for row in cur:
            print()
            print("Food: ", row[0])
            details.append(row[0])
            details.append(row[1])
            print("Price: ", row[1])
            print()
            print()
        return details

    def insert_Rider_details(self, name, phone_no):
        query1 = "Insert into Riders(name, phone_no) values('{}', {})".format(name, phone_no)
        print(query1)
        cur = self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("Riders details data is saved in database")

    def fetch_Rider_details(self):
        query1 = 'select * from Riders'
        cur = self.con.cursor()
        cur.execute(query1)
        details = []

        for row in cur:
            print()
            print("Name: ", row[0])
            details.append(row[0])
            details.append(row[1])
            print("Phone number: ", row[1])
            print()
            print()
        return details



    def fetch_Owners_details(self):
        query1='select * from owners'
        cur = self.con.cursor()
        cur.execute(query1)
        details = []
        # prc=[]
        for row in cur:
            print()
            print("Name: ", row[0])
            details.append(row[0])
            details.append(row[1])
            print("Phone number: ", row[1])
            print()
            print()
        return details


    def insert_data_desi_foods(self, Food, Price):
        query1 = "Insert into Desi_foods(Food, Price) values('{}', {})".format(Food, Price)
        print(query1)
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("Desi foods data is saved in database")

    def insert_data_fast_foods(self, Food, Price):
        query2 = "Insert into Fast_foods(Food, Price) values('{}', {})".format(Food, Price)
        print(query2)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("Fast foods data is saved in database")

    #Fetching data function

    def fetch_data_desi_foods(self):
        query1='select * from Desi_foods'
        cur = self.con.cursor()
        cur.execute(query1)
        itm = []
        # prc=[]
        for row in cur:
            print()
            print("Food: ", row[0])
            itm.append(row[0])
            itm.append(row[1])
            print("Price: ", row[1])
            print()
            print()
        return itm

    def fetch_data_fast_foods(self):
        row ='\0'
        itm = []
        query2='select * from Fast_foods'
        c = self.con.cursor()
        c.execute(query2)
        itm=[]
        #prc=[]
        print(c)

        for row in c:
            print()
            print("Food: ", row[0])
            itm.append(row[0])
            itm.append(row[1])
            print("Price: ", row[1])
            print()
            print()
        return itm

    # deleting data

    def delete_data_desi_foods(self, Food):
        query1="delete from Desi_foods where Food='{}'".format(Food)
        print(query1)
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        print("Deleted")

    def delete_data_fast_foods(self, Food):
        query2="delete from Fast_foods where Food='{}'".format(Food)
        print(query2)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("Deleted")

    #Updating data

    def update_data_desi_foods(self,Food,NewFood, NewPrice):
        query="update Desi_foods set Food='{}',Price={} where Food='{}' ".format(NewFood, NewPrice, Food)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def update_data_fast_foods(self,Food,NewFood, NewPrice):
        query="update Fast_foods set Food='{}',Price={} where Food='{}' ".format(NewFood, NewPrice, Food)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def min_desi_price(self):

        query1 = "SELECT MIN(price) FROM desi_foods "
        cur = self.con.cursor()
        cur.execute(query1)
        lowest = cur.fetchone()
        query2 = "SELECT Food FROM desi_foods where price='{}'".format(lowest[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name = cur.fetchone()
        print("Name:", name)
        print("Lowest Price of food available : ", lowest[0])
        return (lowest, name)


    def min_fast_price(self):

        query1 = "SELECT MIN(price) FROM Fast_foods "
        cur = self.con.cursor()
        cur.execute(query1)
        lowest = cur.fetchone()
        query2 = "SELECT Food FROM Fast_foods where price='{}'".format(lowest[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name = cur.fetchone()
        print("Name:", name)
        print("Lowest Price of food available : ", lowest[0])
        return (lowest, name)



    def max_desi_price(self):

        query1 = "SELECT MAX(price) FROM desi_foods "
        cur = self.con.cursor()
        cur.execute(query1)
        maximum = cur.fetchone()

        query2 = "SELECT Food FROM desi_foods where price='{}'".format(maximum[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name = cur.fetchone()
        print("Name:", name)
        print("Maximum Price of food available : ", maximum[0])
        return (maximum, name)

    def max_fast_price(self):

        query1 = "SELECT MAX(price) FROM Fast_foods "
        cur = self.con.cursor()
        cur.execute(query1)
        maximum = cur.fetchone()


        query2 = "SELECT Food FROM Fast_foods where price='{}'".format(maximum[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name=cur.fetchone()
        print("Name:",name)
        print("Maximum Price of food available : ", maximum[0])
        return (maximum ,name)

    def update_data_dessert_foods(self,Food,NewFood, NewPrice):
        query="update dessert set Food='{}',Price={} where Food='{}' ".format(NewFood, NewPrice, Food)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def update_data_owner(self, name, Newname, phoneno):
        query = "update owners set name='{}',phone_no={} where name='{}' ".format(Newname, phoneno, name)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def delete_data_owner(self, name):
        query2="delete from owners where name='{}'".format(name)
        print(query2)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("Deleted")

    def delete_data_dessert_foods(self, Food):
        query2="delete from dessert where Food='{}'".format(Food)
        print(query2)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("Deleted")

    def update_data_rider(self, name, Newname, phoneno):
        query = "update riders set name='{}',phone_no={} where name='{}' ".format(Newname, phoneno, name)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def delete_data_rider_foods(self, name):
        query2="delete from riders where name='{}'".format(name)
        print(query2)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        print("Deleted")

    def min_dessert_price(self):

        query1 = "SELECT MIN(price) FROM Dessert "
        cur = self.con.cursor()
        cur.execute(query1)
        lowest = cur.fetchone()
        query2 = "SELECT Food FROM Dessert where price='{}'".format(lowest[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name = cur.fetchone()
        print("Name:", name)
        print("Lowest Price of food available : ", lowest[0])
        return (lowest, name)

    def max_dessert_price(self):

        query1 = "SELECT MAX(price) FROM Dessert "
        cur = self.con.cursor()
        cur.execute(query1)
        Maximum = cur.fetchone()
        query2 = "SELECT Food FROM Dessert where price='{}'".format(Maximum[0])
        cur = self.con.cursor()
        cur.execute(query2)
        name = cur.fetchone()
        print("Name:", name)
        print("Maximum Price of food available : ", Maximum[0])
        return (Maximum, name)




ft=DBHelper()
