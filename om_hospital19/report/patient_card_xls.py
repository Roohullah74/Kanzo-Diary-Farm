
# # -*- coding: utf-8 -*-


#
# import base64
# import io
# from odoo import models
#
# class PatientCardXlsx(models.AbstractModel):
#     _name = 'report.om_hospital19.report_patient_id_card_xls'
#     _inherit = 'report.report_xlsx.abstract'
#
#     def generate_xlsx_report(self, workbook, data, patients):
#
#         # ---------------- FORMATS ----------------
#         bold = workbook.add_format({'bold': True})
#         title_format = workbook.add_format({
#             'bold': True,
#             'align': 'center',
#             'bg_color': '#FFD966',
#             'border': 1
#         })
#
#         value_format = workbook.add_format({'border': 1})
#         label_format = workbook.add_format({'bold': True, 'border': 1})
#
#         for obj in patients:
#             sheet = workbook.add_worksheet(obj.name[:31])  # Excel limit
#
#             row = 2
#             col = 2
#
#             # Column width
#             sheet.set_column('C:C', 18)
#             sheet.set_column('D:D', 25)
#
#             # ---------------- TITLE ----------------
#             sheet.merge_range(row, col, row, col + 1, 'Patient ID Card', title_format)
#
#             row += 2
#
#             # ---------------- IMAGE ----------------
#             if obj.image:
#                 patient_image = io.BytesIO(base64.b64decode(obj.image))
#                 sheet.insert_image(
#                     row, col,
#                     "image.png",
#                     {
#                         'image_data': patient_image,
#                         'x_scale': 0.5,
#                         'y_scale': 0.5
#                     }
#                 )
#                 row += 6
#
#             # ---------------- DATA ----------------
#             def write_field(label, value):
#                 nonlocal row
#                 sheet.write(row, col, label, label_format)
#                 sheet.write(row, col + 1, value or '', value_format)
#                 row += 1
#
#             write_field('Name', obj.name)
#             write_field('Reference', obj.reference)
#             write_field('Age', obj.age)
#             write_field('Gender', dict(obj._fields['gender'].selection).get(obj.gender))
#             write_field('Status', dict(obj._fields['state'].selection).get(obj.state))
#             write_field('Responsible', obj.responsible_id.name if obj.responsible_id else '')
#             write_field('Appointments', obj.appointment_count)
#             write_field('Description', obj.note)
#
#             # ---------------- FOOTER BOX ----------------
#             row += 2
#             sheet.merge_range(row, col, row + 1, col + 1, 'Signature', title_format)
#
#
#
#
#
#
# # # -*- coding: utf-8 -*-
# # import base64
# # import io
# # from odoo import models
# #
# #
# # class PatientCardXlsx(models.AbstractModel):
# #     _name = 'report.om_hospital19.report_patient_id_card_xls'
# #     _inherit = 'report.report_xlsx.abstract'
# #
# #     def generate_xlsx_report(self, workbook, data, patients):
# #
# #         sheet = workbook.add_worksheet('Patient ID Card')
# #
# #         # ---------------- FORMATS ----------------
# #         title_format = workbook.add_format({
# #             'bold': True,
# #             'align': 'center',
# #             'valign': 'vcenter',
# #             'border': 1,
# #         })
# #
# #         label_format = workbook.add_format({
# #             'bold': True,
# #             'border': 1
# #         })
# #
# #         value_format = workbook.add_format({
# #             'border': 1
# #         })
# #
# #         center_format = workbook.add_format({
# #             'align': 'center',
# #             'border': 1
# #         })
# #
# #         # ---------------- COLUMN SIZE ----------------
# #         sheet.set_column('A:A', 20)
# #         sheet.set_column('B:B', 25)
# #
# #         row = 0
# #
# #         # ---------------- LOOP ----------------
# #         for obj in patients:
# #
# #             # ===== TITLE =====
# #             sheet.merge_range(row, 0, row, 1, 'PATIENT ID CARD', title_format)
# #             row += 2
# #
# #             # ===== IMAGE =====
# #             if obj.image:
# #                 image_data = base64.b64decode(obj.image)
# #                 image_stream = io.BytesIO(image_data)
# #
# #                 sheet.insert_image(row, 0, "patient.png", {
# #                     'image_data': image_stream,
# #                     'x_scale': 0.5,
# #                     'y_scale': 0.5,
# #                 })
# #
# #             row += 5
# #
# #             # ===== PATIENT DATA =====
# #             sheet.write(row, 0, 'Reference', label_format)
# #             sheet.write(row, 1, obj.reference or '', value_format)
# #             row += 1
# #
# #             sheet.write(row, 0, 'Name', label_format)
# #             sheet.write(row, 1, obj.name or '', value_format)
# #             row += 1
# #
# #             sheet.write(row, 0, 'Age', label_format)
# #             sheet.write(row, 1, obj.age or 0, value_format)
# #             row += 1
# #
# #             sheet.write(row, 0, 'Gender', label_format)
# #             sheet.write(row, 1, obj.gender or '', value_format)
# #             row += 1
# #
# #             sheet.write(row, 0, 'Status', label_format)
# #             sheet.write(row, 1, obj.state or '', value_format)
# #             row += 1
# #
# #             sheet.write(row, 0, 'Appointments', label_format)
# #             sheet.write(row, 1, obj.appointment_count or 0, value_format)
# #             row += 2
#
#             # ===== SEPARATOR =====
#             row += 2
# # from docutils.parsers.rst.directives.tables import align
# # from xlrd import sheet
# #
# # from odoo import models
# #
# # class PatientCardXlsx(models.AbstractModel):
# #     _name = 'report.om_hospital19.report_patient_id_card_xls'
# #     _inherit = 'report.report_xlsx.abstract'
# #
# #     def generate_xlsx_report(self, workbook, data,patients):
# #         print('patient test',patients)
# #         sheet=workbook.add_worksheet('Patient_ID')
# #
# #         bold = workbook.add_format({'bold': True})
# #         format_1=workbook.add_format({'bold':True,'align':'center','bg_color':'yallow'})
# #         row=3
# #         col=3
# #         sheet.set_column('D:D',13)
# #         sheet.set_column('E:E',12)
# #
# #         for obj in patients:
# #             row+=1
# #             sheet.insert_range(row,col,row,col+1,'ID CARD',format_1)
# #             row+=1
# #             < img
# #             t - att - src = "'data:image/png;base64,%s' % o.image_field"
# #             style = "max-width:100%; height:auto;" / >
# #
# #
# #             print('patient test', obj)
# #             report_name = obj.name
# #             # One sheet by partner
# #             # sheet = workbook.add_worksheet(report_name[:31])
# #             sheet.write(0, 0, obj.name, bold)