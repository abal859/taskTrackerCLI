#!/usr/bin/env python3

import task_functions as tf
import argparse

def interactive_mode():
    while True:
        cmd = input("task-cli> ").strip().split()
        if not cmd:
            continue
        if cmd[0] in ["exit", "quit"]:
            break
        try:
            main(cmd)
        except SystemExit:
            pass

def main(cmd_args=None):
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("description", type=str, help="Description of a task")

    del_parser = subparsers.add_parser("delete", help="Delete a task")
    del_parser.add_argument("id_task", type=int, help="ID of the task to remove")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id_task", type=int, help="ID of the task to update")
    update_parser.add_argument("new_description", type=str, help="New description for task")

    mark_ip_parser = subparsers.add_parser("mark-in-progress", help="Mark task in progress")
    mark_ip_parser.add_argument("id_task", type=int, help="ID of the task to mark in progress")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark task done")
    mark_done_parser.add_argument("id_task", type=int, help="ID of the task to mark done")

    subparsers.add_parser("list", help="List all tasks")
    subparsers.add_parser("list-done", help="List done tasks")
    subparsers.add_parser("list-in-progress", help="List in progress tasks")
    subparsers.add_parser("list-todo", help="List todo tasks")

    args = parser.parse_args(cmd_args)

    if args.command is None:
        parser.print_help()
        return

    match(args.command):
        case "add": tf.add_task(args.description)
        case "delete": tf.del_task(args.id_task)
        case "update": tf.update_task(args.id_task, args.new_description)
        case "mark-in-progress": tf.mark_in_progress(args.id_task)
        case "mark-done": tf.mark_done(args.id_task)
        case "list": tf.list_all_tasks()
        case "list-done": tf.list_done()
        case "list-in-progress": tf.list_in_progress()
        case "list-todo": tf.list_todo()
        case _ : parser.print_help()

if __name__ == "__main__":
    interactive_mode()
