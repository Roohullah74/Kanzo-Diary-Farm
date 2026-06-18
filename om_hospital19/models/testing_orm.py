from odoo import models, fields,api
from odoo.exceptions import ValidationError




class TestPatient(models.Model):
    _name = 'test.patient'
    _description = 'Test Patient'

    name1 = fields.Char(string="Name")
    age1 = fields.Integer(string="Age")
    code_num=fields.Integer(string="Code Number")

    def create_test_patient(self):

        if not self.name1:
            # 🔴 raise stops execution
            raise ValidationError("Please enter a name first!")

        # 🔵 ORM LOGIC
        reco = self.env['test.patient'].create({
            'name1': 'Ahmed',
            'age1': 30,
            'code_num': 100,
        })

        # 🟢 if create succeeded → show green message
        if reco:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success!',
                    'message': f'{reco.name1} created!',
                    'type': 'success',
                    'sticky': False,
                }
            }

    #
    # def create_test_patient(self):
    #     if self.name1:
    #         tes=self.env['test.patient'].create([])
    #     # 🟢 BUSINESS LOGIC: check condition first
    #     if self.age1 <0:
    #         raise ValidationError("Age cannot be negative!")
    #
    #
    #     # 🔵 ORM LOGIC: create record
    #     reco = self.env['test.patient'].create({
    #         'name1': 'Ahmed',
    #         'age1': 30,
    #         'code_num': 100,
    #     })
    #     print(reco.id)
    #     print('this log record',reco.id)
    #     print('that one try',reco.name1)
    #     print('code num',reco.code_num)
    #     print('testing',self.name1)
    #     print('age',self.age1)
    #
    #
    #     return reco


        # # 🔴 Check — if wrong, STOP here
        # if (self.code_num == 123) and (self.age1 != ''):
        #  return {
        #         'type': 'ir.actions.client',
        #         'tag': 'display_notification',
        #         'params':{
        #             'title': 'Success!',
        #             'message':' Code match successfully!',
        #             'type': 'success',
        #             'sticky': False,
        #              }
        #  }
        #
        # else:
        #     raise ValidationError("Code number is not corrrect!")

        # ✅ Create the record
        # reco = self.env['test.patient'].create({

        # 🟢 ONE return at the end — show success

            # }
        # }
# ------------------------------------------------------------------
    # def create_test_patient(self):
    #     if self.age1<=30:
    #         name='roohullah1'
    #     else:
    #         name='wali1'
    #     rec=self.env['test.patient'].create([{
    #             'name1': name,
    #             'age1': self.age1
    #         }])
    #     print(rec.id)
    #     print(self.age1)
    #     print(self.name1)
    #     return rec
    #
# ---------------------------------------------------------

    # def create_test_patient(self):
    #
    #     patient = dict([
    #         {'name1': 'roohullah1', 'age1': 23},
    #         {'name1': 'wali', 'age1': 34},
    #         {'name1':'sayed','age1':44},
    #         {'name1':'salaer','age1':44},
    #         {'name1':'abubaqar','age1':44},
    #         {'name1':'noor','age1':44},
    #         {'name1':'Ayub','age1':44},
    #         {'name1':'Sher batsha','age1':44},
    #         {'name1':'Zakir','age1':44}
    #
    #     ])
    #
    #     reco = self.env['test.patient'].create([patient])
    #     return reco

    #
    # def create_test_patient(self):
    #     reco = self.env['test.patient'].create({
    #         'name1': 'Ahmed',
    #         'age1': 30,
    #     })
    #
    #     print(reco.id)  # 5
    #     print(reco.name1)  # Ahmed
    #     print(reco.age1)  # 30
    # self = the record currently open on screen


    # def create_test_patient(self):
    #     reco = self.env['test.patient'].create({
    #         'name1': self.name1 + ' (Copy)',  # takes name from current record
    #         'age1': self.age1,  # takes age  from current record
    #     })
    #     print(reco.name1)  # "tt (Copy)"  if current record is tt
    #     print(reco.age1)   # "tt (Copy)"  if current record is tt
