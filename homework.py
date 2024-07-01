# Name=input("enter your name:")
# email=input("enter your email:")
# password=input("enter your password:")

# user_dict = {}
 
# num_entries = int(input("Enter the number of entries you want to add: "))
 
# for i in range(num_entries):
#     email = input("Enter email ")
#     password = input("Enter password: ")
#     user_dict[email] = password
 
# print(user_dict)

c_m = {
'lod':123,
'ele':345,
'ali':456,
'abq':567,
'amr':678
}
c_m.get("login")
login = input("please enter user name: ")
password = input("please enter your password: ")

for k,v in c_m():
   if k == login and v == password:
      print("Welcome back!")

   else:
      print("Something went wrong")

