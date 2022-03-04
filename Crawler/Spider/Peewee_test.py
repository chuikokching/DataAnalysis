from peewee import *

db = MySQLDatabase("crawler_spider", host="rm-wz91d04489o07fux7qo.mysql.rds.aliyuncs.com", port=3306, user="ckc_spider", password="Chuikokching520")


class Person(Model):
    name = CharField(max_length=20)
    birthday = DateField(null=True)

    class Meta:
        database = db # This model uses the "people.db" database.
        # table_name = "users" #自定义表名

#数据的增、删、改、查
if __name__ == "__main__":
    db.create_tables([Person])
    from datetime import date

    # #生成数据
    # uncle_ckc = Person(name='ckc', birthday=date(1994, 3, 3))
    # uncle_ckc.save()  # bob is now stored in the database
    #
    # uncle_ckc = Person(name='bkb', birthday=date(1998, 3, 4))
    # uncle_ckc.save()  # bob is now stored in the database
    #
    # uncle_ckc = Person(name='aka', birthday=date(1999, 3, 5))
    # uncle_ckc.save()  # bob is now stored in the database

    #查询数据（只获取一条） get方法在取不到数据会抛出异常
    ckc = Person.select().where(Person.name == 'ckc').get()
    print(ckc.name)
    ckc = Person.get(Person.name == 'ckc')
    print(ckc.birthday)

    # query = Person.select().where(Person.name == 'ckc')[1:]
    # for person in query:
    #     print(person.name, person.birthday)

    query = Person.select().where((Person.name == "aka") |(Person.name == "bkb") )
    for person in query:
        print(person.name, person.birthday)

    # #Update & Delete
    # query = Person.select().where(Person.name == 'aka')
    # for person in query:
    #     print(person.name, person.birthday)
    #     person.birthday = date(2010, 12,4)
    #     person.save()
    #     print(person.name, person.birthday)
    #     # person.delete_instance()