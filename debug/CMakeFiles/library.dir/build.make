# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/automaton641/Projects/game

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/automaton641/Projects/game/debug

# Include any dependencies generated for this target.
include CMakeFiles/library.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/library.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/library.dir/flags.make

CMakeFiles/library.dir/src/library/application.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/application.c.o: ../src/library/application.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/library.dir/src/library/application.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/application.c.o   -c /home/automaton641/Projects/game/src/library/application.c

CMakeFiles/library.dir/src/library/application.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/application.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/application.c > CMakeFiles/library.dir/src/library/application.c.i

CMakeFiles/library.dir/src/library/application.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/application.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/application.c -o CMakeFiles/library.dir/src/library/application.c.s

CMakeFiles/library.dir/src/library/player.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/player.c.o: ../src/library/player.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/library.dir/src/library/player.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/player.c.o   -c /home/automaton641/Projects/game/src/library/player.c

CMakeFiles/library.dir/src/library/player.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/player.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/player.c > CMakeFiles/library.dir/src/library/player.c.i

CMakeFiles/library.dir/src/library/player.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/player.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/player.c -o CMakeFiles/library.dir/src/library/player.c.s

CMakeFiles/library.dir/src/library/array.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/array.c.o: ../src/library/array.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/library.dir/src/library/array.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/array.c.o   -c /home/automaton641/Projects/game/src/library/array.c

CMakeFiles/library.dir/src/library/array.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/array.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/array.c > CMakeFiles/library.dir/src/library/array.c.i

CMakeFiles/library.dir/src/library/array.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/array.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/array.c -o CMakeFiles/library.dir/src/library/array.c.s

CMakeFiles/library.dir/src/library/game.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/game.c.o: ../src/library/game.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object CMakeFiles/library.dir/src/library/game.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/game.c.o   -c /home/automaton641/Projects/game/src/library/game.c

CMakeFiles/library.dir/src/library/game.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/game.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/game.c > CMakeFiles/library.dir/src/library/game.c.i

CMakeFiles/library.dir/src/library/game.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/game.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/game.c -o CMakeFiles/library.dir/src/library/game.c.s

CMakeFiles/library.dir/src/library/math.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/math.c.o: ../src/library/math.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object CMakeFiles/library.dir/src/library/math.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/math.c.o   -c /home/automaton641/Projects/game/src/library/math.c

CMakeFiles/library.dir/src/library/math.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/math.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/math.c > CMakeFiles/library.dir/src/library/math.c.i

CMakeFiles/library.dir/src/library/math.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/math.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/math.c -o CMakeFiles/library.dir/src/library/math.c.s

CMakeFiles/library.dir/src/library/memory_block.c.o: CMakeFiles/library.dir/flags.make
CMakeFiles/library.dir/src/library/memory_block.c.o: ../src/library/memory_block.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object CMakeFiles/library.dir/src/library/memory_block.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/library.dir/src/library/memory_block.c.o   -c /home/automaton641/Projects/game/src/library/memory_block.c

CMakeFiles/library.dir/src/library/memory_block.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/library.dir/src/library/memory_block.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/library/memory_block.c > CMakeFiles/library.dir/src/library/memory_block.c.i

CMakeFiles/library.dir/src/library/memory_block.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/library.dir/src/library/memory_block.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/library/memory_block.c -o CMakeFiles/library.dir/src/library/memory_block.c.s

# Object files for target library
library_OBJECTS = \
"CMakeFiles/library.dir/src/library/application.c.o" \
"CMakeFiles/library.dir/src/library/player.c.o" \
"CMakeFiles/library.dir/src/library/array.c.o" \
"CMakeFiles/library.dir/src/library/game.c.o" \
"CMakeFiles/library.dir/src/library/math.c.o" \
"CMakeFiles/library.dir/src/library/memory_block.c.o"

# External object files for target library
library_EXTERNAL_OBJECTS =

liblibrary.a: CMakeFiles/library.dir/src/library/application.c.o
liblibrary.a: CMakeFiles/library.dir/src/library/player.c.o
liblibrary.a: CMakeFiles/library.dir/src/library/array.c.o
liblibrary.a: CMakeFiles/library.dir/src/library/game.c.o
liblibrary.a: CMakeFiles/library.dir/src/library/math.c.o
liblibrary.a: CMakeFiles/library.dir/src/library/memory_block.c.o
liblibrary.a: CMakeFiles/library.dir/build.make
liblibrary.a: CMakeFiles/library.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking C static library liblibrary.a"
	$(CMAKE_COMMAND) -P CMakeFiles/library.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/library.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/library.dir/build: liblibrary.a

.PHONY : CMakeFiles/library.dir/build

CMakeFiles/library.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/library.dir/cmake_clean.cmake
.PHONY : CMakeFiles/library.dir/clean

CMakeFiles/library.dir/depend:
	cd /home/automaton641/Projects/game/debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/automaton641/Projects/game /home/automaton641/Projects/game /home/automaton641/Projects/game/debug /home/automaton641/Projects/game/debug /home/automaton641/Projects/game/debug/CMakeFiles/library.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/library.dir/depend
