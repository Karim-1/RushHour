class Board:
    def __init__(self, size, cars):
        #self.board = self.load_board(size)
        self.size=size
        self.cars=cars

    def load_board(self):
        """
        Loads default empty board.
        """
        # VOOR 10-1: willen we list in list maken? Zodat we erover heen kunnen loopen?
        # Maakt een bord van n*n
        #Matrix = [[0 for x in range(size)] for y in range(size)]
        notbegin_car=[]
        print(self.cars)
        for x in range(self.size):
            for y in range(self.size):
                #print("x", end='')
                #print(x+1, end='')
                #print("y", end='')
                #print(y+1)

                for car in self.cars:

                    #print("cars", end='')
                    #print("-",car[2],"-", car[3])
                    if int(car[2]) == (y+1) and int(car[3]) == (x+1):
                        #print(x+1)
                        #print(y+2)
                        #print(car)
                        if car[1]=='H':
                            # if coordinate is good, print coordinates
                            # else, print empty
                            print(car[0],end='')
                            for i in range(int(car[4])):
                                list=[]
                                list.append(car[0])
                                list.append(int(car[2])+(i))
                                list.append(int(car[3]))
                                print(list)
                                notbegin_car.append(list)

                            #x=x+int(car[4])
                            #for i in range(int(car[4])):
                            #    print(car[0],end='')

                        if car[1]=='V':
                            print(car[0],end='')
                            for i in range(int(car[4])):
                                list=[]
                                list.append(car[0])
                                list.append(int(car[2]))
                                list.append(int(car[3])+(i))
                                print(list)
                                notbegin_car.append(list)


                else:
                    print('O',end='')
                        #print(car[0], end='')


                #    else:
                        #print('#',end='')
            print("\n")

                    #print(" HIER")
                    #print("# ", end='')


    def __repr__(self):
        return self.board
