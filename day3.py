# 1) For-loop: print 1→5
for i in range(1, 6):
    print(i)

# 2) While-loop: count down 5→1
count = 5
while count > 0:
    print(count)
    count -= 1

# 3) Chat stub: ask until they type “exit”
while True:
    ans = input("Good to go? (or 'exit') ")
    if ans.lower() == "exit":
        print("Bye!")
        break
    print("You said:", ans)
