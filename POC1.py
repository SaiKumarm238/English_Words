#!/usr/bin/env python
# coding: utf-8

# ```
# 1. Write a function :
# a. Number to word
# Eg : 1 > one
# 
# b. Word to number
# Eg: one > 1
# 
# c. Number to roman
# Eg : 11 > XI
# 
# d. Nearest palindrome to a given number
# 
# e. Age calculation
# Eg : month. Day .year > year month days hours min and sec
# ```

# In[6]:


import num2words
from word2number import w2n
import roman


# In[9]:


def num_word():
    x = int(input("Enter a number :"))
    return num2words.num2words(x)


# In[10]:


def word_to_num():
    x = input("Enter a number in words: ")
    return w2n.word_to_num(x)


# In[11]:


def num_to_roman():
    num = int(input("Enter a Number : "))
    return roman.toRoman(num)


# In[12]:


def nearest_palindrome_to_a_given_number():
    x = int(input("Enter a Number : "))
    x= x+1
    while x > 0:
        st = str(x)
        if st[::-1] == st:
            return f"Next Palindrome of Given Number is : {st}"
        x +=1 


# In[23]:


def age_calculation():
    '''this function takes input as date/month/year format and returns years,months,days,hours,minutes,seconds'''
    import datetime
    user_name = input("Enter your name:")
    while True:
        user_input=input("Hi {}! Do you want to calculate the age? if yes then enter yes or y if not enter no or no:".format(user_name.title()))
        user_input = user_input.strip().lower()
        if user_input=="y" or user_input == 'yes':
            try:
                birth_date = input("Enter your date of birth in date/month/year format:")
            except:
                print("The birth_date should be in date/month/year format only")
                birth_date = input("Enter your date of birth in date/month/year format:")
            else:
                currentDate = datetime.datetime.now() 
                birth_date= datetime.datetime.strptime(birth_date,'%d/%m/%Y')
               
                total_days = currentDate - birth_date
                years = ((total_days.days)//(365))
                yearsInt=int(years)
                rem_days = total_days.days - int(years) * 365
                '''Function to check the number of leap years from birthdate to current year.'''
                def checkYear(year): 
                    return (((year % 4 == 0) and
                             (year % 100 != 0)) or
                             (year % 400 == 0))  
                   
                count = 0 
                for yr in range(birth_date.year,currentDate.year): 
                    if checkYear(yr): 
                        count += 1
                        
                '''Instead of count I can directly subtract one day each time whenever the year is leap year from remaining days'''
                rem_days -= count
                d = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
                months = 0
                
                '''print("CMonth:",currentDate.month)
                print("BMonth:",birth_date.month)'''
                ''' Condition to find the number of months '''
                if birth_date.month > currentDate.month:
                    if rem_days >= 30:
                        for num in range(birth_date.month,len(d)+1):
                            rem_days -= d[num]
                            months += 1
                        for num in range(1,currentDate.month):
                            rem_days -= d[num]
                            months += 1
                    while rem_days >= 30:
                        if rem_days >= 30:
                            rem_days -= 30
                            months += 1
                elif birth_date.month < currentDate.month:
                    if rem_days >= 30:
                        for num in range(birth_date.month,currentDate.month):
                            rem_days -= d[num]
                            months += 1
                    while rem_days >= 30:
                        if rem_days >= 30 :
                            rem_days -= 31
                            months += 1                 
                hours = currentDate.hour
                minutes = currentDate.minute
                seconds = currentDate.second
                print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} minutes, {5:d} seconds old.'.format(yearsInt,months,rem_days,hours,minutes,seconds))
        elif user_input == "n" or user_input == 'no':
            break
        else:
            print("input should be either yes or y and no or n")


# In[20]:


print("Enter a Option Below")
print("1.num_word\n2.word_to_num\n3.num_to_roman\n4.nearest_palindrome_to_a_given_number\n5.age_Calculation")
user_input = input("Enter a your Option")
while True:
    if user_input == "1":
        print(num_word())
        break
    elif user_input == "2":
        print(word_to_num())
        break
    elif user_input == "3":
        print(num_to_roman())
        break
    elif user_input == "4":
        print(nearest_palindrome_to_a_given_number())
        break
    elif user_input == "5":
        print(age_calculation())
        break


# In[ ]:




