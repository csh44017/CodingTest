morse = { 
'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
'--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
'--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
'...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
'-.--':'y','--..':'z'
}

def solution(letter):
    result = ""
    string_list = letter.split()
    for s in string_list:
        result = result + morse[s]
    return result
