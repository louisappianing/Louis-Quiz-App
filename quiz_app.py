#This is a Simple Quiz App I'm trying to make from a tutorial I watch

#Importing Time Function
import time

#These are the Questions
questions = ["",
             #Africa
             "What is the capital city for Ghana?",
             "What is the capital city for Angola?",
             "What is the capital city for Benin?",
             "What is the capital city for Nigeria?",
             "What is the capital city for Egypt?",
             #Asia
             "What is the capital city for China?",
             "What is the capital city for India?",
             "What is the capital city for Japan?",
             "What is the capital city for South Korea?",
             "What is the capital city for Bangladesh?",
             #North America
             "What is the capital city for Canada?",
             "What is the capital city for United States?",
             "What is the capital city for Jamaica?",
             "What is the capital city for Cuba?",
             "What is the capital city for Mexico?",
             #South America
             "What is the capital city for Brazil?",
             "What is the capital city for Argentina?",
             "What is the capital city for Uruguay?",
             "What is the capital city for Columbia?",
             "What is the capital city for Peru?",
             #Europe
             "What is the capital city for France?",
             "What is the capital city for Spain?",
             "What is the capital city for Germany?",
             "What is the capital city for Italy?",
             "What is the capital city for Portugal?",
             #Australia & Oceania
             "What is the capital city for Australia?",
             "What is the capital city for Samoa?",
             "What is the capital city for New Zealand?",
             "What is the capital city for Fiji?",
             "What is the capital city for Vanuatu?",]

#These are the letters to the correct Answers
answers = ["",
           #Africa
           "B", #Accra
           "A", #Luanda
           "B", #Porto Novo
           "C", #Abuja
           "D", #Cairo

           #Asia
           "B", #Beijing
           "A", #New Delhi
           "D", #Tokyo
           "B", #Seoul
           "D", #Dhaka

           #North America
           "C",#Ottawa
           "D",#Washingto Dc
           "C",#Kingston
           "B",#Havana
           "D",#Mexico City
           
           #South America
           "D",#Brasilia
           "A",#Buenos Aires
           "C",#Montevideo
           "C",#Bogota
           "D",#Lima
           
           #Europe
           "D",#Paris
           "D",#Madrid
           "C",#Berlin
           "B",#Rome
           "A",#Lisbon

           #Australia
           "C",#Australia
           "B",#Apia
           "D",#wellington
           "A",#Suva
           "C"]#Port Vila

#These are the Possible Answers A, B anc C
options = ["",
           #Africa
           "   A. Lome  B. Accra  C.Maseru   D. Port Novo"  ,
           "   A. Luanda  B. Cairo  C. Gabon   D. Yaounde",
           "   A. Austria  B.  Porto Novo  C. Tripoli  D. Addis Ababa",
           "   A. Lusaka  B. Bamako  C. Abuja  D. Banjul",
           "   A. Washington DC  B. Guinea  C. Rabat  D. Cairo",

           #Asia
           "   A. Accra  B. Beijing  C.Muscat  D. Seoul",
           "   A. New Delhi  B. Tokyo  C. Dhaka   D. Nicosia",
           "   A. Addis Ababa  B. Moscow   C. Beirut  D. Tokyo",
           "   A. Kuwait City  B. Seoul  C. Paris   D. Jakarta",
           "   A. Beirut  B. Rabat  C. Male   D. Dhaka",
           
           #North America
           "   A. Belmopan  B. Roseau   C. Ottawa   D. St. John's",
           "   A. Port-au-Prince   B. Castries    C. Nassau   D. Washington Dc",
           "   A. Panama City  B. Caracas C. Kingston   D. Managua",
           "   A. St. John's   B. Hava  C. Kingstown   D. Nassau",
           "   A. Managua  B. Port of Spain   C. San Jose   D. Mexico City",
           
           #South America
           "   A.Santiago  B. Montevideo  C.Caracas   D. Brasilia ",
           "   A. Buenos Aires  B. Port of Spain   C. Asuncion   D. Quito",
           "   A. Caracas B. Lima  C. Montevideo    D. Santiago",
           "   A. Paramaribo  B. Caracas  C. Bogota   D. Quito",
           "   A. Port of Spain  B. Santiago  C. Georgetown   D. Lima",
           
           #Europe
           "   A. Vienna  B. Tirana   C. Valletta   D. Paris",
           "   A. Yerevan  B. London  C. Baku   D. Madrid",
           "   A. Moscow  B. Lisbon   C. Berlin   D. Vienna",
           "   A. Prague B. Rome  C. Monaco   D. London",
           "   A. Lisbon B. Ankara   C. Madrid  D. Kiev",

            # Australia
            "   A. Funafuti B. Suva   C.Canberra   D. Vatican City",
            "   A. Honiara  B.Apia  C. Majuro   D. Bern",
            "   A. Ankara  B. Palikir  C. Suva   D. Wellington",
            "   A. Suva  B. Honiara   C. Bern   D. Majuro",
            "   A. Funafuti B. Melekeok  C. Port Vila   D.Palikir "]




# The Body
print()
print()
print("       ====================================================")
print("                        LOUIS QUIZ APP                     ")
print("       ====================================================")

print()
print("       ============COUNTRIES AND THEIR CAPITALS============")

print()

#Storing score of each question (correct or wrong)

# This is stores the time when quiz started


#Replay options
Y = True #Y for Yes
N = False #N for No
while True:
    #Stores score of the quiz
    score = 0
    #Start timer when quiz begins
    start = time.time()

#Loop through each question and answer
    for i in range(1, len(questions)):  #The length of questions 1 to 11
        print(f"{i}.",questions[i])     #Display questions
        print(f"{options[i]}")          #Display possible answers
        usr_ans = input("   Answer: ")  #Takes user's answers

    #Comparing user's answers with correct
        if usr_ans.lower() == answers[i].lower():   #The lower() checks the case of the users input
            print("Correct")
            score = score + 1            #Add 1 mark when correct
            print()

        else:
            print("Incorrect")
            score = score + 0           #No mark when incorrect
            print()

    #Calculate percentage of score
    perc = (score / 30) * 100

    print("       ====================================================")

    #Display percentage of total score
    print(f"        Quiz Complete! Your Score : {perc:.0f} / 100 ")


    #Grading system of the quiz
    if perc >= 80:
        print("         Grade A\n")
    elif perc >= 70 <= 79 :
        print("         Grade B\n")
    elif perc >= 60 <= 69:
        print("         Grade C\n")
    elif perc >= 50 <= 59:
        print("         Grade D\n")
    else:
        print("         Grade F\n")

    #End timer when quiz end
    end = time.time()
    #Calculate time taken
    total_time = end - start

    #Converts seconds to minutes
    minutes = total_time // 60
    #Remaing seconds
    seconds = total_time % 60

    #Display Time Taken
    print(f"        Time Taken  {minutes} min {seconds:.0f} sec \n")  #Displays the total spent to finish the quiz

    print("       Keep Practicing!!!!!")
    print("       ====================================================\n")

    #Display replay feature
    play_again = input("Play again Y/N: ")
    if play_again.lower() == "N".lower():
        print()
        print("Thanks for playing.\n See You Later")
        exit()

