class ChatMessageSubstring:
    def __init__(self):
        pass
    def solution(self, chatMessage):
        count = 0
        n = len(chatMessage)
        vowel = ["a","e","i","o","u"]
        if n<3:
            return count
        for i in range(n-2):
            for char in chatMessage[i:i+3]:
                if char.lower() in vowel:
                    count+=1
                    break                  
        return count