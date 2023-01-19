#include <unistd.h>			
#include <fcntl.h>			
#include <sys/ioctl.h>		
#include <linux/i2c-dev.h>	
#include <bitset>
#include <iostream>

#include "i2c.h"

#define REG_ADDR 0x68 
using namespace std;

void I2CConnector::init()
{
    char *filename = (char*)"/dev/i2c-1";
    if ((file_i2c = open(filename, O_RDWR)) < 0)
    {
        printf("Failed to open the i2c bus");
        return;
    }
    if (ioctl(file_i2c, I2C_SLAVE, REG_ADDR) < 0)
    {
        printf("Failed to acquire bus access and/or talk to slave.\n");
        return;
    }
}

int I2CConnector::readData(int length)
{
    printf("Entering readData.\n");
    unsigned char buffer[length] = {0};
    if (read(file_i2c, buffer, length) != length)		//read() returns the number of bytes actually read, if it doesn't match then an error occurred (e.g. no response from the device)
    {
        //ERROR HANDLING: i2c transaction failed
        printf("Failed to read from the i2c bus.\n");
        return -1;
    }
    int value = convertData(buffer[0], buffer[1]);
    return value;
}


void I2CConnector::setConfig(int cfg)
{
    char buffer[1] = {0};    
    buffer[0] = cfg;
    int length = 1;			//<<< Number of bytes to write
    if (write(file_i2c, buffer, length) != length)		//write() returns the number of bytes actually written, if it doesn't match then an error occurred (e.g. no response from the device)
    {
        /* ERROR HANDLING: i2c transaction failed */
        printf("Failed to write to the i2c bus.\n");
    }
}

int I2CConnector::convertData(char msbyte, char lsbyte) {
    printf("Entering convertData.\n");
    bitset<32> bt(msbyte);
    bt<<=8;
    bitset<32> bt2(lsbyte);
    bt = bt | bt2;
    for (int i = 31; i >15; i--){
        bt.set(i, bt[15]);
    }
    cout<<bt[15]<<endl;
    cout<<bt.to_string()<<endl;
    unsigned long num = bt.to_ulong();
    int value = int(num);
    return value; 
}

I2CConnector::~I2CConnector()
{
    close(file_i2c);
}
