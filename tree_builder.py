class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # If no current_node was passed, start searching from the root
        if current_node is None:
            current_node = self.root

        # Safety check: tree is empty
        if current_node is None:
            print("⚠️ Cannot insert - the tree has no team lead yet.")
            return

        # Found the manager
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print(f"❌ LEFT side of {manager_name} is already occupied.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print(f"❌ RIGHT side of {manager_name} is already occupied.")
            else:
                print("❌ Side must be 'left' or 'right'.")
            return

        # Manager not found yet → search both sides recursively
        found = False

        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
            found = True

        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)
            found = True

        # If we reached a leaf and never found the manager
        if not found and current_node.left is None and current_node.right is None:
            print(f"❌ Manager '{manager_name}' not found in the team.")

    def print_tree(self, node=None, level=0):
        # If no node is passed and we're at the top level, start from the root
        if node is None:
            if level == 0:
                node = self.root
            else:
                return  # We've reached past a leaf

        # Safety check in case the tree is empty
        if node is None:
            print("The team is currently empty.")
            return

        # Print the current employee with indentation based on level
        print("  " * level + "- " + node.name)

        # Recursively print left and right subordinates
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


company_directory()


# Recursive insertion works by starting at the root and walking down the tree until it finds the manager we’re looking for. At each node, the method checks whether the current employee matches the target manager name. If it does, it tries to place the new employee on the requested side (left or right). If that side is already taken, it prints an error. If the current node is not the manager, the method calls itself on the left child and then the right child, continuing the search deeper into the tree. This continues until either the manager is found or the method reaches a leaf with no children.
# The main challenge was making sure the search didn’t stop too early or miss a manager deeper in the tree. Because every node can have up to two children, I had to carefully decide when to recurse and when to stop. Another tricky part was handling the case where the manager simply doesn’t exist — the method needs to report that cleanly instead of crashing or silently failing. Getting the base cases right (empty tree, missing manager, occupied side) took a few attempts.
# Trees are especially useful in real-world systems that have a natural hierarchy. Company org charts, file systems, and decision trees are good examples. Unlike a flat list or dictionary, a tree makes the parent-child relationships explicit and easy to traverse. Searching or printing an entire reporting structure becomes straightforward with recursion, and adding new nodes in the correct place is more intuitive than trying to maintain the same relationships in a linear structure.