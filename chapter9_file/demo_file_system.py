#!/usr/bin/env python
import os
import dbm

# print os.mkdir("asdf")/

# print os.remove("asdf")

# print os.rename()

# for item in os.walk("."):
#     print item,

# os.chdir()

# os.chroot()

print os.listdir(".")

print os.getcwd()

# print os.access(".", 12)

# os.chmod("./demo_built_in.py", 777)

# os.chown()

# os.umask()


print os.path.basename("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.basename(".")

print os.path.dirname("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.join(os.path.dirname("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py"), os.path.basename("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py"))

print os.path.split("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.splitext("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.getatime("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.getctime("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.getmtime("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.getsize("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.exists("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.isabs("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.isdir("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.isfile("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.islink("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.ismount("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py")

print os.path.samefile("/Users/bjhl/PycharmProjects/python_demo/chapter9_file/demo_built_in.py", "./demo_built_in.py")

print __file__


