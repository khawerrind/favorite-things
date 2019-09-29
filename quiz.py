from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdg5M-MUL9w8EuCZlA3PnY7an3o8ZmS3wI2m9ZYqmV7GSBNy'\
    b'_ThD99zpQ6YBswTv7qdMZHVkQpkIvKh5aw8gZNRe6K_Pc8K3dn_DBgXVg19nuSK8EI3C7k3'\
    b'--07jLoB-7JHt_3wEyH1qbLBHFdI3lLW08wvOkN6zi1lCJNk2a6uzfxw8I='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == '__main__':
    main()
