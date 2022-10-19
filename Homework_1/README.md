# **Collections** :whale:
## Home work 1
Utility **hw1_collections.py** provides some basic tools for working with *nucleic acid sequences*. Based on python dictionaries and the complementarity principle, 
this script allows to make complement sequences for DNA and RNA, to reverse them, and to transcribe RNA sequence from DNA template. 
For your convenience **hw1_collections.py** is not case-sensitive, and all charachters in output sequences in accordance with input register.
Here some **guidelines** for *how to use it* and *how does it work*.

### **How to use it**
The **hw1_collections.py** recieves two variables from std.input() - *command* and *nucleic_acid*.
- **command**: string variable, paste your command in std.input(), programm proceeds to specified *functions* (see below) resulted in *std.out()*
- **nucleic_acid**: string variable, this sequence undergoes some checking-outs, if it is recognised as DNA or RNA type, the show begins

### **How does it work**
The **hw1_collections.py** supports the list of *commands*:
- **transcribe** — to initiate function for DNA transcription, in std.out() RNA sequence from DNA template
- **reverse* — to initiate function that reverses either DNA or RNA, in std.out() reversed DNA or RNA sequence
- **complement** — to launch function for either DNA or RNA complementation, in std.out() complemented DNA or RNA sequence  
- **reverse_complement** — to launch function for reversion and complementation of either DNA or RNA complementation, in std.out() RNA sequence from DNA template
- **exit** — for utilite shutdown
<br> *__Notice__*: The empty std.input() for *command* results in utilite shutdown. 

Hope you enjoy this utility!
