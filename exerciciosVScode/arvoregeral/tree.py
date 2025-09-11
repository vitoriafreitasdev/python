
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self 
        self.children.append(child)  

    def get_level(self):
        level = 0
        p = self.parent 
        while p:
            level += 1
            p = p.parent
        return level 

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    #pai
    root = TreeNode("Electronics")
    #filho
    laptop = TreeNode("Laptop")
    #netos
    mac = TreeNode("Mac")
    surface = TreeNode("Surface")
    thinkpad = TreeNode("Thinkpad")

    laptop.add_child(mac)
    laptop.add_child(surface)
    laptop.add_child(thinkpad)
    #filho
    cellphone = TreeNode("Cell Phone")
    #netos
    iphone = TreeNode("iPhone")
    google_pixel = TreeNode("Google Pixel")
    vivo = TreeNode("Vivo")

    cellphone.add_child(iphone)
    cellphone.add_child(google_pixel)
    cellphone.add_child(vivo)
    #filho
    tv = TreeNode("TV")
    #netos
    sansung = TreeNode("Samsung")
    lg = TreeNode("LG")

    tv.add_child(sansung)
    tv.add_child(lg)

    #bisneto

    mac.add_child(TreeNode("Mac1"))
    mac.add_child(TreeNode("Mac2"))
    surface.add_child(TreeNode("surface1"))
    surface.add_child(TreeNode("surface2"))
    thinkpad.add_child(TreeNode("thinkpad1"))
    thinkpad.add_child(TreeNode("thinkpad2"))

    iphone.add_child(TreeNode("iphone1"))
    iphone.add_child(TreeNode("iphone2"))
    google_pixel.add_child(TreeNode("google_pixel1"))
    google_pixel.add_child(TreeNode("google_pixel2"))
    vivo.add_child(TreeNode("vivo1"))
    vivo.add_child(TreeNode("vivo2"))

    sansung.add_child(TreeNode("sansung1"))
    sansung.add_child(TreeNode("sansung2"))
    lg.add_child(TreeNode("lg1"))
    lg.add_child(TreeNode("lg2"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)


    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()