#!/usr/bin/env python3
import os
import mmap
import subprocess
import sys

def find_sources(source_directory):
    sources = []
    for file in os.listdir(source_directory):
        if file.endswith(".c") or file.endswith(".h"):
            sources.append(os.path.join(source_directory, file))
    return sources

class Library:
    def __init__(self, name, dependecies = []):
        self.name = name
        self.dependecies = dependecies
        self.include_path = "./src/"
        self.source_directory = "./src/"
        self.tabs = 0
        self.sources = []
        self.linked_libraries = []
        self.build_type = "debug"
        self.makecontent = """
cmake_minimum_required(VERSION 3.13.4)
project (TheProject)
"""
    def find_sources(self):
        for file in os.listdir(self.source_directory):
            if file.endswith(".c") or file.endswith(".h"):
                self.sources.append(os.path.join(self.source_directory, file))
    def run(self, target):
            build_directory = self.build_type
            isdir = os.path.isdir(build_directory) 
            if not isdir:
                print("[info] build directory'" + build_directory + "' not found...") 
                subprocess.run(["mkdir", build_directory])
                os.chdir(build_directory)
                if build_directory == "debug":
                    subprocess.run(["cmake", "-DCMAKE_BUILD_TYPE=Debug", ".."])
                else:
                    subprocess.run(["cmake", "-DCMAKE_BUILD_TYPE=Release", ".."])
                subprocess.run(["make"])
                os.chdir("..")
            self.makecontent += "set( " + self.name +"_sources\n"
            for source in self.sources:
                self.makecontent += source + "\n"
            self.makecontent += ")\n"
            self.makecontent += "add_library(" + self.name + " ${" + self.name + "_sources} )\n"
            self.makecontent += "target_include_directories( " + self.name + " PRIVATE " + self.include_path + " )\n"
            self.makecontent += "\n"
            target_sources_directory = self.include_path + target
            isdir = os.path.isdir(target_sources_directory) 
            if not isdir:
                print("[ERROR] target '" + target + "' not found...") 
                sys.exit()
            target_sources = find_sources(target_sources_directory)
            self.makecontent += "add_executable( " + target + "\n"
            for source in target_sources:
                self.makecontent += source + "\n"
            self.makecontent += ")\n"
            self.makecontent += "target_include_directories( " + target + " PRIVATE " + self.include_path + " )\n"
            self.makecontent += "target_link_libraries( " + target + " " + self.name + " )\n"
            for linked_library in self.linked_libraries:
                self.makecontent += "target_link_libraries( " + target + " " + linked_library + " )\n"
            filename = "CMakeLists.txt"
            myfile = open(filename, 'w')
            myfile.write(self.makecontent)
            myfile.close()
            os.chdir(self.build_type)
            print("[" + self.build_type + "] " + "building...")
            subprocess.run(["make"])
            print("[" + self.build_type + "] " + "...finished building")
            print("[" + self.build_type + "] " + "running...")
            os.chdir("..")
            subprocess.run([ "./" + self.build_type + "/" + target ])
            print("[" + self.build_type + "] " + "...finished running")

argc = len(sys.argv)
argv = sys.argv
build_types = ["debug", "release"]
library = Library("library")
library.source_directory += "library/"
library.linked_libraries = ["pthread"]
library.find_sources()
target = "game"
if argc > 1:
    target = argv[1]
    if target == "clean":
        print("[clean] cleaning...")
        for build_directory in build_types:
            subprocess.run(["rm","-r",build_directory])
        sys.exit()
    if argc > 2:
        library.build_type = argv[2]
        if not library.build_type in build_types:
            print("invalid build type")
            sys.exit()


library.run(target)