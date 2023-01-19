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
    unsigned char buffer[length] = {0}; //read value will be stored in this buffer
    if (read(file_i2c, buffer, length) != length)
    {
        // read() returns the number of bytes actually read
        // if it doesn't match then something is wrong (e.g. no response from the device)
        printf("Failed to read from the i2c bus.\n");
        return -1;
    }
    int value = convertData(buffer[0], buffer[1]); //read value need convertion from bytes to integer
    return value;
}


void I2CConnector::setConfig(int cfg)
{
    char buffer[1] = {0};
    buffer[0] = cfg;   // Our configuration is placed into the buffer. It will be written from the buffer into the register of the device.
    int length = 1;
    if (write(file_i2c, buffer, length) != length)
        // write() returns the number of bytes actually read,
        // if it doesn't match then something is wrong (e.g. no response from the device)
        printf("Failed to write to the i2c bus.\n");
    }
}

int I2CConnector::convertData(char msbyte, char lsbyte) {
    /*
    In our configuration, device sends two bytes of data. Because we're using 12 bit precision,
    the first 4 bits are the same as the fifth bit, which is the sign of our number.
    In order to create signed int from these bytes we have to:

    > create 32 bit bitset with more significant byte :
    ........................SSSSSAAA
    > shift it left by 8 positions :
    ................SSSSSAAA00000000 :
    > create 32 bit bitset with lest significant byte :
    ........................bbbbbbbb
    > Use OR operation on both bitsets to combine them:
    ................SSSSSAAAbbbbbbbb:
    > Set first 16 bits to match the value of 17th bit :
    SSSSSSSSSSSSSSSSSSSSSAAAbbbbbbbb
    */

    printf("Entering convertData.\n");
    bitset<32> bt(msbyte);                  // bitset with more significant byte
    bt<<=8;                                 // binary shift left
    bitset<32> bt2(lsbyte);                 // biteset with less significant byte
    bt = bt | bt2;                          // combining two bitsets using OR operation
    for (int i = 31; i >15; i--){
        bt.set(i, bt[15]);                  // seting first 16 bits to match the 17th bit
    }
    cout<<bt[15]<<endl;
    cout<<bt.to_string()<<endl;
    unsigned long num = bt.to_ulong();      // bitset offers built in conversion to ulong
    int value = int(num);                   // next we have to convert ulong to int
    return value;
}

I2CConnector::~I2CConnector()
{
    close(file_i2c);
}
