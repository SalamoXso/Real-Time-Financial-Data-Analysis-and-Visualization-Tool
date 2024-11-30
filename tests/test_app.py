import pytest
from dash import Dash
from dashboard.app import app

def test_app_creation():
    # Ensure the Dash app can be created without issues
    assert isinstance(app, Dash)

def test_layout():
    # Ensure that the layout is set up properly
    layout = app.layout
    assert layout is not None
    assert any(child.id == 'live-graph' for child in layout.children)
