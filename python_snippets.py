# POST the file using python requests
files = {'file_key': open('my_file.extension', 'rb')}
response = requests.post(url, files=files, data={'key': 'value'}, timeout=3)

# ---------------------------------------------------------------------------- #

# Save the file (locally) from post request in django views
destination = open('my_file.extension', 'wb+')
for chunk in request.FILES['file_key'].chunks():
    destination.write(chunk)
destination.close()

# ---------------------------------------------------------------------------- #

from django.core.files import File  # This is to save the raw file in models
my_file = open('file.extension', 'rb')
my_new_record = ModelName(field1='', file_field=File(my_file),
                          field2=request.data['key'])
# File class helps to store file in django db
my_new_record.save()  # Save the new record in database
my_file.close()

# ---------------------------------------------------------------------------- #

# Send notifications on android mobile using third party app Pushetta
# pip install pushetta
from pushetta import Pushetta

api_key = ""
channel_name = ""
p = Pushetta(api_key)
msg = 'Hey there, Android! I am Python here.'
p.pushMessage(channel_name, msg)
# ---------------------------------------------------------------------------- #
