# Task1.

from datetime import datetime


class Chat:
    '''A class to create chat for conteining messages from user
    
    Methods:
        recieve(): to add message to chat
        show_last_message(): to obtain information about last message in chat
        show_chat(): to show all messages and their information in chat from 
                     the newest to the oldest one
        str_to_date(): to transform date in string format to datetime format
        get_history_from_time_period(): to show all messages and their information 
                                        for defined time period  
    '''
    
    
    def __init__(self, period_history=None):
        '''Constructs all the necessary attributes for the Chat object

        Parameters:
            chat_history (list): contains all messages in the chat
        '''
        
        
        if period_history:
            self.chat_history = period_history
        else:
            self.chat_history = []
    
    
    def recieve(self, message):
        '''Recieves message and adds it into chat_history
        
        Parameters:
            messages (object, Message): message to add in chat_history
        '''
        
        
        self.chat_history.insert(0, message)
        
        
    def show_last_message(self):
        '''Shows the last message and its information from chat
        
        Returns: None
        '''
    
        
        last_message = self.chat_history[0]
        return last_message.show()
    
    
    def show_chat(self):
        '''Shows all messages and their information in chat from the newest to the oldest one
        
        Returns: None
        '''
        
        
        for message in self.chat_history:
            message.show()
            print("--------------------")
            
            
    def str_to_date(self, strdate):
        '''Transforms date from string format to datetime format using datetime module
        Example: '2023/02/21' -> datetime.datetime(2023, 2, 21, 0, 0)
        Note: this fuction is for module script, but you may use it in your purpose
        
        Parameters:
            strdate (str): date in string format (i.e., datetime.datetime(2023, 2, 21, 0, 0))
            
        Returns: date in datetime format
        '''
        
        
        return datetime.strptime(strdate, "%Y/%m/%d")
    
    
    def get_history_from_time_period(self, date_from='0001/01/01', 
                                     date_to='9999/12/31'):
        '''Shows all messages and their information for defined time period
        
        Parameters:
            date_from (str, optional): date to search from, use this format: YYYY/MM/DD
            date_to (str, optional): date to search to, use this format: YYYY/MM/DD
        Note: default values for date_from and date_to were set according 
        to min and max dates in datetime module 
            
        Returns: new_chat (Chat) - with messages and their information for given time period
        '''
        
        
        date_from = self.str_to_date(date_from)
        date_to = self.str_to_date(date_to)
        
        period_history = []
        for message in self.chat_history:
            if date_from <= message.datetime <= date_to:
                period_history.append(message)
        new_chat = Chat(period_history)
        new_chat.show_chat()
        return new_chat
    
    
class Message:
    '''A class for creation of text message by user and sending it to chat
    
    Attributes:
        user (dict): dictionary with all information for user created message
        text (str): text of the message
        
    Methods:
        user_info(): to create user's info in printable view
        show(): to print all message's information
        send(): to send message to chat
    '''
    
    
    def __init__(self, text, user):
        '''Constructs all the necessary attributes for the Message object

        Parameters:
            user (dict): dictionary with all information for user created message
            text (str): text of the message
            datetime (datetime.datetime): date and time when message were sended to chat
                                          (creats ONLY for messages that were sended to chat)
        '''
        
        
        self.user = user.__dict__
        self.text = text
        self.datetime = None
                
            
    def user_info(self):
        '''Creates user's info in printable view
        
        Returns:
            info (str): all user's information as string
        '''
        
        
        info = []
        for key, value in self.user.items():
            info.append(f'{key}: {value}  ')
        return info
    
    
    def show(self):
        '''Shows text of the message and all information about user created it
        
        Returns: None
        '''
        
        
        for key, value in self.__dict__.items():
            if key == "user":
                print(f'user ... ', *self.user_info())
            # elif key == "datetime":
            elif key == "datetime" and value:
                print(f'datetime ... {datetime.strftime(value, "%Y/%m/%d %I:%M%p")}')
            else:
                print(f'{key} ... {value}')
    

    def send(self, chat):
        '''Sends message to chat and puts sending date and time in new attribute "datetime"
        
        Parameters:
            chat (object, Chat): Chat object to send in message
            
        Returns: None
        '''
        
        
        # date_time = datetime.now()
        # setattr(self, "datetime", date_time)
        self.datetime = datetime.now()
        chat.recieve(self)
        
        
class User():
    '''A class to represent a user
    
    Attributes:
        name (str): first name of the user
        surname (str): family name of the user
        nickname (str): nickname of the user
        email (str): email of the user
    '''
    
    
    def __init__(self, user_dict):
        '''Constructs all the necessary attributes for the User object

        Parameters:
            user_dict (dict): dictionary with all user's information
        '''
        
        
        for key, value in user_dict.items():
            setattr(self, key, value)
            

## Example 1. Basic usage

# the first user
user_dict1 = {"name": "Nick", 
             "surname": "Goward", 
             "nickname": "@ngow", 
             "email": "nick_goward@gmail.com"}
user1 = User(user_dict1)
mes1 =  Message("Hello!", user1)

#the second user
user_dict2 = {"name": "Gorge",
             "surname": "Green",
             "nickname": "@ggreen",
             "email": "g_green@gmail.com"}
user2 = User(user_dict2)
mes2 = Message("My name is Gorge!", user2)

# Chat initiation
chat1 = Chat()

# calling attributes for user1 and user2
user1.name, user2.email

# user1's message information
mes1.show()

# sending mes1 and mes2 to chat1
mes1.send(chat1)
mes2.send(chat1)

# after sending mes1 to chat it gained datetime
mes1.show()

# retrieving messages from chat history
chat1.show_chat()

# obtaining last message in chat
chat1.show_last_message()

## Example2. Obtaining messages for time period

messages_list = []
dates = ["2023/02/21 03:15PM", "2023/02/16 03:15PM",
         "2023/02/09 02:45PM", "2023/01/02 05:25PM"]
for i in range(len(dates)):
    mes = Message("Hello!", user1)
    # creating attribute datetime for this Example
    mes.datetime = datetime.strptime(dates[i], "%Y/%m/%d %I:%M%p")
    messages_list.append(mes)

chat14 = Chat(messages_list)
mes_from_period = chat14.get_history_from_time_period('2023/02/09', '2023/02/17')
# type for chat with messages from defined time period
type(mes_from_period)


# Task2.

class Args:
    '''A class for calling functions in custom way
    Example: sum << Args([1, 2])
    
    Parameters:
        args
        kwargs      
    '''
    
    
    def __init__(self, *args, **kwargs):
        '''Constructs all the necessary attributes for the Args object

        Parameters:
            args (list)
            kwargs (dict)
        '''
        
        
        self.args = args
        self.kwargs = kwargs
    
    
    def __rlshift__(self, function):
        '''Adds the left-shift functionality to a class and
        implements the reverse bitwise left-shift operation with reflected, swapped operands
        
        Parameters:
            function (object): function to use on args and kwargs
        '''
        
        
        return function(*self.args, **self.kwargs)
    

# Task3.

class StrangeFloat(float):
    '''A class for extending float functionality'''
    
    
    def __getattr__(self, attr):
        '''Deals with unnown attributes
        
        Parameters:
            attr (str): operation and number written via _
            
        Returns: operation result in StrangeFloat() format
        '''
        
        
        operation, number = attr.split('_')
        operations = ['add', 'subtract', 'multiply', 'divide']
        
        if operation not in operations:
            raise Exception("Unacceptaaaaaaaaaable operation for StrangeFloat, \
                            try add, substract, multiply, or divide")
                
        if operation == 'add':
            return type(self)(self + float(number))
        elif operation == 'subtract':
            return type(self)(self - float(number))
        elif operation == 'multiply':
            return type(self)(self * float(number))
        elif operation == 'divide':
            return type(self)(self / float(number))
        

# Task4.

# my solution for this Task
import numpy as np


matrix = list.__call__()
for idx in range.__call__(0, 100, 10):
    # __iadd__ created 1D list and I did not find the way to transform it in right shape (10, 10)
    matrix.__getattribute__("append")(list.__call__(range.__call__(idx, idx.__add__(10))))
    
selected_columns_indices = list.__call__(filter.__call__(
    lambda x: x in range.__call__(1, 5, 2), range.__call__(matrix.__len__())))
selected_columns = map.__call__(
    lambda x: list.__call__(x.__getitem__(col) for col in selected_columns_indices), matrix)

arr = np.array.__call__(list.__call__(selected_columns))

# here I decided to use __getattribute__ for T
# my method for matrix transposition results in two tuples (for rows), which have not got
# neither __mod__ nor __sub__ magic methods (my matrix transposition is chown below)
mask = arr.__getattribute__("T").__getitem__(1).__mod__(3).__eq__(0)
new_arr = arr.__getitem__(mask)

# yes, here I used my matrix transposition
product = new_arr.__matmul__(list.__call__(zip.__call__(*new_arr)))

if product.__getitem__(0).__lt__(1000).__contains__(False).__eq__(False).__and__(
    product.__getitem__(2).__gt__(1000).__contains__(True)):
    print(sum.__call__(sum.__call__(product)).__truediv__(
        product.__len__().__mul__(product.__getitem__(0).__len__())))
    

# Task5.

from abc import ABC, abstractmethod


class BiologicalSequence(ABC):
    '''An abstract class for biological sequences
    
    Abstract methods:
        __init__(): class constructor
        __getitem__(): gets item by slice or index
        __len__(): returns sequence length
        __str__(): makes readable sequence version
        __repr__(): for class representation
        check_alphabet(): checks if sequence correspondes to class alphabet
    '''
    
    @abstractmethod
    def __init__(self, seq):
        pass
     
        
    @abstractmethod
    def __getitem__(self, els):
        pass
    
    
    @abstractmethod
    def __len__(self):
        pass
    
    
    @abstractmethod
    def __str__(self):
        pass
    
    
    @abstractmethod
    def __repr__(self):
        pass
    
    
    @abstractmethod
    def check_alphabet(self):
        pass
    
    
class AminoNucSequence(BiologicalSequence):
    '''A class for implementation of BiologicalSequence interface'''
    
    def __init__(self, seq):
        if isinstance(seq, str):
            self.seq = seq.upper()
        else:
            raise NotImplementedError('NotImplemented')
        
     
    def __getitem__(self, els):
        return self.seq[els]
    
    
    def __len__(self):
        return len(self.seq)
    
    
    def __str__(self):
        return self.seq
    
    
    def __repr__(self):
        return f'{type(self).__name__}:\n{self.seq}'
    
    
    def check_alphabet(self):
        for letter in self.seq:
            if letter not in self.alphabet:
                return False
        return True
    

class NucleicAcidSequence(AminoNucSequence):
    '''A class for nucleic acid sequences
    
    Methods:
        complement(): makes coplement for nucleic acid
        gc_content(): counts GC-content of nucleic acid
    '''
    
    
    def complement(self):
        '''To complement nucleic acid sequence
        
        Returns: str, complemented nucleic acid sequence    
        '''
        
        
        assert self.check_alphabet(), 'Wrong alphabet'
        if hasattr(self, 'alphabet'):
             return self.seq.translate(str.maketrans(self.alphabet))
        else:
            raise NotImplementedError('NotImplemented')
    
    
    def gc_content(self):
        '''To calculate GC-content of nucleic acid sequence
        
        Returns: float, GC-share in nucleic acid sequence
        '''
        
        
        assert self.check_alphabet(), 'Wrong alphabet'
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq)

    
class DNASequence(NucleicAcidSequence):
    '''A class for DNA sequences
    
    Attributes:
        alphabet (dict): contains complement DNA nucleotides pairs
        
    Methods:
        transcribe(): transcribes nucleic acid sequence
    '''
    
    
    alphabet = {'A': 'T', 'T': 'A',
                'G': 'C', 'C': 'G'}
    
    def transcribe(self):
        '''To transcribe nucleic acid sequence
        
        Returns: str, transcribed nucleic acid sequence
        '''
        
        
        assert self.check_alphabet(), 'Wrong alphabet'
        return self.seq.replace('T', 'U')


class RNASequence(NucleicAcidSequence):
    '''A class for RNA sequences
    
    Attributes:
        alphabet (dict): contains complement RNA nucleotides pairs
    '''
    
    
    alphabet = {'A': 'U', 'U': 'A',
                'G': 'C', 'C': 'G'}

    
class AminoAcidSequence(AminoNucSequence):
    '''A class for amino acid sequences
    
    Attributes:
        alphabet (frozen): contains all amino acids
        
    Methods:
        extinction_coef(): calculates extinction coefficient for amino acid sequence
    '''

    
    alphabet = frozenset('GPAVLIMCFYWHKRQNEDST')
    
    
    def extinction_coef(self):
        '''Calculates extinction coefficient, 
        asuming all Cys (C) is in disulfide bonds
        
        Returns: int, calculated extinction coefficient
        '''
        
        
        assert self.check_alphabet, 'Wrong alphabet'
        n_W = self.seq.count('W')
        n_Y = self.seq.count('Y')
        n_C = self.seq.count('C')
        return n_W * 5500 + n_Y * 1490 + n_C * 125
    

if __name__ == '__main__':
    seq1 = DNASequence('ACGTACGTACGT')
    seq2 = RNASequence('ACGUACGUACGU')
    seq3 = AminoAcidSequence('GPAVLIMCFYWHKRQNEDST')
    seq4  = AminoAcidSequence('ZZZGPAVLIMCFYWZZZZHKRQNEDSTZZZ')
    print(seq1)
    print(seq1[:5], seq1[0])
    print(seq1.complement())
    print(seq1.transcribe())
    print(seq2.complement())
    print(seq3[1:])
    print(seq3.extinction_coef())
    print(seq3.check_alphabet(), seq4.check_alphabet())