class Tree:
    def __init__(self, data):
        self.data = data
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
    
    def print(self, level):
        
        now_level = self.get_level()

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        
        if self.children:
            for child in self.children:
                if now_level < level:
                    child.print(level)

        
        

            


def create_tree():

    Global = Tree("Global")

    India = Tree("India")
    Usa = Tree("USA")

    Global.add_children(India)
    Global.add_children(Usa)

    Gujarat = Tree("Gurajat")
    Karnataka = Tree("Karnataka")

    India.add_children(Gujarat)
    India.add_children(Karnataka)

    Gujarat.add_children(Tree("Ahmedabad"))
    Gujarat.add_children(Tree("Baroda"))

    Karnataka.add_children(Tree("Bangluru"))
    Karnataka.add_children(Tree("Mysore"))


    NewJersey = Tree("New Jersey")
    California = Tree("California")

    Usa.add_children(NewJersey)
    Usa.add_children(California)

    NewJersey.add_children(Tree("Princeton"))
    NewJersey.add_children(Tree("Trenton"))

    California.add_children(Tree("San Francisco"))
    California.add_children(Tree("Mountain View"))
    California.add_children(Tree("Palo Alto"))

    return Global

if __name__ == "__main__":
    root = create_tree()
    root.print(3)


