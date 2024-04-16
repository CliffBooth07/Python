# import random for getting random int value
import random
# user=True for infinite while loop
user=True
# list for storing questions
question=['''What is the captial of Australia
a) Sydney
b) Melbourne
c) Canberra
d) Perth''',
'''Who painted the Mona Lisa?
a) Vincent van Gogh
b) Pablo Picasso
c) Leonardo da Vinci
d) Michelangelo''',
'''What is the largest ocean in the world?
a) Atlantic Ocean
b) Indian Ocean
c) Arctic Ocean
d) Pacific Ocean''',
'''Which planet is known as the "Red Planet"?
a) Venus
b) Mars
c) Jupiter
d) Saturn''',
'''Who wrote the play "Romeo and Juliet"?
a) William Shakespeare
b) Jane Austen
c) Charles Dickens
d) F. Scott Fitzgerald''']
# list for storing answers
answers_word=["Canberra","Leonardo da Vinci","Pacific Ocean","Mars","William Shakespeare"]
answers_option=["c","c","d","b","a"]
# while loop with user sets as True
while (user):

  # it check len of question list is equal to 0 or not
  if(len(question)!=0):
    # it get random index from question list
    key=random.randint(0,len(question)-1)
    print(question[key])
    # user give input for answer
    answer=input("Enter your answer: ")
    if(answer==answers_word[key] or answer==answers_option[key]):
      print("That's Right")
      # remove the question are already appeared by using their index and pop function
      question.pop(key)
      answers_word.pop(key)
      answers_option.pop(key)
    # if answer is wrong then it will print you lose and user value get change and infinite loop will stop
    else:
      print("You lose")
      user=False
    # if all answer are right and no more question are left then it will print you win and user value get change and infinite loop will stop
  else:
    print("You Win")
    user=False