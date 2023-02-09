import redis
import typer
import time
from random import seed
from random import randint



#Typer App CLI Helper
app = typer.Typer()

HOST = '192.168.0.18'

def generate_random():
    return randint(0,100)


#Main Task
@app.command()
def main():
    print("USE CTRL+C TO STOP")
    while(True):
        r = redis.Redis(host=HOST, port=6379, db=0)
        r.set('number',generate_random())
        time.sleep(10)

if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        #print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
