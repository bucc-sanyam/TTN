from abc import ABC, abstractmethod


class Box():

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def count(self):
        pass

    def repack_boxes(self, n):
        self.n = n


class item():

    def __init__(self, name, value):
        self.name = name
        self.value = value


class listBox(Box):
    listVal = []
    flag = 0

    def __init__(self):
        pass

    def add(self, *items):
        super().add()
        # self.flag=self.flag+1
        for item in items:
            self.listVal.append(item)
        # print(self.flag)

    def empty(self):
        super().empty()
        print("All items that were added in the box : " + str(
            [self.listVal[i].name for i in range(0, len(self.listVal))]))
        self.listVal = []
        print("Final Value of the list : " + str(self.listVal))

    def count(self):
        super().count()
        print("Number of elements in the list is {}.".format(len(self.listVal)))




class DictBox(Box):
    def __init__(self):
        dicts = {}
        self.dicts = dicts

    def add(self, *args):
        for item in args:
            self.dicts.update({item.name: item.value})

    def empty(self):
        l = []
        for key, val in self.dicts.items():
            listitem = item(key, val)
            l.append(listitem)
        self.dicts.clear()  # clears the dict
        return l

    def count(self):
            return len(self.dicts.items())


a=item('A',10)
b=item('B',20)
c=item('C',30)
d=item('D',40)
e=item('E',50)
f=item('F',60)
g=item('G',70)
h=item('H',80)

aa=item('AA',270)
bb=item('BB',280)
cc=item('CC',290)
dd=item('DD',300)
ee=item('EE',310)
ff=item('FF',320)
gg=item('GG',330)
hh=item('HH',340)


lists=listBox()
lists.add(a,b,c,d,e,f)
x=lists.empty()
for values in x:
    print(values.name+":"+str(values.value))


dicts=DictBox()
dicts.add(e,f,g,h)
x=dicts.empty()
for values in x:
    print(values.name+":"+str(values.value))