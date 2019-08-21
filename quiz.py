from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdTqmtxyi8ENaBnteg5cO9Q0WJmkiFetgQZniKt6zBoT3KOQin7HxjkUz8zwVRwsl_TgjDfX0x9CQM_DQRYhHbIeqVOQV1LElrGTHtOeAGmSZ-SABp10iJW6oPXQCDWau4kTMlq32QnKcyYwUTVn3HzJ-Aq6EREj894GW6kvXS405w7OI='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
    