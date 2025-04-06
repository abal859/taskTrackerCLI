import unittest
from io import StringIO
from unittest.mock import patch
import sys
from main import main
import task_functions as tf
import re

def remove_ansi_codes(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

class TestTaskManagerCLI(unittest.TestCase):

    @patch('task_functions.add_task')
    @patch('sys.argv', new=['task-cli', 'add', 'Test task'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_add_command(self,  mock_add_task):
        main()
        mock_add_task.assert_called_with('Test task')

    @patch('task_functions.del_task')
    @patch('sys.argv', new=['task-cli', 'delete', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_delete_command(self, mock_stdout, mock_del_task):
        main()
        mock_del_task.assert_called_with(1)

    @patch('task_functions.update_task')
    @patch('sys.argv', new=['task-cli', 'update', '1', 'Updated task'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_update_command(self, mock_stdout, mock_update_task):
        main()
        mock_update_task.assert_called_with(1, 'Updated task')

    @patch('task_functions.mark_in_progress')
    @patch('sys.argv', new=['task-cli', 'mark-in-progress', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_mark_in_progress_command(self, mock_stdout, mock_mark_in_progress):
        main()
        mock_mark_in_progress.assert_called_with(1)

    @patch('task_functions.mark_done')
    @patch('sys.argv', new=['task-cli', 'mark-done', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_mark_done_command(self, mock_stdout, mock_mark_done):
        main()
        mock_mark_done.assert_called_with(1)

    @patch('task_functions.list_all_tasks')
    @patch('sys.argv', new=['task-cli', 'list'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_list_command(self, mock_stdout, mock_list_all_tasks):
        main()
        mock_list_all_tasks.assert_called()

    @patch('task_functions.quit')
    @patch('sys.argv', new=['task-cli', 'quit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_quit_command(self, mock_stdout, mock_quit):
        main()
        mock_quit.assert_called()

if __name__ == '__main__':
    unittest.main()

