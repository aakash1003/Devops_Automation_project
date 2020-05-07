import os
import webbrowser

print("Testing is successful (yes/no)")
ch = input()

if ch == 'yes':
    os.system("curl --user 'admin:jenkins@123' http://192.168.43.194:8080/job/merge/build?token=aksharma")
    print("Congratulation your code is successfully uploaded to the production server")
elif ch == no:
    print("testing is failed")
else:
    print("wrong option, please choose a valid option")
