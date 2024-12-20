class Father:
    x=10
    y=20
    z=30
    def property(self):
        self.name="f_name"
        self.bank="f_bank"
        print(self.bank)
        print(self.name)
class Mother:
    p=40
    q=50
    r=60
    def property1(self):
        self.name1="m_name"
        self.bank1="m_bank"
        print(self.name1)
        print(self.bank1)
class Son(Father,Mother):
    pass
obj=Son()
obj.property()
obj.property1()
print("son propert_details= ",dir(Son))

