# ----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    # def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    def BinarySearch(self, item, l_border, r_border):
        if r_border <= l_border:
            return l_border + 1 if item.Cast() > self.store[l_border].Cast() else l_border
        mid = int((l_border + r_border) / 2)
        if item.Cast() == self.store[mid].Cast():
            return mid + 1
        if item.Cast() > self.store[mid].Cast():
            return self.BinarySearch(item, mid + 1, r_border)
        return self.BinarySearch(item, l_border, mid - 1)

    def BinaryInsertion(self):
        loc, counter = 0, 0
        for j in range(len(self.store) - 1):
            counter = j
            selected = self.store[counter + 1]
            loc = self.BinarySearch(selected, 0, counter)
            while counter >= loc:
                self.store[counter + 1] = self.store[counter]
                counter -= 1
            self.store[counter + 1] = selected
