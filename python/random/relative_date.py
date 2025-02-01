from datetime import date
from dateutil.relativedelta import relativedelta

input_date = date(2025, 1, 20)
previous_month_date = input_date - relativedelta(months=1)
#previous_day_date = input_date - relativedelta(days=1)
print(previous_month_date)  # Output: 2024-12-20

