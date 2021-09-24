
def decode(data: bytes):
    data = data.decode("UTF-8")
    return data

if __name__ == '__main__':
    print("enter byte code")
    data = input()
    response = decode(data)
    print(response)