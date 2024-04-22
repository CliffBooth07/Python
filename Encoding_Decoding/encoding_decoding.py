#Logic used for encoding and decoding
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

#random module to get random integer
import random
#ask user what he want to do with their message
user_input=input("What do you want (Encode(e) or Decode(d)):")
encode_list=[]
decode_list=[]
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
first=""
last=""
encoded=""
decoded_message=""
#if user wants to encode
if user_input=="e":
  print("---Encode---")
  #enter your message
  message=input("Enter your message for encoding:")
  if(len(message)>=3):
    #converting string to list
    for i in message:
      encode_list+=i
    # print(encode_list)
    #add 0 index element to last 
    encode_list.append(encode_list[0])
    #remove 0 index element
    encode_list.pop(0)
    # print(encode_list)
    #used to convert list to string
    for i in encode_list:
      encoded+=i
    #used to make random string
    for i in range(0,3):
      a=alpha[random.randint(0,len(alpha)-1)]
      first+=a
    for i in range(0,3):
      a=alpha[random.randint(0,len(alpha)-1)]
      last+=a

    #print the combination of random string and our message
    print(f"Your message has been encoded: {first+encoded+last}")
  else:
    #reverse the string
    endoded=message[1]+message[0]
    print(f"Your message has been encoded: {endoded}")

#if user wants to decode
elif user_input=="d":
  print("---Decode---")
  #enter your message
  message=input("Enter your message for decoding:")
  if(len(message)>=3):
    #converting string to list
    for i in message:
      decode_list+=i

    #for loop will run 3 time and remove 3 elements from front and back of string
    for i in range(3):
      decode_list.pop(0)
      decode_list.pop(-1)

    #use to insert last element to 0 index
    decode_list.insert(0,decode_list[-1])
    #remove last element
    decode_list.pop(-1)
    #use to convert list to string
    for i in decode_list:
      decoded_message+=i
    print(f"Here is your decoded message: {decoded_message}")
    
  else:
    #reverse the string
    endoded=message[1]+message[0]
    print(f"Your message is decoded: {endoded}")



# a=input()
# # # for i in a
# # p1=a.slice(0,1)
# # print(p1)
# # # b=a.slice(i,len(a))
# # # print(b)

# endoded=a[1]+a[0]
# print(endoded)