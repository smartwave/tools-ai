"""Shared code for the governance checks in ci/.

Nothing here reaches the network. Every check imports from this package so
that configuration resolution, provenance gating, and result reporting have
exactly one implementation.
"""
