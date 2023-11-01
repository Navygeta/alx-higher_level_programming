#!/usr/bin/python3
"""
Module: Function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices

    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        Result of multiplication
    """

    return (np.matmul(m_a, m_b))
