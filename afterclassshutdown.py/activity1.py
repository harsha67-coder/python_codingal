def shutdown():
    a=input("enter wether to shut down code or continue (Y/N)")
    if a=='Y' or a=='y':
        print("shutting down code")
    elif a=='N' or a=='n':
        print("abort shut down")
    else:
        print("sorry")

shutdown()