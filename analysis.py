import sys
from fuzzingbook.ControlFlow import gen_cfg
import ast
import astor


# check the graph of the given function for uninitialized vars
def find_uninitialized(func_cfg, func_start_lineno, func_name):
    found = False
    for node in func_cfg.values():
        if (isinstance(node.ast_node, ast.AnnAssign) and
                node.ast_node.value is None and
                node.ast_node.target.id not in {'enter', 'exit', '_if', '_for', '_while'}):
            if not found:
                print("\nWarning in function", func_name, ":")
                found = True
            print("\tLine", func_start_lineno + node.lineno(), ": variable", node.ast_node.target.id, "uninitialized")


# create AST from source file
tree = astor.parse_file(sys.argv[1])

# visit tree nodes, check functions for uninitialized vars
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        find_uninitialized(gen_cfg(astor.to_source(node)), node.lineno, node.name)
