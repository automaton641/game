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
include CMakeFiles/game.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/game.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/game.dir/flags.make

CMakeFiles/game.dir/src/game/main.c.o: CMakeFiles/game.dir/flags.make
CMakeFiles/game.dir/src/game/main.c.o: ../src/game/main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/game.dir/src/game/main.c.o"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/game.dir/src/game/main.c.o   -c /home/automaton641/Projects/game/src/game/main.c

CMakeFiles/game.dir/src/game/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/game.dir/src/game/main.c.i"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/automaton641/Projects/game/src/game/main.c > CMakeFiles/game.dir/src/game/main.c.i

CMakeFiles/game.dir/src/game/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/game.dir/src/game/main.c.s"
	/usr/bin/clang $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/automaton641/Projects/game/src/game/main.c -o CMakeFiles/game.dir/src/game/main.c.s

# Object files for target game
game_OBJECTS = \
"CMakeFiles/game.dir/src/game/main.c.o"

# External object files for target game
game_EXTERNAL_OBJECTS =

game: CMakeFiles/game.dir/src/game/main.c.o
game: CMakeFiles/game.dir/build.make
game: liblibrary.a
game: CMakeFiles/game.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/automaton641/Projects/game/debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable game"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/game.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/game.dir/build: game

.PHONY : CMakeFiles/game.dir/build

CMakeFiles/game.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/game.dir/cmake_clean.cmake
.PHONY : CMakeFiles/game.dir/clean

CMakeFiles/game.dir/depend:
	cd /home/automaton641/Projects/game/debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/automaton641/Projects/game /home/automaton641/Projects/game /home/automaton641/Projects/game/debug /home/automaton641/Projects/game/debug /home/automaton641/Projects/game/debug/CMakeFiles/game.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/game.dir/depend

