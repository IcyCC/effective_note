cmake_minimum_required(VERSION 3.12)
project(stl)

set(CMAKE_CXX_STANDARD 14)

add_executable(stl src/myallocator.hpp src/mysecallocator.hpp)