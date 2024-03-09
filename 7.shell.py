import subprocess 

def execute_command (comman ) :
    process = subprocess.Popen( comman , stdout=subprocess.PIPE , stderr=subprocess.PIPE, shell=True)
    output , error = process.communicate()
    
    if process.returncode != 0 :
        print(f"erro : {error.decode()}")
    else : 
        print(output.decode())
        
def shell () :
    while True :
        a = input("shell : >>>")
        if a == "exit" :
            break
        execute_command(a)

if __name__ == "__main__":
    shell()