from datetime import datetime
from pytz import timezone

# current_datetime = datetime.now()
#
# current_date = current_datetime.strftime("%Y-%m-%d")
# print("current date = ", current_date)
#
# current_time = current_datetime.strftime("%H:%M")
# print("current time = ", current_time)
#
# print(f"current datetime: {current_date}T{current_time}")

def patient_id():
    fmt = "%Y%m%d%H%M%S"
    bangkok = datetime.now(timezone('Asia/Bangkok'))
    return bangkok.strftime(fmt)

print(patient_id())