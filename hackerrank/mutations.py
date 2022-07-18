def mutate_string(string, pos, char):
  s_new = list(string)
  s_new[pos] = char
  s_new = ''.join(s_new)
  return s_new
    
if __name__ == '__main__':
    s = input("enter the string  ")
    i, c = input("enter position you want to change and char ").split()
    s_new = mutate_string(s, int(i), c)
    print("changed string is ", s_new)