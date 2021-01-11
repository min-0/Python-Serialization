from faker import Faker

class Ipman :
    
    def __init__ (self, name, address, ip):
        self.name = name
        self.address = address
        self.ip = ip

    def show_data(self):
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)

if __name__ == "__main__":
    f = Faker('ko_KR')

    #가상 환경 쓸 경우, 버퍼에 가상환경 주소가 남아 있는 것을 해결하기 위해
    input()

    number = int(input('몇개 생성하실 ? > '))
    Ipmans = []

    for i in range(int(number)):
        Ipmans.append(Ipman(f.name(), f.address(), f.ipv4_private()))

    for j in Ipmans:
        j.show_data()