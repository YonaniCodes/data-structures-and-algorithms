# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    first= float('inf')
    second= float('inf')
    
    for record in records:
        #if the num is lessthan the first num
        if record[1]< first: # , inf
            second= first
            first= record[1]
        #if the number is between first and second
        elif record[1]<second and first< record[1]:
            second= record[1]
    output=[]
    for record in records:
        if record[1]== second:
            output.append(record[0])
            # print(record[0])
    output.sort()
    for name in output:
        print(name)
    # print(second,first)
    
    
    #5 inf
    #5 37<inf  and
    

        
        
        
        