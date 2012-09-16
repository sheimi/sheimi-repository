project(histogram)
find_package(OpenCV REQUIRED)
add_executable(histogram histogram)
target_link_libraries(histogram ${OpenCV_LIBS})
