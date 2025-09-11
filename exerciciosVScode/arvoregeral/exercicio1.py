
class Tree:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation 

        self.children = []
        self.parent = None 

    def add_children(self, child):
        child.parent = self
        self.children.append(child)     

    def get_level(self): 
        level = 0 
        p = self.parent 
        while p:
            level += 1
            p = p.parent 
        return level
    
    def print_tree(self, type):
        
        if type == "both":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(f"{prefix}{self.name} ({self.designation})")
            if self.children:
                for child in self.children:
                    child.print_tree(type)
        
        elif type == "name":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(f"{prefix}{self.name}")
            if self.children:
                for child in self.children:
                    child.print_tree(type) 

        elif type == "designation":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(f"{prefix}{self.designation}")
            if self.children:
                for child in self.children:
                    child.print_tree(type)

        else:
            print("Choose a option between: both, name, designation")

        
        

def build_tree():

    #pai
    root = Tree("Nilupul", "CEO")
    #filhos
    Chinmay = Tree("Chinmay", "CTO")
    Gels = Tree("Gels", "HR Head")
    root.add_children(Chinmay)
    root.add_children(Gels)
    #netos
    Vishwa = Tree("Vishwa", "Infrastructure Head")
    Aamir = Tree("Aamir", "Application Head")
    Chinmay.add_children(Vishwa)
    Chinmay.add_children(Aamir)

    Peter = Tree("Peter", "Recruitment Manager")
    Waqas = Tree("Waqas", "Policy Manager")
    Gels.add_children(Peter)
    Gels.add_children(Waqas)

    #bisneto 

    Dhaval = Tree("Dhaval", "Cload Manager")
    Abhijit = Tree("Abhijit", "App Manager")

    Vishwa.add_children(Dhaval)
    Vishwa.add_children(Abhijit)

    return root


if __name__ == '__main__':
    root = build_tree()
    print("\nNames:\n")
    root.print_tree("name")
    print("\nDesignation:\n")
    root.print_tree("designation")
    print("\nBoth:\n")
    root.print_tree("both")
