class BasicExecute:
    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):

        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'DOC':
            if node[1] == 'LPAREN':
                if node[2] == 'STRING':
                    if node[3] == 'RPAREN':
                        if node[4] == None:
                            self.walkTree(node[5])
                        else:
                            self.walkTree(node[2])

        if node[0] == 'expr':
            pass

        if node[0] == 'NUMBER':
            return node[1]

        if node[0] == 'STRING':
            return node[1]

        if node[0] == 'PLUS':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'MINUS':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'TIMES':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'DIVIDE':
            return self.walkTree(node[1]) / self.walkTree(node[2])

        if node[0] == 'ASSIGN':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'VAR':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '" + node[1] + "' found!")
                return 0


