"""
노드 클래스
"""
class Node:
    __slots__ = ["__value", "__next"]

    def __init__(self,value,next=None):
        self.__value = value
        self.__next = next
    
    # value를 리턴.
    def get_value(self):
        return self.__value 
    
    # next를 리턴.
    def get_next(self):
        return self.__next

"""
노드로 구현한 스택 자료구조

*** 처음 구현 했을 때, pop 함수가 자꾸 이상하게 나와서, 그 부분은 다시 복습했고, 나머지는 처음해본거! *** 
*** 거의 외우다시피 한거라 계속 봐야할 것 같아요. *** 
"""

class Stack:
    __slots__ = ["__element", "__length"]

    def __init__(self):

        self.__element = None
        self.__length = 0
    

    # 스택의 길이를 구하는 매소드.
    def get_length(self):
        return self.__length

    # push: 스택에 데이터를 추가하는 매소드. 
    def push(self,data):
        node = Node(data,self.__element)
        self.__element = node # next가 element가 됨.
        self.__length += 1

    # pop: 스택에서 가장 위에있는 데이터를 빼내는 메소드.
    def pop(self):
        data = self.__element
        value = data.get_value() # element에서 값을 추출.
        self.__element = data.get_next() # next의 값이 현재의 값으로 변환.
        self.__length -= 1
        return value
    # 마지막 데이터를 리턴. 길이가 줄어들진 않음.
    def peek(self):
        value = self.__element.get_value()
        return value 
    # 만약 스택이 비어있으면 true 아니면 false.
    def isEmpty(self):
        if self.__length == 0:
            return True
        else:
            return False

    # 스택의 출력될때 돕는 매소드.
    def __str__(self):
        parenthesis = '[' # 스택이 처음 [ 로 표시된다. 
        data = self.__element
        if data is not None:
            parenthesis += str(data.get_value())
            while data is not None:
                parenthesis += ", " + str(data.get_value())
                data = data.get_next()
        parenthesis += "]"
        return parenthesis


# 메인 함수
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("selfish Gene")
    stack.push(True)
    print(stack)
    a = stack.pop()
    b = stack.pop()
    c = stack.peek()
    print(a)
    print(b)
    print(c)
    print(stack)


    
    


if __name__ == "__main__":
    main()
        

