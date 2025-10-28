print("Assignment 1 :\n")
list = (10,20,30,40,50,60,70,80,90,100)
print("Question 1 Solutions :-")
print(" 1- Answer:", list[0])
print(" 2- Answer:", list[-1])
print(" 3- Answer:", list[-6])
print(" 4- Answer:", list[::-1])
print(".............................................\n")

list_std=(56,78,34,60,49,90,88,100,45,23)
avg=sum(list_std)/len(list_std)
print("Question 2 Solutions :- Above average i.e. greater than",avg,"are:")
for i in list_std:
   if i>avg:
       print(i)
print(".............................................\n")

colors = ['red', 'green', 'blue', 'yellow', 'black','white']
print("Question 3 Solutions :-")
print("Answer 1:", colors[1:5:3])
colors.remove('yellow')
colors.insert(3,'purple')
print("Answer 2:", colors)
print(".............................................\n")

student =('Alice',17,'Physics',91.5)
Name,Age,Subject,Marks = student
print("Question 4 Solutions :-")
print("Name:",Name)
print("Age:",Age)
print("Subject:",Subject)
print("Marks:",Marks)
print(".............................................\n")

team_A={'Alice','Bob','Charlie'}
team_B={'Charlie','David','Eve'}
print("Question 5 Solutions :-")
print("Union of both team:", team_A | team_B)
print("Common team member of both team:", team_A & team_B)
print("Members unique to team A only:", team_A - team_B)
print(".............................................\n")

string = 'Mississippi'
print("Question 6 Solutions :-")
print("Unique characters are : ",set(string))
print(".............................................\n")

profile = {
      "user": {
          "name": "Alice",
          "preferences": {
              "theme": "dark",
              "notifications": True
          }
      }
}
print("Question 7 Solutions :-")
print("Before update:",profile)
profile['user']['preferences']['theme']='light'
print("After update:",profile)
print(".............................................\n")