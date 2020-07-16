cmake_minimum_required(VERSION 3.13)
project(arm-linux-example C)
set(PROJECT_VERSION_MAJOR 1)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_VERSION_PATCH 0)

# Auto generate version.h through version.h.in
# You need to prepare version.h.in
configure_file(${CMAKE_SOURCE_DIR}/src/version.h.in ${CMAKE_SOURCE_DIR}/src/version.h)

# Compiler setting
if (APPLE)
    message("BUILD TARGET OS : ${CMAKE_HOST_SYSTEM_NAME}")
elseif(WINDOWS)
    message("BUILD TARGET OS : ${CMAKE_HOST_SYSTEM_NAME}")
elseif(UNIX)
    message("BUILD TARGET OS : ARM-Linux")
    set(CMAKE_C_COMPILER arm-linux-gnueabi-gcc)
    set(CMAKE_CXX_COMPILER arm-linux-gnueabi-g++)
endif ()

# Application build setting
add_executable(output src/main.c)