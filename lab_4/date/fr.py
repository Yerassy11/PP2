from datetime import datetime
f_data=datetime(2025,2,1,12,0)
s_data=datetime(2025,2,1,12,30)
diff=f_data-s_data
seconds=diff.total_seconds()
print(diff)
