import unittest


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []  # Lista dzieci węzła
        self.edges = {}  # Przechowuje wartości krawędzi

    def add_child(self, child, edge_value=None):
        """Dodaje dziecko do węzła."""
        self.children.append(child)
        self.edges[child] = edge_value

    def __str__(self, level=0):
        """Rekurencyjne formatowanie drzewa."""
        edge_values = [f"{self.edges[child]}" for child in self.children]
        result = " " * level + f"Node({self.value}) -> Edges: {edge_values}\n"
        for child in self.children:
            result += child.__str__(level + 4)
        return result


class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value)

    def traverse(self):
        """Przechodzi przez wszystkie węzły drzewa i zwraca ich wartości."""
        values = []

        def dfs(node):
            if node:
                values.append(node.value)
                for child in node.children:
                    dfs(child)

        dfs(self.root)
        return values

    def __str__(self):
        """Zwraca wizualną reprezentację drzewa."""
        return str(self.root)


class TestTree(unittest.TestCase):
    def test_tree_creation(self):
        tree = Tree("Root")
        self.assertEqual(tree.root.value, "Root")
        self.assertEqual(tree.traverse(), ["Root"])

    def test_add_child(self):
        tree = Tree("Root")
        node_a = TreeNode("A")
        tree.root.add_child(node_a, "edge_to_A")
        self.assertEqual(len(tree.root.children), 1)
        self.assertEqual(tree.root.edges[node_a], "edge_to_A")

    def test_traverse(self):
        tree = Tree("Root")
        node_a = TreeNode("A")
        node_b = TreeNode("B")
        node_c = TreeNode("C")

        tree.root.add_child(node_a, "edge_to_A")
        tree.root.add_child(node_b, "edge_to_B")
        node_a.add_child(node_c, "edge_to_C")

        self.assertEqual(tree.traverse(), ["Root", "A", "C", "B"])

    def test_str_representation(self):
        tree = Tree("Root")
        node_a = TreeNode("A")
        tree.root.add_child(node_a, "edge_to_A")
        self.assertIn("Node(Root)", str(tree))
        self.assertIn("edge_to_A", str(tree))
        self.assertIn("Node(A)", str(tree))


if __name__ == "__main__":
    unittest.main()