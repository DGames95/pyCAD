class ConstraintGraph:
    def __init__(self):
        self.constraints = []  # List to store all constraints
        self.constraint_dependencies = {}  # Dictionary to track constraint dependencies

    def add_constraint(self, constraint):
        # Add a constraint to the graph
        self.constraints.append(constraint)

    def add_dependency(self, dependent_constraint, depends_on_constraint):
        # Specify that dependent_constraint depends on depends_on_constraint
        if dependent_constraint not in self.constraint_dependencies:
            self.constraint_dependencies[dependent_constraint] = []
        self.constraint_dependencies[dependent_constraint].append(depends_on_constraint)

    def resolve_constraints(self):
        # Iterate through constraints and resolve them, considering dependencies
        resolved_constraints = set()  # Track resolved constraints to avoid duplicate processing
        while len(resolved_constraints) < len(self.constraints):
            for constraint in self.constraints:
                if constraint in resolved_constraints:
                    continue
                dependencies = self.constraint_dependencies.get(constraint, [])
                if all(dep in resolved_constraints for dep in dependencies):
                    # All dependencies are resolved; resolve this constraint
                    constraint.resolve()
                    resolved_constraints.add(constraint)
