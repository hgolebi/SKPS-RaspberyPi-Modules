all: adc

adc:
	$(CXX) tcp_connection.cpp adc.cpp i2c.cpp -o adc $(LDFLAGS)

clean:
	rm -f adc *.o
