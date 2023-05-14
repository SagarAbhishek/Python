for i in range(2,21):
    with open(f"Crash Course\\file input output\\tables\\multiplication_table_of{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
    
    
