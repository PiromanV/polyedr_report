@classmethod
def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	6	24
-1	-1	1
-1	1	1
1	1	1
1	-1	1
-1	-1	-1
-1	1	-1
1	1	-1
1	-1	-1
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5
4	8    7    6    5"""
        fake_file_path = 'data/poly_cube.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.poly_cube = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)


    # double edges (with two facets) can be countable

def test_cube_perimetr(self):
    self.assertEqual(self.poly_cube.good_perimetr, 12)
