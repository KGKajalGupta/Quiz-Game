print("\n <------------ Welcome in Computer Quiz Game ------------>")
print("\nRules: \nThere are 6 different type of quiz available\nType the option in which you want to participate\nIn each Round there are 10 Questions")
print("Each question has 4 options. \nYou have to write correct option in given space")
class Questions:
    Python_question1 = ["\n1. What is Python \n\na)A high-level programming language \nb)A computer hardware component \nc) A type of snake \nd)A software development tool",
                        "\n2. What is the purpose of the \"self\" parameter in a Python class method? \n\na)It refers to the current instance of the class \nb)It allows access to private variables \nc)It is used to define class-level variables \nd)It indicates a static method",
                        "\n3. What is the difference between a shallow copy and a deep copy in Python?? \n\na)A shallow copy creates a new object, while a deep copy refers to the same object \nb)A shallow copy copies only the references of nested objects, while a deep copy creates new copies of nested objects \nc)A shallow copy is used for immutable objects, while a deep copy is used for mutable objects \nd)There is no difference; both terms refer to the same concept",
                        "\n4. Which data type is used to store a sequence of characters in Python? \n\na)string \nb)integer \nc)float \nd)boolean",
                        "\n5. What is the purpose of the \"super()\" function in Python? \n\na)It calls the parent class constructor \nb)It terminates the execution of a program \nc)It imports modules from the standard library \nd)It creates a new instance of a class",
                        "\n6. What is the difference between a module and a package in Python? \n\na)A module is a collection of classes, while a package is a collection of modules \nb)A module is a single file, while a package is a directory with multiple files \nc)A module is used for testing, while a package is used for deployment \nd)There is no difference; both terms are used interchangeably",
                        "\n7. What is the result of 2 ** 3 ** 2 \n\na)1026 \nb)512 \nc)64 \nd)128",
                        "\n 8.What is the difference between a list and a tuple in Python? \n\na)A list is mutable, while a tuple is immutable \nb)A list can store elements of different data types, while a tuple can only store elements of the same data type \nc)A list is ordered, while a tuple is unordered \nd)There is no difference; both terms refer to the same data structure",
                        "\n9. What does the \"@\" symbol typically represent in the context of decorators in Python? \n\na)It is used to define a decorator function \nb)It is used to apply a decorator to a function or class \nc)It is used to indicate a property of a class \nd)It is used to separate elements in a tuple",
                        "\n10. What is the result of (\"Hello\" + \"World\")*2 in Python? \n\na)HelloWorldHelloWorld \nb)HelloWorld HelloWorld \nc)Hello World Hello World \nd)None of these"]

    Python_ans1 = ["a) A high-level programming language", "a) It refers to the current instance of the class", "b) A shallow copy copies only the references of nested objects, while a deep copy creates new copies of nested objects", "a) string", "a) It calls the parent class constructor", "b)A module is a single file, while a package is a directory with multiple files", "b) 512", "a) A list is mutable, while a tuple is immutable","b) It is used to apply a decorator to a function or class", "a) HelloWorldHelloWorld"]

    Programming_question = ["\n1.Which of the following is not a programming language? \n\na)Python \nb)HTML \nc)Java \nd)SQL",
                            "\n2. Which keyword is used to define a constant in C programming: \n\na)const \nb)final \nc)constant \nd)def",
                            "\n3. In Java, which access modifier makes a member accessible only within? \n\na)public \nb)private \nc)protected \nd)static",
                            "\n4. Which programming language is primarily used for developing Android? \n\na)Java \nb)Python \nc)C++ \nd)Ruby",
                            "\n5. Which sorting algorithm has best average-case time complexity? \n\na)Bubble Sort \nb)Insertion Sort \nc)Quick Sort \nd)Selection Sort",
                            "\n6. What is the purpose of construct in object-oriented programming? \n\na)To create new instances of a class \nb)To define private class members \nc)To override superclass methods  \nd)To implement static methods",
                            "\n7. Which of the following is an example of a low-level programmin? \n\na)Java \nb)Python \nc)C# \nd)Assembly",
                            "\n8. What does the acronym SQL stand for? \n\na)Structured Query Language \nb)Simple Query Language \nc)Secure Query Language \nd)Srandard Query Language",
                            "\n9. What is the term 'DRY' stand for in software development? \n\na)Don't Repeat Yourself \nb)Document, Reciew, Yield \nc)Design, Run, Yield \nd)Debug, Refactor, Yield",
                            "\n10. What is the perpose of an 'else' statement in an 'if-else' construct? \n\na)To check an additional condition \nb)To terminate the program \nc)To define the main program logic \nd)To provide an alternative path of execution"]

    Programming_ans = ["b) HTML", "a) const", "b) Private", "a) Java", "c) Quick Sort", "a) To create new instances of a class", "d) Assembly", "a) Structure Query Language", "a) Don't Repeat Yourself", "d) To provide alternative path of execution"]

    World_question = ["\n1. Which country is the largest archipelago in the world? \n\na)Indonesia \nb)Philippines \nc)Japan \nd)Maldives",
                      "\n2. In which country would you find the ancient city of Petra? \n\na)Jordan \nb)Egypt \nc)Lebanon \nd)Iraq",
                      "\n3. What is the largest country in Africa by land area? \n\na)Algeria \nb)Sudan \nc)Egypt \nd)Democratic Republic of the Congo",
                      "\n4. Which European city is divided by the Bosphorus Strait, separating its European and Asian sides? \n\na)Istanbul \nb)Athens \nc)Rome \nd)Berlin",
                      "\n5. Which African country is known as the 'Pearl of Africa'?\n\na)Kenya \nb)Uganda \nc)Ethiopia \nd)Tanzania",
                      "\n6. Which river is the longest in South America? \n\na)Amazon River \nb)Nile River \nc)Orinoco River \nd)Parana River",
                      "\n7. Which country is the largest producer of coffee in the world? \n\na)Brazil \nb)Colombia \nc)Ethiopia \nd)Vietam",
                      "\n8. Which Asian country is known as the 'Land of Thunder Dragon'? \n\na)Nepal \nb)Bhutan \nc)Myanmar \nd)Sri Lanka",
                      "\n9. What is the capital city of Canada? \n\na)Ottawa \nb) Toronto \nc)Vancouver \nd) Montreal",
                      "\n10. Which country is the world's leading producer of oil? \n\na)Saudi Arabia \nb) Russia \nc)United States \nd) Iraq"]

    World_ans = ["a) Indonesia", "a) Jordan", "a) Algeria", "a) Istanbul", "a) Uganda", "a) Amazon River", "a) Brazil", "b) Bhutan", "a) Ottawa", "a) Soudi Arebia" ]

    Plant_question = ["\n1. Which of the following is NOT a primary function of plant roots? \n\na)Absorbing water and nutrients \nb)Anchoring the plant in the ground \nc)Photosynthesis \nd)Storing food and nutrients",
                      "\n2. The process by which green plants convert sunlight into energy is called: \n\na)Respiration \nb)Photosynthesis \nc)Transpiration \nd)Reproduction",
                      "\n3. Which part of the plant is responsible for the production of seeds?\n\na)Leaves \nb)Roots \nc)Flowers \nd)Stems",
                      "\n4. The primary function of plant leaves is:\n\na)Absorbing sunlight \nb)Anchoring the plant in the ground \nc)Absorbing water and nutrients \nd)Storing food and nutrients",
                      "\n5. Which of the following is a reproductive structure of a flowering plant?\n\na)Stamen \nb)Petiole \nc)Rhizome \nd)Bilb",
                      "\n6. The process by which water evaporates from the leaves of a plant is called:\n\na)Transpiration \nb)Respiration \nc)Photosynthesis \nd)Absorption",
                      "\n7. Which part of the plant absorbs water and nutrients from the soil?\n\na)Leaves \nb)Roots \nc)Flowers \nd)Stems",
                      "\n8. What is the male reproductive part of a flower called?\n\na)Stamen \nb)Pistil \nc)Sepal \nd)Petal",
                      "\n9. Which of the following is an example of a flowering plant?\n\na)Oak tree \nb)Fern \nc)Cactus \nd)Rose bush",
                      "\n10. What is the primary pigment responsible for capturing sunlight in plants?\n\na)Chlorophyll \nb)Carotene \nc)Anthocyanin \nd)Xanthophyll"]

    Plant_ans = ["c) Photosynthesis", "b) Photosynthesis", "c) Flowers", "a) Absorbing sunlight", "a) Stamen", "a)Transpiration","b)Roots", "a)Stamen", "d)Rose bush", "a)Chlorophyll"]

    Animal_question = ["\n1. Which of the following is a warm-blooded animal?\n\na)Snake \nb)Fish \nc)Penguin \nd)Frog",
                      "\n2. Which animal does not have a backbone?\n\na)Cat \nb)Dolphin \nc)snake \nd)Jellyfish",
                      "\n3. What is the largest species of shark?\n\na)Tiger shark \nb)Hammerhead shark \nc)Great white shark \nd)Whale shark",
                      "\n4. Which of the following animals is a marsupial?\n\na)Koala \nb)Tiger \nc)Hippopotamus \nd)Rhino",
                      "\n5. Which animal has the longest lifespan?\n\na)Elephant \nb)Galapagos tortoise \nc)Bowhead whale \nd)African Grey parrot",
                      "\n6. What is the largest species of bat?\n\na)Fruit bat \nb)Vampire bat \nc)Flying fox \nd)Brown bat",
                      "\n7. Which animal has the ability to change its color to blend with its surroundings?\n\na)Chameleon \nb)Octopus \nc)Cuttlefish \nd)Anglerfish",
                      "\n8. What is the world's smallest mammal?\n\na)Bat \nb)Shrew \nc)Mouse \nd)Hedgehog",
                      "\n9. Which of the following animals is a ruminant?\n\na)Horse \nb)Sheep \nc)Cat \nd)Dog)",
                      "\n10. What is the largest living species of lizard?\n\na)Komodo dragon \nb)Gila monster \nc)Green iguana \nd)Monitor lizard"]

    Animal_ans = ["c) Penguin", "d)Jellyfish","d) Whale shark", "a)Koala", "b)Galapagos tortoise", "c) Flying fox", "a) Chameleon", "c) Shrew","d) Sheep ", "a) Komodo dragon"]

    Sport_question = ["\n1. Which ancient civilization is credited with the invention of the Olympic Games?\n\na)Egyptian civilization \nb)Greek civilization \nc)Roman civilization \nd)Mayan civilization",
                      "\n2. Which sport originated in Scotland and is often referred to as \"the gentlemen's game\"?\n\na)Tennis \nb)Cricket \nc)Golf \nd)Rugby",
                      "\n3. Who is considered the father of the modern Olympic Games?\n\na)Pierre de Coubertin \nb)Avery Brundage \nc)Thomas Bach \nd)Juan Antonio Samaranch",
                      "\n4. Which sport was first included in the Olympic Games in 1900 and was the only sport where women were allowed to participate?\n\na)Tennis \nb)Figure skating \nc)Gymnastics \nd)Archery",
                      "\n5. Which country is known for popularizing the sport of sumo wrestling?\n\na)China \nb)Mongolia \nc)Japan \nd)South Korea",
                      "\n6. Which sport was introduced to the Olympics in 1964 and combines elements of martial arts and boxing?\n\na)Judo \nb)Taekwondo \nc)Fencing \ndWrestling)",
                      "\n7. Which famous ancient Greek philosopher was also an Olympic wrestling champion?\n\na)Socrates \nb)Plato \nc)Aristotle \nd)Pythagoras",
                      "\n8. In which year were the first modern Paralympic Games held?\n\na)1948 \nb)1960 \nc)1972 \nd1980)",
                      "\n9. Which Indian hockey player is known as \"The Wizard\" and is considered one of the greatest hockey players of all time?\n\na)Dhyan Chand \nb)Dhanraj Pillay \nc)Balbir Singh Sr. \nd)Milkha Singh)",
                      "\n10. Which Indian athlete won the country's first individual Olympic gold medal in 2008?\n\na)Abhinav Bindra \nb)Mary Kom \nc)Sushil Kumar \nd)P. V. Sindhu"]

    Sport_ans = ["b) Greek civilization","c)Golf","a) Pierre de Coubertin", "d) Archery", "c) Japan", "a)Judo","c) Aristotle", "b) 1960", "a) Dhyan Chand", "a)Abhinav Bindra"]


class Excecute:
    def __init__(self, category):
        self.point = 0
        self.category = category

    def ques_ans(self, ques, ans):
        for i in range(10):
            print(ques[i])
            self.check_ans(ans, i)
        self.show_result()

    def check_ans(self, ans1, i):
        print("")
        a = input("Enter the correct option : ")
        if a == ans1[i][0]:
            print("\nCongratulation! Correct Answer \U0001F929")
            self.point += 1
        else:
            print("\nSorry! Wrong Answer \U0001F622 \nRight Answer is : ", ans1[i])

    def check_category(self):
        if self.category==1:
            self.ques_ans(Questions.Python_question1, Questions.Python_ans1)
        elif self.category==2:
            self.ques_ans(Questions.Programming_question, Questions.Programming_ans)
        elif self.category==3:
            self.ques_ans(Questions.World_question, Questions.World_ans)
        elif self.category == 4:
            self.ques_ans(Questions.Plant_question, Questions.Plant_ans)
        elif self.category==5:
            self.ques_ans(Questions.Animal_question, Questions.Animal_ans)
        elif self.category==6:
            self.ques_ans(Questions.Sport_question, Questions.Sport_ans)

    def show_result(self):
        print(f"\nYou got {self.point} points\n")
        ask = input("Do you want to play again : ")
        if ask in ("Y", "y", "YES", "yes", "Yes", "YEs", "yEs", "yES", "yeS"):
            Input()
        else:
            print("\nWell Played \nHave a nice day \nThank You \U0001F600")
            return


class Input:
    def __init__(self):
        print("\nOn which topic, Do you want to play Quiz? \n1. Python Language \n2. Programming \n3. World \n4. Plants \n5. Animals \n6. Sports Spectacular\n")
        ans = int(input("Enter your option number : "))
        p = Excecute(ans)
        p.check_category()
Input()



