def sec_to_hours(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    print(f"{a} hours {b} mins {c} seconds")
print(sec_to_hours(2200))
