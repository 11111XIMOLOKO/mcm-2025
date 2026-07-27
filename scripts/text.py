import pandas as pd
from ydata_profiling.profile_report import ProfileReport

programs = pd.read_csv('./2025_Problem_C_Data/summerOly_programs.csv',encoding='windows 1252')
ProfileReport(programs).to_file('./report/programs.html')