
cmake_minimum_required(VERSION 3.13.4)
project (TheProject)
set( library_sources
./src/library/game.h
./src/library/application.c
./src/library/math.h
./src/library/player.c
./src/library/memory_block.h
./src/library/array.c
./src/library/game.c
./src/library/application.h
./src/library/math.c
./src/library/memory_block.c
./src/library/player.h
./src/library/array.h
)
add_library(library ${library_sources} )
target_include_directories( library PRIVATE ./src/ )

add_executable( game
./src/game/main.c
)
target_include_directories( game PRIVATE ./src/ )
target_link_libraries( game library )
target_link_libraries( game pthread )
