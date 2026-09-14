class Cart:

    def __init__(self):
        self.shop_items = {
            "milk": 3.49,
            "eggs": 2.99,
            "bread": 2.50,
            "apples": 1.99,
            "chicken_breast": 5.99,
            "rice": 1.20,
            "coffee": 7.99,
            "End" : "End the shopping"
        }
        self.current_cart = {}

    def interface(self):

        print("1 : Add items to the cart")

        print("2 : Give total")

        print("3: Cart")

        print("4: Exied the cart")

        print("\n")

        choice = int(input("Choose the option "))

        match choice:
            case 1:
                print("1 : Add items to the cart :")
                print("\n")
                self.add()
            case 2:
                print("2 : Give total : ",end=" ")
                self.total()
            case 3:
                print("3: Cart ")
                print("\n")
                self.cart_items()
            case 4:
                print("4: Exied the cart")

    

    def add(self):
        for i,(key,value) in enumerate(self.shop_items.items()):
            print(i, ":", key, " : ", value )
        print("\n","\t")
        item_ordered = int(input("Add item in the cart : "))

        if item_ordered == len(self.shop_items.items()) -1 :
            return self.interface()

        for i in range(len(self.shop_items.items())):
            if list(self.shop_items.keys())[i] == list(self.shop_items.keys())[item_ordered]:
                self.current_cart.update({list(self.shop_items.keys())[i]:self.shop_items[list(self.shop_items.keys())[i]]})
                return self.add()


    def total(self):
       total = sum(self.current_cart.values())
       print(total)
       print("\n")
       return self.interface()

    def cart_items(self):
        for i in self.current_cart.items():
                print(i)
        print("\n")    
        return self.interface()


s1 = Cart()

s1.interface()