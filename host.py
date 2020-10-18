import socket

def get_ip():
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    result={"hostname":hostname,"ip":ip}
    return result


if __name__=="__main__":
    result=get_ip()
    print(result)