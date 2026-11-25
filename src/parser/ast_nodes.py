"""
ast_nodes.py — Abstract Syntax Tree (AST) node definitions for Cobra.

All nodes are plain Python dataclasses so they are easy to inspect,
pretty-print, and traverse.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Optional


# ── Base ──────────────────────────────────────────────────────────────────────

@dataclass
class ASTNode:
    """Base class for every AST node."""
    line:   int = field(default=0, compare=False, repr=False)
    column: int = field(default=0, compare=False, repr=False)


# ── Top-level ─────────────────────────────────────────────────────────────────

@dataclass
class Program(ASTNode):
    """The root node of a Cobra program — a list of top-level statements."""
    body: List[ASTNode] = field(default_factory=list)


# ── Statements ────────────────────────────────────────────────────────────────

@dataclass
class FunctionDef(ASTNode):
    """
    fn name(params) -> return_type:
        body
    """
    name:        str
    params:      List[str]      = field(default_factory=list)
    return_type: Optional[str]  = None
    body:        List[ASTNode]  = field(default_factory=list)


@dataclass
class IfStmt(ASTNode):
    """
    if condition:
        then_body
    else:
        else_body
    """
    condition: ASTNode
    then_body: List[ASTNode]            = field(default_factory=list)
    else_body: Optional[List[ASTNode]]  = None


@dataclass
class WhileStmt(ASTNode):
    """
    while condition:
        body
    """
    condition: ASTNode
    body:      List[ASTNode] = field(default_factory=list)


@dataclass
class ReturnStmt(ASTNode):
    """return value"""
    value: Optional[ASTNode] = None


@dataclass
class AssignStmt(ASTNode):
    """name = value"""
    name:  str
    value: ASTNode = field(default=None)  # type: ignore[assignment]


# ── Expressions ───────────────────────────────────────────────────────────────

@dataclass
class BinaryOp(ASTNode):
    """left op right  — e.g. a + b, x == y"""
    op:    str
    left:  ASTNode = field(default=None)  # type: ignore[assignment]
    right: ASTNode = field(default=None)  # type: ignore[assignment]


@dataclass
class UnaryOp(ASTNode):
    """op operand  — e.g. not x, -n"""
    op:      str
    operand: ASTNode = field(default=None)  # type: ignore[assignment]


@dataclass
class Literal(ASTNode):
    """A literal value: integer, float, string, or boolean."""
    value: Any = None


@dataclass
class Identifier(ASTNode):
    """A variable / function name reference."""
    name: str = ""


@dataclass
class CallExpr(ASTNode):
    """callee(args...)"""
    callee: ASTNode              = field(default=None)  # type: ignore[assignment]
    args:   List[ASTNode]        = field(default_factory=list)
