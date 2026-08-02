from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None


def test_graph_exists(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-filter")
    assert picker is not None