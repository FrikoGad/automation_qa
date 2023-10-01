from pages.interactions_page import SortablePage, SelectablePage, DraggablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'the order of the list has not been changed'
            assert grid_before != grid_after, 'the order of the grid has not been changed'

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0,  'no elements were selected'
            assert len(item_grid) > 0,  'no elements were selected'

    class TestDraggablePage:

        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, 'the position of the box has not been changed'

        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted('x')
            top_y, left_y = draggable_page.axis_restricted('y')
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"

