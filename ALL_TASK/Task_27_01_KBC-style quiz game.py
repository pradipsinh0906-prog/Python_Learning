class KBC:
    def __init__(self):
        self.questions = [
            {
                "question": "Who is the Prime Minister of India?",
                "options": ["A. Narendra Modi", "B. Rahul Gandhi", "C. Amit Shah", "D. Arvind Kejriwal"],
                "answer": "A",
                "amount": 1000
            },
            {
                "question": "Which language is used to create websites?",
                "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
                "answer": "B",
                "amount": 5000
            },
            {
                "question": "What is the capital of India?",
                "options": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
                "answer": "C",
                "amount": 10000
            },
            {
                "question": "Which company owns Instagram?",
                "options": ["A. Google", "B. Microsoft", "C. Meta", "D. Twitter"],
                "answer": "C",
                "amount": 50000
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
                "answer": "B",
                "amount": 100000
            },
            {
                "question": "Who invented Python?",
                "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
                "answer": "C",
                "amount": 500000
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["A. func", "B. define", "C. def", "D. function"],
                "answer": "C",
                "amount": 1000000
            },
            {
                "question": "What is the result of 10 // 3?",
                "options": ["A. 3.33", "B. 3", "C. 4", "D. Error"],
                "answer": "B",
                "amount": 2500000
            },
            {
                "question": "Which data type is immutable?",
                "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
                "answer": "D",
                "amount": 5000000
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
                "answer": "C",
                "amount": 70000000
            }
        ]
        
        self.total_amount = 0
        
    def play_game(self):
        print("Welcome to KAUN BANEGA CROREPATI \n")
        
        for i in range(len(self.questions)):
            q = self.questions[i]
            print(f"\nQ{i+1}: {q['question']}")
            
            for opt in q["options"]:
                print(opt)
                
            user_ans = input("Enter your answer (A/B/C/D): ").upper()
            
            if user_ans == q["answer"]:
                self.total_amount = q["amount"]
                print("Correct Answer!")
                print(f"You Won ₹{self.total_amount:,}")
                
                self.shoutout(i + 1)
            
            else:
                print("Wrong Answer!")
                print(f"Total Winning Amount : ₹{self.total_amount:,}")
                break
        
        else:
            print("\n CONGRATULATIONS ")
            print("You are a CROREPATI!")
            print(f"Total Winning Amount: ₹{self.total_amount:,}")
            
    def shoutout(self, q_no):
        if q_no <= 3:
            print("Good Start! Keep Going!")
        elif q_no <= 6:
            print("Excellent! You are playing well!")
        elif q_no <= 9:
            print("Brilliant! Almost a Cropati!")
        else:
            print("LEGEND! 7 CRORE JEET LIYE!")
            
game = KBC()
game.play_game()