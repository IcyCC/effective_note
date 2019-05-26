cmake_minimum_required(VERSION 3.12)
project(stl)

set(CMAKE_CXX_STANDARD 14)

add_executable(stl src/SGI_alloc.hpp src/stl_iterator.hpp)