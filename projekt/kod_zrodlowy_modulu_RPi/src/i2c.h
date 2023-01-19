#ifndef I2CCONNECTOR
#define I2CCONNECTOR

class I2CConnector
{
    private:
        int file_i2c;
        int convertData(char msbyte, char lsbyte);
    public:
        void init();
        int readData(int length);
        void setConfig(int cfg);
        ~I2CConnector();
};

#endif