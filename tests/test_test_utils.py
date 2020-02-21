import shutil

from pathlib import Path

from nose.tools import ok_, eq_

from rsmtool.test_utils import copy_data_files


class TestCopyData():

    def setUp(self):
        self.dirs_to_remove = []

    def tearDown(self):
        for temp_dir in self.dirs_to_remove:
            shutil.rmtree(temp_dir)

    def test_copy_data_files(self):
        file_dict = {'train': 'data/files/train.csv',
                     'features': 'data/experiments/lr/features.csv'}
        expected_dict = {'train': 'temp_test_copy_data_file/train.csv',
                         'features': 'temp_test_copy_data_file/features.csv'}
        self.dirs_to_remove.append('temp_test_copy_data_file')
        output_dict = copy_data_files('temp_test_copy_data_file',
                                      file_dict)
        for file_type in expected_dict:
            eq_(output_dict[file_type], expected_dict[file_type])
            ok_(Path(output_dict[file_type]).exists())
            ok_(Path(output_dict[file_type]).is_file())


    def test_copy_data_files_directory(self):
        file_dict = {'exp_dir': 'data/experiments/lr-self-compare/lr-subgroups'}
        expected_dict = {'exp_dir': 'temp_test_copy_dirs/lr-subgroups'}
        self.dirs_to_remove.append('temp_test_copy_dirs')
        output_dict = copy_data_files('temp_test_copy_dirs',
                                      file_dict)
        for file_type in expected_dict:
            eq_(output_dict[file_type], expected_dict[file_type])
            ok_(Path(output_dict[file_type]).exists())
            ok_(Path(output_dict[file_type]).is_dir())


    def test_copy_data_files_files_and_directories(self):
        file_dict = {'exp_dir': 'data/experiments/lr-self-compare/lr-subgroups',
                     'test': 'data/files/test.csv'}
        expected_dict = {'exp_dir': 'temp_test_copy_mixed/lr-subgroups',
                         'test': 'temp_test_copy_mixed/test.csv'}
        self.dirs_to_remove.append('temp_test_copy_mixed')
        output_dict = copy_data_files('temp_test_copy_mixed',
                                      file_dict)
        for file_type in expected_dict:
            eq_(output_dict[file_type], expected_dict[file_type])
            ok_(Path(output_dict[file_type]).exists())
        ok_(Path(output_dict['exp_dir']).is_dir())
        ok_(Path(output_dict['test']).is_file())