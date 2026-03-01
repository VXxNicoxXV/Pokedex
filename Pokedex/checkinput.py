class CheckInput:
    def isNumber(user_input):
        if user_input == " ":
            return False
        try:
            user_input = int(user_input)
        except ValueError:
            return False
        return True
    
    def is_valid_name(name):
        if not name.strip():
            return False
        return all(word.isalpha() for word in name.split())
    
    def is_valid_nickname(nickname):
        if not nickname.strip():
            return False
        if " " in nickname.strip():
            return False