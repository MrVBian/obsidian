
```shell
git clone https://github.com/libcpr/cpr.git
cd cpr && mkdir build && cd build
cmake .. -DCMAKE_POSITION_INDEPENDENT_CODE=ON
make
sudo make install

# 注释掉influxdb-cxx-0.7.3/CMakeLists.txt
# if (INFLUXCXX_TESTING)
#   enable_testing()
#   add_subdirectory("test")
# endif()


git clone https://github.com/offa/influxdb-cxx.git
cd influxdb-cxx
mkdir build
cd build
cmake ..
make
sudo make install
```