@classmethod
def setUpClass(self):
        fake_file_content = """200.0	60.0	-140.0	60.0
8	5	20
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
4	1    4    8    5"""
        fake_file_path = 'data/poly_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.poly_box = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)


 # polyedr perimetr

def test_box_perimetr(self):
    self.assertEqual(self.poly_box.good_perimetr, 12)
