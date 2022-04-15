from unicodedata import decimal
import xlrd
import traceback
from api.models import Organization, District


def extract_excel_data(location):
    """
    :param location: uri of the excel file of users to extract from. Usually excel files are placed in the sheets folder
    Creates Organisations  from an excel sheet provided
    Sheet Fields: No , facility_name ,District , Contact Person , Telephone
    """
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    for row_number in range(0, sheet.utter_max_rows):
        try:
            row_data = sheet.row_values(row_number)
        except Exception as e:
            print(e)
            break
        
        facility_name_value = row_data[0]
        district_value = row_data[1]
        if phone_number_value:  phone_number_value = int(row_data[2])
        latitude = (row_data[3])
        longitude = decimal(row_data[4])
        

        if not facility_name_value:
            break

        try:
            district_value = District.objects.get(name__contains=district_value)
        except Exception as e:
            print(e)
            district_value,_ = District.objects.get_or_create(name=district_value)
       
        try:
            phone_number_value = "0" + str(int(phone_number_value))
            organization = Organization(
                        facility_name=facility_name_value.strip(),
                        phone_number=phone_number_value.strip(),
                        district=district_value,
                        latitude=latitude,
                        longitude=longitude
                        )
            organization.save()
        except Exception:
            print(traceback.print_exc())
