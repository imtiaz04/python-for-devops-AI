import psutil

def get_cpu_threshold():

    user_cpu = int(input("Enter cpu threshold"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu%: ", current_cpu)

    if current_cpu > user_cpu:

        print("cpu alert email sent...")
    else:
        print("cpu usage is safe")


def get_disk():

    user_disk = float(input("enter your system disk (%): "))


    disk = psutil.disk_usage("/")
    current_disk_percent = disk.percent

    print("present disk usage:",current_disk_percent, "%")


    if current_disk_percent< user_disk:
        print("system healthy")
    else:
        print("not healthy")

# cpu and disk monitoring script
# cpu and disk mon

###############################################
# def get_disk():
#     user_disk = float(input("enter your system disk (%): "))

#     disk = psutil.disk_usage("/")     # returns sdiskusage object
#     current_disk_percent = disk.percent

#     print("present disk usage:", current_disk_percent, "%")

#     if current_disk_percent < user_disk:
#         print("system healthy")
#     else:
#         print("not healthy")






get_cpu_threshold()
get_disk()           






